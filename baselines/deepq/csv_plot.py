import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import os
import numpy as np

mean_results = np.zeros((36,4))

list_dirs=os.walk('./log')
for root, dirs, files in list_dirs:
    path = 0
    for d in dirs:
        depth = len(os.path.join(root,d).split(os.path.sep))
        root_depth = len('./log'.split(os.path.sep))
        
        if depth == root_depth+1:
            mean_max_rew = np.zeros((8,2))#Associate max_rew from each tentative to its step
            lngs =str(d).split("_")[0]
            buffs = str(d).split("_")[1]
            steps = []
            mean_rew_100 = []

            for tentative in range(1,9,1):
                log = [l.split("\n")[0].split(",") for l in open(os.path.join(root, d, str(tentative), 'progress.csv')).readlines()]
                print("opened "+str(os.path.join(root, d, str(tentative), 'progress.csv')))
                count=0
                for i in log[0]:
                    if i == 'mean 100 episode reward':
                        index_mean=count
                    elif i=="steps":
                        index_steps=count
                    count=count+1
                
                log = log[1:]  # ignore the first line which is a string comment
                
                log = np.array(log)
                
                steps = log[:, index_steps].astype(np.float32)
                mean_rew_100 = log[:, index_mean].astype(np.float32)

                tmp_steps = steps
                tmp_mean = mean_rew_100

                steps = (steps + tmp_steps)/2
                mean_rew_100 = mean_rew_100 + tmp_mean
                
                max_rew = 0 #to retrieve the max reward
                
                for j in range(len(mean_rew_100)):
                    if max_rew < mean_rew_100[j]:
                        max_rew = mean_rew_100[j]
                        index = j
                
                
                mean_max_rew[tentative-1][0] = max_rew
                mean_max_rew[tentative-1][1] = index
            
            #stores the mean of max_rew and steps from the 8 tentatives
            
            mean_results[path][0] = np.mean(mean_max_rew[:][0])# mean of the 8 max rewards
            mean_results[path][1] = np.mean(mean_max_rew[:][1])# mean of the 8 steps related to max_rew
            mean_results[path][2] = str(d).split("_")[0]# path leargningStarts
            mean_results[path][3] = str(d).split("_")[1]#path bufferSize

            
            print(mean_results)
            
            path +=1


for lngs in (100, 500, 800, 1000, 1200, 1500):
    buffer_size = [25000, 35000, 50000, 65000, 75000, 100000]
    meanB = []

    for k in range(mean_results.shape[0]):
        if lngs == mean_results[k][2]:
            meanB.append(mean_results[k][0])
            
    plt.figure()
    plt.ylabel('Mean rew 100')
    plt.xlabel('Buffer_size')
    plt.title('Learning_starts = '+str(lngs))
    plt.scatter(buffer_size,meanB)
    plt.savefig(os.path.join('./log','lngs='+str(lngs)+'.png'))
    plt.close()



for buffs in (25000, 35000, 50000, 65000, 75000, 100000):
    learning_starts = [100, 500, 800, 1000, 1200, 1500]
    meanL = []

    for k in range(mean_results.shape[0]):
        if buffs == mean_results[k][3]:
            meanL.append(mean_results[k][0])
            
    plt.figure()
    plt.ylabel('Mean rew 100')
    plt.xlabel('Learning_starts')
    plt.title('Buffer_size = '+str(buffs))
    plt.scatter(learning_starts,meanL)
    plt.savefig(os.path.join('./log','buffs='+str(buffs)+'.png'))
    plt.close()


