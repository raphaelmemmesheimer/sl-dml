# SL-DML: Signal Level Deep Metric Learning for MultimodalOne-Shot Action Recognition

![SL-DML Overview](images/example.png)

This repository contains the code for SL-DML, a metric learning approach for one-shot action recognition supporting multiple modalities. A pre-print can be found on [arxiv](https://arxiv.org/pdf/2004.11085.pdf).

## Video Abstract


[![SL-DML Overview](images/sl-dml_video_preview.png)](https://userpages.uni-koblenz.de/~raphael/videos/sl-dml.mp4)

[Video](https://userpages.uni-koblenz.de/~raphael/videos/sl-dml.mp4)

## Requirements

* `pip install -r requirements.txt`
*  SL-DML is based on the [pytorch-metric-learning](https://github.com/KevinMusgrave/pytorch-metric-learning) library

## Precalculated Representations

We provide precalculated representations for all conducted experiment splits:

* [NTU RGB+D 120 One-Shot-TODO](https://agas.uni-koblenz.de/datasets/sl-dml/ntu120_one_shot.zip)
* [UTD-MHAD](https://agas.uni-koblenz.de/datasets/sl-dml/utdmhad_one_shot.zip)
* [Simitate](https://agas.uni-koblenz.de/datasets/sl-dml/simitate_one_shot.zip) 

## Training

Download the representations from aboce i.e. 

`wget https://agas.uni-koblenz.de/datasets/sl-dml/ntu120_one_shot.zip`

Then extract the files into a folder that the environment variable `$DATASET_FOLDER` points to.

```
export DATASET_FOLDER=~/datasets/
unzip ntu120_one_shot.zip -d $DATASET_FOLDER
```

Training for the NTU 120 one-shot action recognition experiments can be executed like:

`python train.py dataset=ntu_swap_axis -m`

Note, this also requires the environment variable `$DATASET_FOLDER` to be existing and the respecitve dataset to be extracted there.
