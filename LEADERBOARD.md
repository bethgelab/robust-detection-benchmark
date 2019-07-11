# Leaderboard

Results are sorted by their absolute performance under corruption.

## ResNet-50 Backbone Track

In this section only models with a ResNet 50 Backbone with Feature Pyramid Networks are listed.

### Coco

#### Object detection:

Model  | Backbone  | box AP clean | box AP corr. | box % |
:-----:|:---------:|:------------:|:------------:|:-----:|
Cascade Mask R-CNN | R-50-FPN    | 41.2  | 20.7  | 50.2  |
Faster R-CNN Combined | R-50-FPN | 34.6  | 20.4  | 58.9  |
Cascade R-CNN | R-50-FPN         | 40.4  | 20.1  | 49.7  |
Mask R-CNN   | R-50-FPN          | 37.3  | 18.7  | 50.1  |
Faster R-CNN | R-50-FPN          | 36.3  | 18.2  | 50.2  |
RetinaNet    | R-50-FPN          | 35.6  | 17.8  | 50.1  |
Faster R-CNN Stylized | R-50-FPN | 21.5  | 14.1  | 65.6  |

#### Instance Segmentation:

Model  | Backbone  | mask AP clean | mask AP corr. | mask % |
:-----:|:---------:|:-------------:|:-------------:|:------:| 
Mask R-CNN Combined | R-50-FPN | 32.9  | 19.0      | 57.7   |
Cascade Mask R-CNN  | R-50-FPN | 35.7  | 17.6      | 49.3   |
Mask R-CNN          | R-50-FPN | 34.2  | 16.8      | 49.1   |
Mask R-CNN Stylizes | R-50-FPN | 30.5  | 13.2      | 64.1   |


### Pascal VOC

#### Object detection:

Model  | Backbone  | box AP50 clean | box AP50 corr. | box % |
:-----:|:---------:|:--------------:|:--------------:|:-----:|
Faster R-CNN Combined | R-50-FPN | 80.4 | 56.2       | 69.9  |
Faster R-CNN Stylized | R-50-FPN | 68.0 | 50.0       | 73.5  |
Faster R-CNN | R-50-FPN          | 80.5 | 48.6       | 60.4  |


### Cityscapes

#### Object detection:

Model  | Backbone  | box AP clean | box AP corr. | box % |
:-----:|:---------:|:------------:|:------------:|:-----:|
Faster R-CNN Combined | R-50-FPN | 36.3 | 17.2   | 47.4  |
Faster R-CNN Stylized | R-50-FPN | 28.5 | 14.7   | 51.5  |
Faster R-CNN | R-50-FPN  | 36.4   | 12.2         | 33.4  |
Mask R-CNN   | R-50-FPN  | 37.5   | 11.7         | 31.1  |



#### Instance Segmentation:

Model  | Backbone  | mask AP clean | mask AP corr. | mask % |
:-----:|:---------:|:-------------:|:-------------:|:------:|
Mask R-CNN Combined  | R-50-FPN | 32.1  | 14.9     | 46.3   |
Mask R-CNN Stylizes  | R-50-FPN | 23.0  | 11.3     | 49.2   |
Mask R-CNN   | R-50-FPN  | 32.7    | 10.0          | 30.5   |




## Unrestricted Track

Any mdel independent of it's backbone can participate in this track.

### Coco

#### Object detection:

Model  | Backbone  | box AP clean | box AP corr. | box % |
:-----:|:---------:|:------------:|:------------:|:-----:|
Hybrid Task Cascade | X-101-64x4d-FPN-DCN | 50.6 | 32.7 | 64.7  |
Faster R-CNN | X-101-32x4d-FPN-DCN | 43.4   | 26.7 | 61.6  |
Faster R-CNN | X-101-64x4d-FPN   | 41.3   | 23.4 | 56.6  |
Mask R-CNN   | R-50-FPN-DCN      | 41.1   | 23.3 | 56.7  |
Faster R-CNN | R-50-FPN-DCN      | 40.0   | 12.4 | 56.1  |
Faster R-CNN | X-101-32x4d-FPN   | 40.1   | 22.3 | 55.5  |
Faster R-CNN | R-101-FPN         | 38.5   | 20.9 | 54.2  |
Cascade Mask R-CNN | R-50-FPN    | 41.2   | 20.7 | 50.2  |
Faster R-CNN Combined | R-50-FPN | 34.6   | 20.4 | 58.9  |
Cascade R-CNN | R-50-FPN         | 40.4   | 20.1 | 49.7  |
Mask R-CNN   | R-50-FPN          | 37.3   | 18.7 | 50.1  |
Faster R-CNN | R-50-FPN          | 36.3   | 18.2 | 50.2  |
RetinaNet    | R-50-FPN          | 35.6   | 17.8 | 50.1  |
Faster R-CNN Stylized | R-50-FPN | 21.5   | 14.1 | 65.6  |

#### Instance Segmentation:

Model  | Backbone  | mask AP clean | mask AP corr. | mask % |
:-----:|:---------:|:-------------:|:-------------:|:------:|
Hybrid Task Cascade | X-101-64x4d-FPN-DCN | 43.8 | 28.1 | 64.0  | 
Mask R-CNN          | R-50-FPN-DCN | 37.2  | 20.7  | 55.7   |
Mask R-CNN Combined | R-50-FPN | 32.9  | 19.0      | 57.7   |
Cascade Mask R-CNN  | R-50-FPN | 35.7  | 17.6      | 49.3   |
Mask R-CNN          | R-50-FPN | 34.2  | 16.8      | 49.1   |
Mask R-CNN Stylizes | R-50-FPN | 30.5  | 13.2      | 64.1   |


### Pascal VOC

#### Object detection:

Model  | Backbone  | box AP50 clean | box AP50 corr. | box % |
:-----:|:---------:|:--------------:|:--------------:|:-----:|
Faster R-CNN Combined | R-50-FPN | 80.4 | 56.2       | 69.9  |
Faster R-CNN Stylized | R-50-FPN | 68.0 | 50.0       | 73.5  |
Faster R-CNN | R-50-FPN          | 80.5 | 48.6       | 60.4  |


### Cityscapes

#### Object detection:

Model  | Backbone  | box AP clean | box AP corr. | box % |
:-----:|:---------:|:------------:|:------------:|:-----:|
Faster R-CNN Combined | R-50-FPN | 36.3 | 17.2   | 47.4  |
Faster R-CNN Stylized | R-50-FPN | 28.5 | 14.7   | 51.5  |
Faster R-CNN | R-50-FPN  | 36.4   | 12.2         | 33.4  |
Mask R-CNN   | R-50-FPN  | 37.5   | 11.7         | 31.1  |



#### Instance Segmentation:

Model  | Backbone  | mask AP clean | mask AP corr. | mask % |
:-----:|:---------:|:-------------:|:-------------:|:------:|
Mask R-CNN Combined  | R-50-FPN | 32.1  | 14.9     | 46.3   |
Mask R-CNN Stylizes  | R-50-FPN | 23.0  | 11.3     | 49.2   |
Mask R-CNN   | R-50-FPN  | 32.7    | 10.0          | 30.5   |


## How to contribute

Coco: Results are evaluated on COCO 2017val.
Cityscapes: Results are evaluated on Cityscapes val.
Pascal: Results are evaluated on Pascal VOC 2007 test.

## Methods


