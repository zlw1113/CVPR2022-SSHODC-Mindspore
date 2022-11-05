# The Implementation with MindSpore of CVPR 2022 MAVOC Challenge's Champion Proposal

**Paper Link:**   https://ieeexplore.ieee.org/document/9857095/

**Award certificate**

<p align="left">
  <img src="./tutorials/MAVOC_Track 1_Champion.png" width=360 />
</p>

<p align="left">
  <img src="./tutorials/MAVOC_Track 2_Champion.png" width=360 />
</p>

## Introduction
Multi-modal aerial view object classification (MAVOC) in Automatic target recognition (ATR), although an important and challenging problem, has been under studied. This paper firstly finds that fine-grained data, class imbalance and various shooting conditions preclude the representational ability of general image classification. Moreover, the MAVOC dataset has scene aggregation characteristics. By exploiting these properties, we propose Scene Clustering Based Pseudo-labeling Strategy (SCP-Label), a simple yet effective method to employ in post-processing. The SCP-Label brings greater accuracy by assigning the same label to objects within the same scene while also mitigating bias and confusion with model ensembles. Its performance surpasses the official baseline by a large margin of +20.57% Accuracy on Track 1 (SAR), and +31.86% Accuracy on Track 2 (SAR+EO), demonstrating the potential of SCP-Label as post-processing. Finally, we win the championship both on Track1 and Track2 in the CVPR 2022 Perception Beyond the Visible Spectrum (PBVS) Workshop MAVOC Challenge.
	
### Experiments Results

| Backbone            | Under-sample| Augmentation Method       | Top-1 Accuracy (%) |
|:--------------------|:------------|:------------              |:------------       |
| Resnet50            | all data    | Rotation+Flipping+Cutmix  | 17.10              |
| Efficientnet-b1     | all data    | Rotation+Flipping+Cutmix  | 15.88              |
| Swin-Transformer    | all data    | Rotation+Flipping+Cutmix  | 16.88              |
| DenseNet161         | all data    | Rotation+Flipping+Cutmix  | 18.05              |
| MobileNetV3-large   | 1741        | Rotation+Flipping+Cutmix  | 21.30              |

## Installation

### Dependency

- mindspore >= 1.8.1
- numpy >= 1.17.0
- pyyaml >= 5.3
- tqdm
- openmpi 4.0.3 (for distributed mode) 

To install the dependency, please run
```shell
pip install -r requirements.txt
```

### Prepare datasets


Please make sure the dataset is placed as shown below, where val_no_label.json represents the unlabeled portion of the training set

```text
mindspore_rooftophsi
├── data
│   ├── RIT-HS20
│   │   ├── annotationsjson
│   │   │   ├── instances_train_s10.json
│   │   │   ├── instances_test_id.json
│   │   │   ├── val_no_label.json
│   │   │   ├── test.json
│   │   ├── spectral
```

### Quickly Test
```shell


# test
bash run_eval_ascend.sh [VALIDATION_JSON_FILE] [CHECKPOINT_PATH]

# Submission.json will be generated in the current workspace directory

```

### Training


```shell
#  pre-training
python train.py --stage 1 

# Generate pseudo labels

python eval.py --checkpoint_path xxx.ckpt

mv submission.json data/RIT-HS20/annotationsjson/

python data/RIT-HS20/annotationsjson/pseudo1.py

python data/RIT-HS20/annotationsjson/pseudo2.py

# the second stage of training
python train.py --stage 1 

```

### Testing


```shell

# test
python eval.py --checkpoint_path xxx.ckpt

```

