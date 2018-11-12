import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import os
from math import floor
from os import listdir
import numpy as np

list_colors=['b-', 'g-','r-','c-','m-','y-','k-','w-','olive-','orange-','grey-','peru-']
list_exp=['Prioritzed', 'alpha', 'beta', 'iters', 'eps']

for exp in range(0,4):
    list_dirs=os.walk('./log_car/'+str(exp))


    for root, dirs, files in list_dirs:
        print(dirs)
        list_steps_best_reward=[[] for x in range(10)]
        list_best_rewards= [[] for x in range(10)]
        param=['']*len(dirs)


        index=-1
        for d in dirs:
            index+=1
            filenames = listdir(os.path.join(root,d))
            csvs = [ filename for filename in filenames if filename.endswith( ".csv" ) ]
            print('len is '+str(len(csvs)))
            best_reward=[0]*len(csvs)
            step_best_reward=[0]*len(csvs)
            index_csv=-1
            for csv in csvs:
               index_csv+=1
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
               print(np.max(mean_rew_100))
               list_best_rewards[index_csv].append(np.max(mean_rew_100))
               list_steps_best_reward[index_csv].append(temp_steps[np.argmax(mean_rew_100)])
            param[index]=d
        print(len(param))
        if len(param)>1:
            print('here')
            l0=param[0].split('_')
            l1=param[1].split('_')
            index_param=([x for x in range(len(l1)) if l0[x]!=l1[x]])[0]
            param=([float(param[i].split('_')[index_param]) for i in range(len(param)) ])
            param.sort()
            plt.figure()
            for num in range(0, 4):
                print(num)
                if len(list_best_rewards[num])!=0:
                    print(param)
                    print(list_best_rewards[num])
                    print(len(param)==len(list_best_rewards[num]))
                    plt.scatter(param, list_best_rewards[num],marker="o")
            plt.title("Changing param "+list_exp[index_param])
            plt.show()

            plt.savefig(os.path.join('./log_car/'+'all_means' + str(exp)+'_points'))
            print(os.path.join('./log_car/'+'all_means' + str(exp)+'_points'))
            plt.close()
