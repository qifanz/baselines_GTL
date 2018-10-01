#!/bin/sh

trap exit SIGINT;

for tentative in 1 2
do
   target="./log/True_0.4/$tentative"
            echo $target
            mkdir -p $target
            chmod 777 $target
    python ./experiments/train_cartpole.py prioritized_replay=True --tentative=$tentative
done
