#!/bin/sh

trap exit SIGINT;

mkdir 'log'
chmod 777 'log'


#for tentative in 1 2 3 4 5 6 7 8
#do
    # for learning_starts in 100 500 800 1000 1200 1500
   # for lngs in 100 500 800 1000 1200 1500
   # do
        #for buffer_size in 25000 35000 50000 65000 75000 100000
       # for buffs in 25000 35000 50000 65000 75000 100000
       # do
        #    target="./log/$lngs"\_"$buffs/$tentative"
         #   echo $target
          #  mkdir -p $target
           # chmod 777 $target
       # done
   # done
#done


for tentative in 1 2
do 
  for learning_starts in 100 500 800 1000 1200 1500
  do
    for buffer_size in 25000 35000 50000 65000 75000 100000
    do
      target="./log/mountaincar/$learning_starts"\_"$buffer_size/$tentative"
      mkdir -p $target
      chmod 777 $target
    done
  done
done
