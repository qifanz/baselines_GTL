#!/bin/bash

trap exit SIGINT;

for tentative in {1..5}
do
    for iters in 1e02 1e03 1e04 1e05 1e06 1e07 1e08
    do
        python ./experiments/train_mountaincar.py --prioritized_replay_beta_iters=$iters --prioritized_replay=True --tentative=$tentative --experiment=4

done
done
