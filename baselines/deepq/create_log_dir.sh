#!/bin/sh

trap exit SIGINT;

mkdir 'log'
chmod 777 'log'

#for tentative in 1 2 3 4 5 6 7 8
#do
#    for eps in 0.01 0.04 0.07 0.1 0.15 0.2 0.25
#    do
#        for fraction in 0.05 0.1 0.15 0.2 0.25 0.3 0.35
#        do
#            target="./log/$eps"\_"$fraction"\_"noise/$tentative"
#            echo $target
#            mkdir -p $target
#            chmod 777 $target
#        done
#    done
#done


for tentative in 4 5 6
do
    for eps in 0.04 0.07 0.1 0.15 0.2 0.25
    do
        for fraction in 0.04 0.07 0.1 0.15 0.2 0.25
        do
            for noise in True False
            do
                target="./log/mountaincar/$eps/$fraction/$noise/$tentative"
                echo $target
                mkdir -p $target
                chmod 777 $target
            done
        done
    done
done
