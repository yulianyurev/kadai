import numpy as np
import matplotlib.pyplot as plt

xmin=-2.0
xmax=2.0
x=np.arange(xmin,xmax,0.01)

plt.plot(x,x,label='x')
plt.plot(x,x**2,label='x^2')
plt.plot(x,x**3,label='x^3')
plt.legend(loc='lower left')

plt.grid()
plt.show()