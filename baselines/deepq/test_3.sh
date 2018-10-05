#!/bin/sh

trap exit SIGINT;

for tentative in 5 6
do
    # for eps in 0.1 0.15 0.2 0.25
    for eps in 0.01 0.04 0.07 0.1 0.15 0.2 0.25
    do
        #for fraction in 0.05 0.1 0.15 0.2
        for fraction in 0.05 0.1 0.15 0.2 0.25 0.3 0.35
        do
            python ./experiments/train_cartpole.py --exploration_final_eps=$eps --exploration_fraction=$fraction --tentative=$tentative --param_noise=true
        done
    done
done