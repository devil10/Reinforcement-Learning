import gym
import matplotlib
import numpy as np
from collections import defaultdict
from blackjack import BlackjackEnv
import plot
matplotlib.style.use('ggplot')
env=BlackjackEnv()
def mc_control(env ,num_episodes,df=1):
    Qcount = defaultdict(lambda: np.zeros(env.action_space.n))
    Q=defaultdict(lambda: np.zeros(env.action_space.n))
    for i in range(num_episodes):
        state = env.reset()
        vi =defaultdict()
        count =0
        ai =defaultdict(float)
        for t in range(100):
            vi[count]=state
            count = count+1
            a = np.ones(2, dtype=float) / 2
            action = np.random.choice(np.arange(len(a)),p=a)
            ai[state]=action
            state,reward,done,_=env.step(action)
            if done:
                W=1
                for j in range(count):
                    Qcount[vi[count-1-j]][ai[vi[count-1-j]]] = Qcount[vi[count-1-j]][ai[vi[count-1-j]]]+W
                    Q[vi[count-1-j]][ai[vi[count-1-j]]]+=W*(reward-Q[vi[count-1-j]][ai[vi[count-1-j]]])/Qcount[vi[count-1-j]][ai[vi[count-1-j]]]
                    W =W*2
                    b =np.argmax(Q[vi[count-1-j]])
                    if b!=ai[vi[count-1-j]]:
                        break
                break        
    return Q
Q = mc_control(env,num_episodes=500000)
V = defaultdict(float)
for state, action_values in Q.items():
    action_value = np.max(action_values)
    V[state] = action_value
plot.plot_value_function(V, title="Optimal Value Function")
