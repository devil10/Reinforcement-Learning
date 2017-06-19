import numpy as np
import scipy
from qwer import GridworldEnv
env = GridworldEnv()
def value_iteration(env,theta = 0.0001,df=1.0):
    V = np.zeros(env.nS)
    policy = np.zeros([env.nS,env.nA])
    while True :
        delta = 0
        vdummy[s] = np.zeros(env.nS)
        for s in range(env.nS):
            max= -1000
            for a in range(env.nA):
                for prob, nextstate ,reward ,done in env.P[s][a]:
                    if V[nextstate]>=max:
                        max=V[nextstate]
                        r = reward
            vdummy[s]=r +max*df
            delta = max(delta,np.abs(vdummy[s]-V[s]))
        V =vdummy
        if delta <theta:
            break
    while True :
        for s in range(env.nS) :
            max = -1000
            for a in range(env.nA):
                for prob,nextstate,reward,done in env.P[s][a] :
                    if V[nextstate]>=max :
                        max = V[nextstate]
            count = 0
            for a in range(env.nA) :
                for prob,nextstate,reward,done in env.P[s][a] :
                    if V[nextstate]==max :
                        policy[s][a] = 1
                        count = count + 1
                    else :
                        policy[s][a] = 0
            for a in range(env.nA) :
                policy[s][a] =policy[s][a]/count
        break
    return policy ,V
policy,v = value_iteration(env)
#print np.reshape(np.argmax(policy,axis = 1),env.shape)
print v.reshape(env.shape)
print policy
