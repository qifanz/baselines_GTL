#!/bin/bash

trap exit SIGINT;

for tentative in {1..10}
do
    for iters in 1 2 3 4 5
    do
        python ./experiments/train_cartpole.py --prioritized_replay_beta_iters=(100000/$iters) --prioritized_replay=True --tentative=$tentative
    
done
done
