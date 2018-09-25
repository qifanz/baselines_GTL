import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import os
import numpy as np


log = [l.split("\n")[0].split(",") for l in open(os.path.join('./log', 'eps_fraction_mean.csv')).readlines()]
log = log[1:]  # ignore the first line which is a string comment
log = np.array(log)

# colum order q_max,q_min,episodes,mean 100 episode reward,steps,% time spent exploring
for eps in (0.01, 0.04, 0.07, 0.1, 0.15, 0.2, 0.25):
    fraction=[]
    mean=[]
    for i in range (0,len(log),1):
        if abs(log[i][0].astype(np.float32) - eps)<0.001:
            fraction.append(log[i][1].astype(np.float32))
            mean.append(log[i][2].astype(np.float32))

    plt.figure()
    plt.ylabel('Mean rew 100')
    plt.xlabel('fraction')
    plt.title('Final epsilon = '+str(eps))
    plt.axis([0, np.max(fraction), 0, np.max(mean)])
    plt.scatter(fraction, mean)
    plt.savefig(os.path.join('./log', 'eps='+str(eps)+'.png'))

for fraction in (0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35):
    eps=[]
    mean=[]
    for i in range (0,len(log),1):
        if abs(log[i][1].astype(np.float32) - fraction)<0.001:
            eps.append(log[i][0].astype(np.float32))
            mean.append(log[i][2].astype(np.float32))
    plt.figure()
    plt.ylabel('Mean rew 100')
    plt.xlabel('epsilon')
    plt.title('Fraction = '+str(fraction))
    plt.axis([0, np.max(eps), 0, np.max(mean)])
    plt.scatter(eps, mean)
    plt.savefig(os.path.join('./log', 'fraction='+str(fraction)+'.png'))