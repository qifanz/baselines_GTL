#!/bin/sh

trap exit SIGINT;

for tentative in {1..10}
do
   python ./experiments/train_cartpole.py --prioritized_replay=True --tentative=$tentative
done
