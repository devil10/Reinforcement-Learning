import gym
import matplotlib
import numpy as np
from collections import defaultdict
from blackjack import BlackjackEnv
import plot
matplotlib.style.use('ggplot')
env = BlackjackEnv()
def mc_control(env,num_episodes,df=1,epsilon=0.1):
    Qcount = defaultdict(lambda: np.zeros(env.action_space.n))
    Q=defaultdict(lambda: np.zeros(env.action_space.n))
    for i in range(num_episodes):
        state=env.reset()
        vi =defaultdict()
        count=0
        ai =defaultdict(float)
        for t in range(100):
            vi[count]=state
            count=count+1
            a=policy(Q,state)
            action =np.random.choice(np.arange(len(a)),p=a)
            ai[state]=action
            Qcount[state][ai[state]]+=1
            state,reward,done,_=env.step(action)
            if done:
                for j in range(count) :
                    Q[vi[j]][ai[vi[j]]]+=(reward-Q[vi[j]][ai[vi[j]]])/Qcount[vi[j]][ai[vi[j]]]
                break
    return Q
def policy(Q,state,epsilon=0.1):
    A=np.zeros(2)
    if Q[state][0]>=Q[state][1]:
        A[0]=1-epsilon/2
        A[1]=1-A[0]
    else :
        A[0]=epsilon/2
        A[1]=1-A[0]
    return A
Q = mc_control(env,num_episodes=500000)
V=defaultdict(float)
#polic=defaultdict(float)
for state,actions in Q.items():
    action_value=np.max(actions)
    V[state] = action_value
	#polic[state] = np.argmax(actions)
plot.plot_value_function(V, title="Optimal Value Function")    
