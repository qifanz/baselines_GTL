#!/bin/bash

trap exit SIGINT;

for tentative in {1..10}
do
    for beta in 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9
    do
        python ./experiments/train_cartpole.py --prioritized_replay_beta_iters=$beta --prioritized_replay=True --tentative=$tentative
    
done
done
