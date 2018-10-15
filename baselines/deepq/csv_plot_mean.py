import matplotlib as mpl
#mpl.use('Agg')
import matplotlib.pyplot as plt
import os
import numpy as np
TENTATIVES=8

# Read the eps_fraction_mean.csv which contains different combinations of eps and fraction
log = [l.split("\n")[0].split(",") for l in open(os.path.join('./log', 'eps_fraction_mean.csv')).readlines()]
log = log[1:]  # ignore the first line which is a string comment
log = np.array(log)
# Add one dimension to the array (which will contain the max_reward)
log = np.hstack((log, np.zeros((log.shape[0], 3), dtype=np.float32)))

# For each row (eps,fraction), read the corresponding csv file and add the max reward to the log array
# TODO: replace max reward by mean max reward of different tentatives
for i in range (0,len(log),1):
    max_reward=[]
    for tentative in range(1,TENTATIVES+1,1):
        # Dir name is eps_fraction/tentative
        dir = log[i][0]+'_'+log[i][1]
        log2 = [l.split("\n")[0].split(",") for l in open(os.path.join('./log', dir, str(tentative),'progress.csv')).readlines()]
        count = 0
        # Look for the index of mean 100 episodes reward
        for j in log2[0]:
            if j == 'mean 100 episode reward':
                index_reward = count
            count=count+1

        # Look for the max mean 100 episodes reward
        log2 = log2[1:]
        log2 = np.array(log2)
        mean_rew_100 = log2[:, index_reward].astype(np.float32)
        max_reward.append(np.max(mean_rew_100))
    max_reward=np.array(max_reward).astype(np.float32)
    log[i][2]=np.mean(max_reward)
    log[i][3]=np.std(max_reward)
print(log)


# For each eps, plot the evolution of reward according to fraction
plt.figure()
plt.ylabel('mean max_reward')
plt.xlabel('fraction')
plt.title('Evolution of mean of max_rewards according to fraction')
plt.axis([0, 0.35, 50, 200])
# TODO: iterate the values contained in csv instead of manual inputs
for eps in (0.01, 0.04, 0.07, 0.1, 0.15, 0.2, 0.25):
    fraction=[]
    mean=[]
    for i in range (0,len(log),1):
        if abs(log[i][0].astype(np.float32) - eps)<0.001:
            fraction.append(log[i][1].astype(np.float32))
            mean.append(log[i][2].astype(np.float32))
    xs, ys = zip(*sorted(zip(fraction, mean)))
    plt.plot(xs, ys, label='eps='+str(eps))
plt.legend(loc='best')
plt.savefig(os.path.join('./log', 'mean_max_reward_eps.png'))
plt.show()

plt.figure()
plt.ylabel('std max_reward')
plt.xlabel('fraction')
plt.title('Evolution of std of max_rewards according to fraction')
#plt.axis([0, 0.35, 50, 200])
# TODO: iterate the values contained in csv instead of manual inputs
for eps in (0.01, 0.04, 0.07, 0.1, 0.15, 0.2, 0.25):
    fraction=[]
    std=[]
    for i in range (0,len(log),1):
        if abs(log[i][0].astype(np.float32) - eps)<0.001:
            fraction.append(log[i][1].astype(np.float32))
            std.append(log[i][3].astype(np.float32))
    xs, ys = zip(*sorted(zip(fraction, std)))
    plt.plot(xs, ys, label='eps='+str(eps))
plt.legend(loc='best')
plt.savefig(os.path.join('./log', 'std_max_reward_eps.png'))
plt.show()


plt.figure()
plt.ylabel('mean max_reward')
plt.xlabel('epsilon')
plt.title('Evolution of mean of max_rewards according to final eps')
plt.axis([0, 0.25, 50, 200])
# For each fraction, plot the evolution of reward according to eps
# TODO: iterate the values contained in csv instead of manual inputs
for fraction in (0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35):
    eps=[]
    mean=[]
    for i in range (0,len(log),1):
        if abs(log[i][1].astype(np.float32) - fraction)<0.001:
            eps.append(log[i][0].astype(np.float32))
            mean.append(log[i][2].astype(np.float32))

    xs, ys = zip(*sorted(zip(eps, mean)))
    plt.plot(xs, ys, label='fraction='+str(fraction))
plt.legend(loc='best')
plt.savefig(os.path.join('./log', 'mean_max_reward_fraction.png'))
plt.show()


plt.figure()
plt.ylabel('std max_reward')
plt.xlabel('epsilon')
plt.title('Std of mean of max_rewards according to final eps')
# For each fraction, plot the evolution of reward according to eps
# TODO: iterate the values contained in csv instead of manual inputs
for fraction in (0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35):
    eps=[]
    std=[]
    for i in range (0,len(log),1):
        if abs(log[i][1].astype(np.float32) - fraction)<0.001:
            eps.append(log[i][0].astype(np.float32))
            std.append(log[i][3].astype(np.float32))

    xs, ys = zip(*sorted(zip(eps, std)))
    plt.plot(xs, ys, label=str(fraction))
plt.legend(loc='best')
plt.savefig(os.path.join('./log', 'std_max_reward_fraction.png'))
plt.show()



