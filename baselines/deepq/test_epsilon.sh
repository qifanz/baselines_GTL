#!/bin/bash

trap exit SIGINT;

for tentative in {1..10}
do
    for iters in 1e-06 1e-05 1e-04 1e-03 1e-02 1e-01 0.5
    do
        python ./experiments/train_cartpole.py --prioritized_replay_eps=$eps --prioritized_replay=True --tentative=$tentative
    
done
done
