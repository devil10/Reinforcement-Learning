import numpy as np
import scipy
from qwer import GridworldEnv
env = GridworldEnv()
def policy_eval(policy,env,df=1,theta=0.00001):
    V= np.zeros(env.nS)
    while True:
    	delta = 0
        for s in range(env.nS):
            v = 0
            for a,actionp in enumerate(policy[s]):
                for prob,nextstate,reward,done in env.P[s][a]:
                    v= v+ actionp*prob*(reward +df*V[nextstate] )


            delta = max(delta,np.abs(V[s]-v))
            V[s]= v
        if delta<theta :
            break;
    return np.array(V)
def polic_improvement(env,policyeval=policy_eval,df = 1):
    policy = np.ones([env.nS,env.nA])/env.nA
    v= policyeval(policy,env)
    while True:
        policynew = np.zeros([env.nS,env.nA])
        for s in range(env.nS):
            max=-10000
            count = 0;
            for a,ap in enumerate(policy[s]):
                for prob,nextstate,reward,done in env.P[s][a]:
                    if df*v[nextstate]>=max:
                        max=df*v[nextstate]
            for a,ap in enumerate(policy[s]):
                for prob,nextstate,reward,done in env.P[s][a]:
                    if df*v[nextstate] == max:
                        policynew[s][a]=1
                        count = count+1
                    else :
                        policynew[s][a]=0
            for a in range(env.nA):
                policynew[s][a]=policynew[s][a]/count
        if np.array_equal(policy,policynew):
            break
        else :
            policy = policynew
            v = policyeval(policy,env)
            #print v.reshape(env.shape)
    return policy , v
policy,v=polic_improvement(env)
print v.reshape(env.shape)
print policy            
