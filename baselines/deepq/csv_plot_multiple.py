import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import os
import numpy as np

plt.figure()
plt.ylabel('Mean rew 100')
plt.xlabel('Steps')
plt.title('Evolution of rewards with fraction=0.05')
plt.axis([0, 100000, 0, 200])
list_dirs=os.walk('./log')
for eps in (0.01, 0.04, 0.07, 0.1, 0.15, 0.2, 0.25):
    for fraction in (0.05,):
        log = [l.split("\n")[0].split(",") for l in open(os.path.join('./log', str(eps)+'_'+str(fraction), '1', 'progress.csv')).readlines()]
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
        # colum order q_max,q_min,episodes,mean 100 episode reward,steps,% time spent exploring`
        log = np.array(log)
        # print(len(log))
        steps = log[:, index_steps].astype(np.float32)
        mean_rew_100 = log[:, index_mean].astype(np.float32)
        plt.plot(steps, mean_rew_100,label='eps'+str(eps))
plt.legend(loc='best')
plt.savefig(os.path.join('./log','multiple_eps.png'))
plt.close()



plt.figure()
plt.ylabel('Mean rew 100')
plt.xlabel('Steps')
plt.title('Evolution of rewars with eps=0.01')
plt.axis([0, 100000, 0, 200])
list_dirs=os.walk('./log')
for eps in (0.01,):
    for fraction in (0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35):

        log = [l.split("\n")[0].split(",") for l in open(os.path.join('./log', str(eps)+'_'+str(fraction), '1', 'progress.csv')).readlines()]
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
        plt.plot(steps, mean_rew_100,label='fraction'+str(fraction))
plt.legend(loc='best')
plt.savefig(os.path.join('./log','multiple_fraction.png'))
plt.close()

