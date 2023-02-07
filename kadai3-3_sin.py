import numpy as np
import matplotlib.pyplot as plt

tmin=-2.0*np.pi
tmax=2.0*np.pi
t=np.arange(tmin,tmax,0.01)

def sintay(n,t):
    ret=0.0
    fac=-1.0
    for i in range(1,n):
        fac*=i
        if(i%2==1):
            fac*=-1
            ret+=(t**i)/fac
    return ret

plt.plot(t,sintay(10,t),label='sin(t)')
plt.legend(loc='lower left')

plt.ylim(-2,2)
plt.grid()
plt.show()