import gym
import itertools
import matplotlib
import numpy as np
import pandas as pd
from collections import defaultdict
from wind import WindyGridworldEnv
import plot
matplotlib.style.use('ggplot')
env=WindyGridworldEnv()
def sarsa(env,num_episodes,discount_factor=1,alpha=0.5,epsilon=0.1):
     Q = defaultdict(lambda: np.zeros(env.action_space.n))
     stats = plot.EpisodeStats(episode_lengths=np.zeros(num_episodes),episode_rewards=np.zeros(num_episodes))


     for i in range(num_episodes):
         state = env.reset()
         flag =1
         a=gpolicy(Q,epsilon,4,state)
         action=np.random.choice(np.arange(len(a)), p=a)
         while flag==1 :
             state2,rewards,done,_=env.step(action)
             stats.episode_rewards[i]+=rewards
             a2=gpolicy(Q,epsilon,4,state2)
             action2=np.random.choice(np.arange(len(a2)),p=a2)
             Q[state][action]+=alpha*(rewards+Q[state2][action2]-Q[state][action])
             state=state2
             action=action2
             if done:
                 break
         stats.episode_lengths[i]=-1*stats.episode_rewards[i]
     return Q,stats
def gpolicy(Q,epsilon,nA,state):
    A = np.zeros(nA)
    a = np.argmax(Q[state])
    for i in range(nA):
        if i==a:
            A[i]=1-epsilon+epsilon/nA
        else :
            A[i]=epsilon/nA
    return A
Q ,stats = sarsa(env,300)
state = env.reset()
#env.render()
flag=1
count = 0
while flag==1:
    a =np.argmax(Q[state])
    state,a,b,_=env.step(a)
    #env.render()
    count+=1
    if b:
        break
print count
#plot.plot_episode_stats(stats)
