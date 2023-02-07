import numpy as np
import matplotlib.pyplot as plt

xmin=-2.0*np.pi
xmax=2.0*np.pi
x=np.arange(xmin,xmax,0.01)

plt.xticks([-2*np.pi,-np.pi,0,np.pi,2*np.pi],['-2π','-π',0,'π','2π'])

plt.xlabel('frequency',rotation=0)
plt.ylabel('amplitude',rotation=90)

def noko(n,t):
    ret=0.0
    for i in range(n):
        ret+=np.sin((i+1)*2*t)/(i+1)
    return ret

y=np.pi/2-noko(99,x)

plt.plot(x,y,label=r'$\frac{π}{2}$-sin(2t)-$\frac{1}{2}$sin(4t)-$\frac{1}{3}$sin(6t)-...-$\frac{1}{99}$sin(198t)')

plt.legend(loc='lower left')

plt.grid()
plt.show()
