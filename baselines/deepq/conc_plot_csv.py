import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import os
from math import floor
from os import listdir
import numpy as np

a=100000
b=1000
for num_exp in range(1,9):
    list_dirs=os.walk('./log/'+str(num_exp))
    for root, dirs, files in list_dirs:
        for d in dirs:
            print(d)
            print(a//b)
            steps=np.linspace(0,a,a//b)
            steps_counts = [0]*(a//b)
            mean_reward=[0]*(a//b)
            filenames = listdir(os.path.join(root,d))
            csvs = [ filename for filename in filenames if filename.endswith( ".csv" ) ]
            for csv in csvs:
               log = [l.split("\n")[0].split(",") for l in open(os.path.join(root,d,csv)).readlines()]
               count=0
               print(len(mean_reward))
               for i in log[0]:
                  if i == 'mean 100 episode reward':
                    index_mean=count
                  elif i=="steps":
                    index_steps=count
                  count=count+1
               print('index mean = ' + str(index_mean))
               print('index steps = ' + str(index_steps))
               log = log[1:]  # ignore the first line which is a string comment
               # colum order q_max,q_min,episodes,mean 100 episode reward,steps,% time spent exploring
               log = np.array(log)
               #print(len(log))
               temp_steps = log[:, index_steps].astype(np.float32)
               #print(len(temp_steps))
               mean_rew_100 = log[:, index_mean].astype(np.float32)

               for t in range(0,len(mean_rew_100)):
                  t_on_b=floor((temp_steps[t] // b))
                  #print(t_on_b)
                  #print(mean_rew_100[t])

                  mean_reward[t_on_b]+=mean_rew_100[t]
                  steps_counts[t_on_b]+=1
            for st in range(0,len(steps)):
                if(steps_counts[st]!=0):
                   mean_reward[st]=(mean_reward[st]/steps_counts[st])

            plt.figure()
            plt.ylabel('Mean rew 100')
            plt.xlabel('Episode')
            plt.title('DQN - Mean reward for the least 100 episodes on 5 episodes')
            #print((steps))
            #print((mean_reward))
            plt.axis([0, np.max(steps), 0, np.max(mean_reward)])
            plt.scatter(steps, mean_reward)
            plt.savefig(os.path.join(root, d +'_dqn.png'))