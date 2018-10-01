import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import os
import numpy as np

list_dirs=os.walk('./log')
for root, dirs, files in list_dirs:
    for d in dirs:
        depth = len(os.path.join(root,d).split(os.path.sep))
        root_depth = len('./log'.split(os.path.sep))
        if depth == root_depth+1:
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
                # print('index mean = ' + str(index_mean))
                # print('index steps = ' + str(index_steps))
                log = log[1:]  # ignore the first line which is a string comment
                # colum order q_max,q_min,episodes,mean 100 episode reward,steps,% time spent exploring
                log = np.array(log)
                # print(len(log))
                steps = log[:, index_steps].astype(np.float32)
                mean_rew_100 = log[:, index_mean].astype(np.float32)
                # print(log)

                #print("****************************steps********************************************")

                # print(steps)
                # print(np.max(steps))

                #print("**************************mean***************")
                # print(mean_rew_100)
                # print(np.max(mean_rew_100))

                plt.figure()
                plt.ylabel('Mean rew 100')
                plt.xlabel('Steps')
                plt.title('DQN - Mean reward for the least 100 episodes')
                plt.axis([0, np.max(steps), 0, np.max(mean_rew_100)])
                plt.scatter(steps, mean_rew_100)
                plt.savefig(os.path.join(root, d, str(tentative),'Evolution mean reward - steps.png'))
                plt.close()


