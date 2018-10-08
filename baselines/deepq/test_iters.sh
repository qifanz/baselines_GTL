#!/bin/bash

trap exit SIGINT;

for tentative in {1..10}
do
    for iters in 100000 50000 10000 5000
    do
        python ./experiments/train_cartpole.py --prioritized_replay_beta_iters=$iters --prioritized_replay=True --tentative=$tentative --experiment=4

done
done
