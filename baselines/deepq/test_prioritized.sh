#!/bin/bash

trap exit SIGINT;

for tentative in {1..5}
do
   python ./experiments/train_mountaincar.py --prioritized_replay=True --tentative=$tentative --experiment=0
   python ./experiments/train_mountaincar.py --prioritized_replay=False --tentative=$tentative --experiment=0
done
