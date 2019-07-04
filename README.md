# robust-detection-benchmark

General project repo, starting point for users & hosting benchmark table:
https://github.com/bethgelab/robust-detection-benchmark (this repo)

Stylize arbitrary datasets:
https://github.com/bethgelab/stylize-datasets

Corrupt arbitrary datasets:
https://github.com/bethgelab/add-common-image-corruptions

Object detection:
https://github.com/bethgelab/robust_object_detection

## Workflow

1. clone
2. get data (COCO, Pascal) & MMdetect
3. stylize.sh
4. train object detector
5. corrupt datasets & evaluate

## Benchmark

Coco: Results are evaluated on COCO 2017val.
Cityscapes: Results are evaluated on Cityscapes val.
Pascal: Results are evaluated on Pascal VOC 2007 test.

Results are sorted by their absolute performance under corruption.

### Coco

#### Object detection:

Model  | Backbone  | Style   | Lr schd | box AP clean | box AP corr. | box % |
:-----:|:---------:|:-------:|:-------:|:------------:|:------------:|:-----:|
Faster R-CNN | X-101-64x4d-FPN | pytorch |1x | 41.3   | 23.4         | 56.6  |
Faster R-CNN | X-101-32x4d-FPN | pytorch |1x | 40.1   | 22.3         | 55.5  |
Faster R-CNN | R-101-FPN | pytorch | 1x      | 38.5   | 20.9         | 54.2  |
Cascade Mask R-CNN | R-50-FPN  | pytorch | 1x| 41.2   | 20.7         | 50.2  |
Faster R-CNN Combined | R-50-FPN | pytorch | 1x | 34.6 | 20.4        | 58.9  |
Cascade R-CNN | R-50-FPN  | pytorch | 1x     | 40.4   | 20.1         | 49.7  |
Mask R-CNN   | R-50-FPN  | pytorch | 1x      | 37.3   | 18.7         | 50.1  |
Faster R-CNN | R-50-FPN  | pytorch | 1x      | 36.3   | 18.2         | 50.2  |
RetinaNet    | R-50-FPN  | pytorch | 1x      | 35.6   | 17.8         | 50.1  |
Faster R-CNN Stylized | R-50-FPN | pytorch | 1x | 21.5 | 14.1        | 65.6  |

#### Instance Segmentation:

Model  | Backbone  | Style   | Lr schd | mask AP clean | mask AP corr. | mask % |
:-----:|:---------:|:-------:|:-------:|:-------------:|:-------------:|:------:|
Mask R-CNN Combined  | R-50-FPN | pytorch | 1x | 32.9  | 19.0          | 57.7   |
Cascade Mask R-CNN | R-50-FPN  | pytorch | 1x| 35.7    | 17.6          | 49.3   |
Mask R-CNN   | R-50-FPN  | pytorch | 1x      | 34.2    | 16.8          | 49.1   |
Mask R-CNN Stylizes  | R-50-FPN | pytorch | 1x | 30.5  | 13.2          | 64.1   |


### Pascal VOC

#### Object detection:

Model  | Backbone  | Style   | Lr schd | box AP50 clean | box AP50 corr. | box % |
:-----:|:---------:|:-------:|:-------:|:--------------:|:--------------:|:-----:|
Faster R-CNN Combined | R-50-FPN | pytorch | 1x | 80.4  | 56.2           | 69.9  |
Faster R-CNN Stylized | R-50-FPN | pytorch | 1x | 68.0  | 50.0           | 73.5  |
Faster R-CNN | R-50-FPN  | pytorch | 1x      | 80.5     | 48.6           | 60.4  |


### Cityscapes

#### Object detection:

Model  | Backbone  | Style   | Lr schd | box AP clean | box AP corr. | box % |
:-----:|:---------:|:-------:|:-------:|:------------:|:------------:|:-----:|
Faster R-CNN Combined | R-50-FPN | pytorch | 1x | 36.3 | 17.2        | 47.4  |
Faster R-CNN Stylized | R-50-FPN | pytorch | 1x | 28.5 | 14.7        | 51.5  |
Faster R-CNN | R-50-FPN  | pytorch | 1x      | 36.4   | 12.2         | 33.4  |
Mask R-CNN   | R-50-FPN  | pytorch | 1x      | 37.5   | 11.7         | 31.1  |



#### Instance Segmentation:

Model  | Backbone  | Style   | Lr schd | mask AP clean | mask AP corr. | mask % |
:-----:|:---------:|:-------:|:-------:|:-------------:|:-------------:|:------:|
Mask R-CNN Combined  | R-50-FPN | pytorch | 1x | ----  | ----          | ----   |
Mask R-CNN   | R-50-FPN  | pytorch | 1x      | 32.7    | 10.0          | 30.5   |
Mask R-CNN Stylizes  | R-50-FPN | pytorch | 1x | ----  | ----          | ----   |


## Citation

If you use our code or the benchmark, please cite:
```
@article{xyz2019,
  title={xxx},
  author={xyz},
  journal={arXiv:},
  year={2019}
}
```
