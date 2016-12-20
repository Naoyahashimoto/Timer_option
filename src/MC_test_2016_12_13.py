import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import uniform
import scipy.integrate
N = 1000
a,b = 0,1
h = lambda x: (np.cos(50 * x) + np.sin(20*x)) **2

I = scipy.integrate.quad(h,a,b)[0]
print("scipy.integrate:"), I

x = h(uniform(loc=a,scale=b-a).rvs(size=N))
estint = np.cumsum(x)  / np.arange(1,N+1)

esterr = np.sqrt(np.cumsum((x-estint)**2))/ np.arange(1,N+1)

plt.plot(estint,color='red', linewidth=2)
plt.plot(estint + 2*esterr,color='gray')
plt.plot(estint - 2*esterr,color='gray')
plt.ylim((0,2))
plt.show()