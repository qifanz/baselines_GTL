#!/bin/sh

trap exit SIGINT;

for eps in 0.04 0.07 0.1 0.15 0.2 0.25
do
    for fraction in 0.04 0.07 0.1 0.15 0.2 0.25
    do
        for noise in True False
        do
            python ./experiments/train_mountaincar.py.py --exploration_final_eps=$eps --exploration_fraction=$fraction --tentative=$tentative --param_noise=$noise
        done
    done
done