# SL-DML: Signal level deep metric learning for multimodal action recognition

![SL-DML Overview](images/example.png)

This repository contains the code for SL-DML, a metric learning approach for one-shot action recognition supporting multiple modalities.

## Video Abstract

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

Training for the NTU 120 one-shot action recognition experiments can be executed like:

`python train.py dataset=ntu_swap_axis -m`

