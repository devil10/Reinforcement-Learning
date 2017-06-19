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
	#print V
    return np.array(V)
policy = np.ones([env.nS,env.nA])/env.nA
v= policy_eval(policy,env)
print v
	
            
