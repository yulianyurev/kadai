import numpy as np
import matplotlib.pyplot as plt

xmin=-4.0
xmax=4.0
x=np.arange(xmin,xmax,0.01)

plt.plot(x,1**x,label='1^x')
plt.plot(x,2**x,label='2^x')
plt.plot(x,3**x,label='3^x')
plt.legend(loc='lower left')

plt.xlim(-4,4)
plt.ylim(-1,5)

plt.grid()
plt.show()