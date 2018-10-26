#!/bin/sh

trap exit SIGINT;

for eps in 0.04 0.07 0.1 0.15 0.2 0.25
do
    for fraction in 0.04 0.07 0.1 0.15 0.2 0.25
    do

            for tentative in 6
            do
                python ./experiments/train_mountaincar.py --exploration_final_eps=$eps --exploration_fraction=$fraction --tentative=$tentative
                python ./experiments/train_mountaincar.py --exploration_final_eps=$eps --exploration_fraction=$fraction --tentative=$tentative --param_noise=True

            done
    done
done