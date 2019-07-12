import pickle
import numpy as np
from argparse import ArgumentParser

def print_coco_results(results):
    
    def _print(result, ap=1, iouThr=None, areaRng='all', maxDets=100 ):
        iStr = ' {:<18} {} @[ IoU={:<9} | area={:>6s} | maxDets={:>3d} ] = {:0.3f}'
        titleStr = 'Average Precision' if ap == 1 else 'Average Recall'
        typeStr = '(AP)' if ap==1 else '(AR)'
        iouStr = '{:0.2f}:{:0.2f}'.format(.5, .95) \
            if iouThr is None else '{:0.2f}'.format(iouThr)
        print(iStr.format(titleStr, typeStr, iouStr, areaRng, maxDets, result))
    
    stats = np.zeros((12,))
    stats[0] = _print(results[0], 1)
    stats[1] = _print(results[1], 1, iouThr=.5)
    stats[2] = _print(results[2], 1, iouThr=.75)
    stats[3] = _print(results[3], 1, areaRng='small')
    stats[4] = _print(results[4], 1, areaRng='medium')
    stats[5] = _print(results[5], 1, areaRng='large')
    stats[6] = _print(results[6], 0, maxDets=1)
    stats[7] = _print(results[7], 0, maxDets=10)
    stats[8] = _print(results[8], 0)
    stats[9] = _print(results[9], 0, areaRng='small')
    stats[10] = _print(results[10], 0, areaRng='medium')
    stats[11] = _print(results[11], 0, areaRng='large')

def get_coco_style_results(filename, task='bbox', metric=None, verbose=1):

    with open(filename, "rb") as f:
        eval_output = pickle.load(f)
        
    if metric is None:
        metrics = ['AP','AP50','AP75','APs','APm','APl', 
                   'AR1','AR10','AR100','ARs','ARm','ARl']
    elif isinstance(metric, list):
        metrics = metric
    else:
        metrics = [metric]
        
    for metric_name in metrics:
        assert metric_name in ['AP','AP50','AP75','APs','APm','APl', 
                   'AR1','AR10','AR100','ARs','ARm','ARl']
        
    results = np.zeros((20,6,len(metrics)), dtype='float32')

    for corr_i, distortion in enumerate(eval_output):
        for severity in eval_output[distortion]:
            for metric_j, metric_name in enumerate(metrics):
                mAP = eval_output[distortion][severity][task][metric_name]
                results[corr_i, severity, metric_j] = mAP
                if verbose > 2:
                    print(distortion, severity, mAP)
                    
    P = results[0,0,:]
    mPC = np.mean(results[:15,1:,:], axis=(0,1))
    rPC = mPC/P
    
    
    if metric == None:
        if verbose > 1:
            print("\nPerformance on Clean Data [P] ({})".format(task))
            print_coco_results(P)
        if verbose > 0:
            print("\nMean Performance under Corruption [mPC] ({})".format(task))
            print_coco_results(mPC)
        if verbose > 1:
            print("\nRealtive Performance under Corruption [rPC] ({})".format(task))
            print_coco_results(rPC)
    else:
        if verbose > 1:
            print("\nPerformance on Clean Data [P] ({})".format(task))
            for metric_i, metric_name in enumerate(metrics):
                print("{:5} =  {:0.3f}".format(metric_name, P[metric_i]))
        if verbose > 0:
            print("\nMean Performance under Corruption [mPC] ({})".format(task))
            for metric_i, metric_name in enumerate(metrics):
                print("{:5} =  {:0.3f}".format(metric_name, mPC[metric_i]))
        if verbose > 1:
            print("\nRealtive Performance under Corruption [rPC] ({})".format(task))
            for metric_i, metric_name in enumerate(metrics):
                print("{:5} => {:0.1f} %".format(metric_name, rPC[metric_i] * 100))
                
    return results


def get_voc_style_results(filename, verbose=1):
    
    with open(filename, "rb") as f:
        eval_output = pickle.load(f)

    results = np.zeros((20,6,20), dtype='float32')

    for i, distortion in enumerate(eval_output):
        for severity in eval_output[distortion]:
            mAP = [eval_output[distortion][severity][j]['ap'] for j in range(len(eval_output[distortion][severity]))]
            results[i, severity,:] = mAP
            if verbose > 2:
                print(distortion, severity, mAP)
              
    P = results[0,0,:]
    mPC = np.mean(results[:15,1:,:], axis=(0,1))
    rPC = mPC/P
    
    if verbose > 1:
        print("{:48} = {:0.3f}".format("Performance on Clean Data [P] in AP50", np.mean(P)))
    if verbose > 0:
        print("{:48} = {:0.3f}".format("Mean Performance under Corruption [mPC] in AP50", np.mean(mPC)))
    if verbose > 1:
        print("{:48} = {:0.1f}".format("Realtive Performance under Corruption [rPC] in %", np.mean(rPC)*100))
                
    return np.mean(results, axis=2, keepdims=True)



def get_results(filename, dataset='coco', task='bbox', metric=None, verbose=1):
    assert dataset in ['coco', 'voc', 'cityscapes']
    
    if dataset in ['coco', 'cityscapes']:
        results = get_coco_style_results(filename, task=task, metric=metric, verbose=verbose)
    elif dataset == 'voc':
        if task is not 'bbox':
            print("Only bbox analysis is supported for Pascal VOC")
            print("Will report bbox results\n")
        if metric not in [None, ['AP'], ['AP50']]:
            print("Only the AP50 metric is supported for Pascal VOC")
            print("Will report AP50 metric\n")
        results = get_voc_style_results(filename, verbose=verbose)
        
    return results

def get_distortions_from_file(filename):
    
    with open(filename, "rb") as f:
        eval_output = pickle.load(f)
        
    return get_distortions_from_eval_output(eval_output)


def get_distortions_from_eval_output(eval_output):
    distortions = []
    for i, distortion in enumerate(eval_output):
        distortions.append(distortion.replace("_", " "))
    return distortions


def main():
    parser = ArgumentParser(description='Corruption Result Analysis')
    parser.add_argument('filename', help='result file path')
    parser.add_argument(
        '--dataset',  
        type=str,
        choices=['coco', 'voc', 'cityscapes'],
        default='coco',
        help='dataset type')
    parser.add_argument(
        '--task', 
        type=str,
        nargs='+',
        choices=['bbox', 'segm'],
        default=['bbox'],
        help='task to report')
    parser.add_argument(
        '--metric', 
        nargs='+',
        choices=[None,'AP','AP50','AP75','APs','APm','APl', 
                   'AR1','AR10','AR100','ARs','ARm','ARl'],
        default=None,
        help='metric to report')
    parser.add_argument(
        '--verbose',
        type=int,
        default=1, 
        help='verbosity: 0 = none, 1 = mPC, 2 = P, mPC and rPC')
    
    args = parser.parse_args()
    
    print(args)
    
    for task in args.task:
        get_results(args.filename, 
                    dataset=args.dataset, 
                    task=task, 
                    metric=args.metric, 
                    verbose=args.verbose)
        
if __name__ == '__main__':
    main()
    
