import numpy as np
import matplotlib.pyplot as plt

tmin=-2.0*np.pi
tmax=2.0*np.pi
t=np.arange(tmin,tmax,0.01)
   
def costay(n,t):
    ret=1.0
    fac=1.0
    for i in range(1,n):
        fac*=i
        if(i%2==0):
            fac*=-1
            ret+=(t**i)/fac
    return ret
    
plt.plot(t,costay(10,t),label='cos(t)')
plt.legend(loc='lower left')

plt.ylim(-2,2)
plt.grid()
plt.show()