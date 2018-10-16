import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import os
from math import floor
from os import listdir
import numpy as np


for exp in range(1,5):
    list_dirs=os.walk('./log/'+str(exp))

    for root, dirs, files in list_dirs:

        param=['']*len(dirs)

        list_best_rewards=[0]*len(dirs)
        list_steps_best_reward=[0]*len(dirs)
        index=-1
        for d in dirs:
            index+=1
            #print(d)
            best_reward=0
            step_best_reward=0
            filenames = listdir(os.path.join(root,d))
            csvs = [ filename for filename in filenames if filename.endswith( ".csv" ) ]
            for csv in csvs:
               log = [l.split("\n")[0].split(",") for l in open(os.path.join(root,d,csv)).readlines()]
               count=0
               for i in log[0]:
                  if i == 'mean 100 episode reward':
                    index_mean=count
                  elif i=="steps":
                    index_steps=count
                  count=count+1
               #print('index mean = ' + str(index_mean))
               #print('index steps = ' + str(index_steps))
               log = log[1:]  # ignore the first line which is a string comment
               log = np.array(log)
               temp_steps = log[:, index_steps].astype(np.float32)
               #print(len(temp_steps))
               mean_rew_100 = log[:, index_mean].astype(np.float32)
               best_reward+=np.max(mean_rew_100)
               step_best_reward+=temp_steps[np.argmax(mean_rew_100)]
            best_reward=best_reward/len(csvs)
            step_best_reward=step_best_reward/len(csvs)
            list_best_rewards[index]=best_reward
            list_steps_best_reward[index]=step_best_reward
            param[index]=d
        if len(param)>1:
            l0=param[0].split('_')
            l1=param[1].split('_')
            index_param=([x for x in range(len(l1)) if l0[x]!=l1[x]])[0]
            param=([float(param[i].split('_')[index_param]) for i in range(len(param)) ])
            param.sort()
            print(param)

            plt.figure()

            fig, ax1= plt.subplots()
            ax1.plot(param,list_best_rewards,'bo')
            print(list_best_rewards)
            ax1.set_xlabel('param')
            ax1.set_ylabel('average best reward', color='blue')
            ax1.tick_params('y', colors='blue')
            #ax2=ax1.twinx()
            #ax2.plot(param, list_steps_best_reward, 'ro')
            #ax2.set_ylabel('step', color='red')
            #ax2.tick_params('y', colors='red')

            plt.show()

            plt.savefig(os.path.join('./log/'+str(exp)+'_tests'))
            plt.close()
