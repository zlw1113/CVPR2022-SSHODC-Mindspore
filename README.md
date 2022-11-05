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

