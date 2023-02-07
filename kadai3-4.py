import numpy as np
import matplotlib.pyplot as plt

example=[2.168,2.724,3.673]
xmin=-4.0
xmax=4.0
x=np.arange(xmin,xmax,0.01)
n=0
emin=1.0
o=2.0
plt.figure(figsize=(6.4*len(example),4.8))

for a in [a*0.001 for a in range(2000,4000,1)]:
    da=np.log(a)
    if (da-1)**2<emin:
        emin=(da-1)**2
        o=a
    if n>=len(example):
        continue
    if a==example[n]:
        n+=1
        plt.subplot(1,len(example),n)
        plt.plot(x,a**x,'r')
        plt.plot(x,(a**x)*da,'b')
        plt.xlim(-4,4)
        plt.ylim(-1,5)
        plt.text(0,-0.3,"base=%.3f,optimal base=%.3f" %(a,o))
        plt.grid()

plt.show()
