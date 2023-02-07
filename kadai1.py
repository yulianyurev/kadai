import numpy as np
import matplotlib.pyplot as plt

t=np.arange(-np.pi,np.pi,0.01)
plt.figure(figsize=(6.4,24))

x=np.sin(np.pi*t)
plt.subplot(5,1,1)
plt.plot(t,x)

x=np.cos(2*t+np.pi/2)
plt.subplot(5,1,2)
plt.plot(t,x)

x=1-np.sin(t)
plt.subplot(5,1,3)
plt.plot(t,x)

x=np.cos(np.pi*t)
plt.subplot(5,1,4)
plt.plot(t,x)

x=np.sin(2*t+np.pi/2)
plt.subplot(5,1,5)
plt.plot(t,x)

plt.show()