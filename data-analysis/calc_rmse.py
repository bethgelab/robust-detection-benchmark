import mmcv
from mmcv.runner import obj_from_dict

import mmdet.datasets as datasets
import numpy as np
from tqdm import tqdm
import csv
from imagecorruptions import corrupt, get_corruption_names
import os.path as osp
import pickle

# Hack into the dataset classes such that they return rmse value between clean and corrupted instead of the images
class VOCRmse(datasets.VOCDataset):
    def prepare_test_img(self, idx):
        img_info = self.img_infos[idx]
        img = mmcv.imread(osp.join(self.img_prefix, img_info['filename']))
        rmse = np.zeros((5, 19))
        for c in range(19):
            for s in np.arange(1, 6):
                try:
                    corrupted_img = corrupt(img, severity=s, corruption_number=c)
                    rmse[s-1][c] = np.sqrt(np.mean((img - corrupted_img)**2))
                except:
                    print("Error occured in file %s with index %d for corruption %d severity %d"%(img_info['filename'], idx, c, s))
                    exit()
        return rmse
    
class CocoRmse(datasets.CocoDataset):
    def prepare_test_img(self, idx):
        img_info = self.img_infos[idx]
        img = mmcv.imread(osp.join(self.img_prefix, img_info['filename']))
        rmse = np.zeros((5, 19))
        for c in range(19):
            for s in np.arange(1, 6):
                corrupted_img = corrupt(img, severity=s, corruption_number=c)
                try:
                    rmse[s-1][c] = np.sqrt(np.mean((img - corrupted_img)**2))
                except:
                    e = sys.exc_info()[0]
                    print("Error occured in file %s with index %d for corruption %d severity %d"%(img_info['filename'], idx, c, s))
                    print(e)
                    exit()
        return rmse

if __name__ == "__main__":
    corruption_names = get_corruption_names('all')
    
    voc_test_config = mmcv.Config.fromfile('rmse_configs/voc07test.py')
    # hack the config to obtain a VocRmse dataset and add CocoRmse to the available datasets
    voc_rmse_config = voc_test_config.data.test
    voc_rmse_config.type = 'VOCRmse'
    datasets.VOCRmse = VOCRmse
    
    # obtain the dataloader
    voc_data = obj_from_dict(voc_rmse_config, datasets, dict(test_mode=True))
    dataloader_voc = datasets.build_dataloader(voc_data, imgs_per_gpu=1, workers_per_gpu=32, num_gpus=1, dist=False, shuffle=False)
    voc_rmse = np.zeros([voc_data.__len__(), 5, 19])
    
    print('starting with voc')
    for i, data in tqdm(enumerate(dataloader_voc)):
        voc_rmse[i, :, :] = data.numpy()

    # calculate mean rmse over all test images
    mean_voc_rmse = np.mean(voc_rmse, axis=0)
    
    # save everything to result file
    #pickle.dump(voc_rmse, open("../raw_data/pascal_voc/vocrmse.pkl", "wb"))

    with open('../raw_data/pascal_voc/voc_rmse.csv', 'w') as fp:
        writer = csv.writer(fp, quoting=csv.QUOTE_NONNUMERIC)
        writer.writerow(['corruption', 'severity', 'RMSE'])
        for severity, row in enumerate(mean_voc_rmse):
            for corruption_number, rmse_value in enumerate(row):
                corruption_name = corruption_names[corruption_number]
                writer.writerow([corruption_name, severity+1, rmse_value])
                
    print('voc finished')
    
    coco_test_config = mmcv.Config.fromfile('rmse_configs/coco17test.py')
    # hack the config to obtain a CocoRmse dataset and add CocoRmse to the available datasets
    coco_rmse_config = coco_test_config.data.test
    coco_rmse_config.type = 'CocoRmse'
    datasets.CocoRmse = CocoRmse
    
    # obtain the dataloader
    coco_data = obj_from_dict(coco_rmse_config, datasets, dict(test_mode=True))
    dataloader_coco = datasets.build_dataloader(coco_data, imgs_per_gpu=1, workers_per_gpu=32, num_gpus=1, dist=False, shuffle=False)
    coco_rmse = np.zeros([coco_data.__len__(), 5, 19])
    
    print('starting with coco')
    for i, data in tqdm(enumerate(dataloader_coco)):
        coco_rmse[i, :, :] = data.numpy()

    # calculate mean rmse over all test images
    mean_coco_rmse = np.mean(coco_rmse, axis=0)
    
    # save everything to result file
    #pickle.dump(coco_rmse, open("../raw_data/coco/cocormse.pkl", "wb"))

    with open('../raw_data/coco/coco_rmse.csv', 'w') as fp:
        writer = csv.writer(fp, quoting=csv.QUOTE_NONNUMERIC)
        writer.writerow(['corruption', 'severity', 'RMSE'])
        for severity, row in enumerate(mean_coco_rmse):
            for corruption_number, rmse_value in enumerate(row):
                corruption_name = corruption_names[corruption_number]
                writer.writerow([corruption_name, severity+1, rmse_value])
                
    print('coco finished')

