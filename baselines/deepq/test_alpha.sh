#!/bin/bash

trap exit SIGINT;

for tentative in {1..4}
do
    for alpha in 0.0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1.0
    do
        python ./experiments/train_pong.py --prioritized_replay=True --prioritized_replay_alpha=$alpha --tentative=$tentative --experiment=1

done
done
