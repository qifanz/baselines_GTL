#!/bin/bash

trap exit SIGINT;

for tentative in {1..5}
do
    for eps in 0.000001 0.00001 0.0001 0.001 0.01 0.1 0.5
    do
        python ./experiments/train_mountaincar.py --prioritized_replay_eps=$eps --prioritized_replay=True --tentative=$tentative -experiment=3

done
done
