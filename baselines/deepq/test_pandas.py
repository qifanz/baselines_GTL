import pandas as pd
import os
import matplotlib.pyplot as plt


dfs=[]
for eps in [0.04, 0.07, 0.1, 0.15, 0.2, 0.25]:
    for fraction in  [0.04, 0.07, 0.1, 0.15, 0.2, 0.25]:
        for noise in [0,1]:
            for tentative in [1,2,3,4,5,6]:
                if noise==1:
                    noise_str='True'
                else:
                    noise_str='False'
                dir = str(eps)+'/'+str(fraction)+'/'+noise_str+'/'+str(tentative)
                file_path=os.path.join('./log/mountaincar', dir,'progress.csv')
                df=pd.read_csv(file_path,header=0)
                df=df.assign(eps=eps)
                df=df.assign(fraction=fraction)
                df=df.assign(noise=noise)
                df=df.assign(tentative=tentative)
                dfs.append(df)



data=pd.concat(dfs,sort=False,ignore_index=True)
data=data.drop('% time spent exploring',1)
data=data.drop('episodes',1)
'''res=data.groupby(['eps', 'fraction','step','noise','tentative'],as_index=False)[['mean 100 episode reward']].max()
res=res.groupby(['eps', 'fraction','noise'],as_index=False)[['mean 100 episode reward']].median()
res=res.groupby(['eps','noise'],as_index=False)[['mean 100 episode reward']].median()'''
steps=range(0,1000001,2000)
for eps in [0.04, 0.07, 0.1, 0.15, 0.2, 0.25]:
    for fraction in  [0.04, 0.07, 0.1, 0.15, 0.2, 0.25]:
        for noise in [0,1]:
            data_eps=data.where(data.get('eps')==eps)
            data_fraction=data_eps.where(data_eps.get('fraction')==fraction)
            data_noise=data_fraction.where(data_fraction.get('noise')==noise)

            data_noise=data_noise.dropna()
            step_reward_list=[0] * (501)

            for tentative in [1,2,3,4,5,6]:
                data_sub=data_noise.where(data_noise.get('tentative')==tentative)
                data_sub = data_sub.dropna()


                for i,step in enumerate(steps):
                    # print(data_sub.get('steps'))
                    reward_step=data_sub.where(data_sub.get('steps')>step)
                    reward_step=reward_step.where(reward_step.get('steps')<step+2000)
                    reward_step=reward_step.dropna()
                    for tmp in reward_step.get('mean 100 episode reward'):
                        temp=tmp

                    step_reward_list[i]+=temp

            step_reward_list = [x / 6 for x in step_reward_list]


            plt.figure()
            plt.title('eps='+str(eps)+' fraction='+str(fraction)+' noise='+str(noise))
            plt.plot(steps,step_reward_list)
            plt.savefig('eps='+str(eps)+' fraction='+str(fraction)+' noise='+str(noise)+'.png')
            plt.show()
            plt.close()
