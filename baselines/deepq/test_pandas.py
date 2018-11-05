import pandas as pd
import os
import matplotlib.pyplot as plt
'''for eps in [0.04, 0.07, 0.1, 0.15, 0.2, 0.25]:
    for fraction in  [0.04, 0.07, 0.1, 0.15, 0.2, 0.25]:
        for noise in [0,1]:
            for tentative in [1,2,3,4,5,6]:
'''
dfs=[]
for eps in [0.04,0.07]:
    for fraction in [0.04]:
        for noise in [0,1]:
            for tentative in [1,2,3]:
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

                plt.figure()
                df.plot(x='steps', y='mean 100 episode reward')
                plt.close()

data=pd.concat(dfs)
res=data.groupby(['eps', 'fraction','noise','tentative'])[['mean 100 episode reward']].max()
print(type(res))
