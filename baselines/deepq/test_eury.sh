#!/bin/sh

trap exit SIGINT;

for tentative in 1
do
    # for learning_starts in 100 500 800 1000 1200 1500
    for lngs in 800 1000
    do
      for buffs in 25000 35000 50000 75000 100000
      do
        #python ./experiments/train_cartpole.py --learning_starts=$lngs --buffer_size=$buffs --tentative=$tentative
        python ./experiments/train_mountaincar.py --learning_starts=$lngs --buffer_size=$buffs --tentative=$tentative

      done
    done
done
