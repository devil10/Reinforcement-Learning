import gym
import matplotlib
import numpy as np
from collections import defaultdict
from blackjack import BlackjackEnv
import plot
matplotlib.style.use('ggplot')
env  = BlackjackEnv()
def mc_prediction(policy ,env,num_episodes,df = 1):
    rs = defaultdict(float)
    rc = defaultdict(float)
    V = defaultdict(float)
    for j in range(num_episodes):
        state = env.reset()
        vi = defaultdict()
        count = 0
        for t in range(100):
            vi[count]=state
            count=count+1
            rc[state] = rc[state]+1
            a = policy(state)
            state,reward,done,_=env.step(a)
            if done:
                for i in range(count) :
                    rs[vi[i]] = rs[vi[i]] +(reward-rs[vi[i]])/rc[vi[i]]
            	break
    V = rs
    return V
def sample_policy(observation):
    score,dealer_score,usableace = observation
    if score>=20:
        return 0
    else :
        return 1
v= mc_prediction(sample_policy,env,num_episodes=10000)
v2 = mc_prediction(sample_policy,env,num_episodes=500000)
plot.plot_value_function(v,title="10,000")
plot.plot_value_function(v2,title="500,000")
        
