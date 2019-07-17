# dataset settings
data_root = '/gpfs01/bethge/data/pascal_voc/'
img_norm_cfg = dict(
    mean=[123.675, 116.28, 103.53], std=[58.395, 57.12, 57.375], to_rgb=True)
data = dict(
    imgs_per_gpu=2,
    workers_per_gpu=2,
    test=dict(
        type='VOCDataset',
        ann_file=data_root + 'VOCdevkit/VOC2007/ImageSets/Main/test.txt',
        img_prefix=data_root + 'VOCdevkit/VOC2007/',
        img_scale=(1000, 600),
        img_norm_cfg=img_norm_cfg,
        size_divisor=32,
        flip_ratio=0,
        with_mask=False,
        with_label=False,
        test_mode=True))
