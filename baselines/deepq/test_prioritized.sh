#!/bin/sh

trap exit SIGINT;

for tentative in 1 2
do
   target="./log/True_0.6_0.4_None_1e-6"
            echo $target
            mkdir -p $target
            chmod 777 $target
    python ./experiments/train_cartpole.py --prioritized_replay=True --tentative=$tentative
done
