from matplotlib import pyplot as plt
import numpy as np
from scipy.stats import norm
mu=0
sigma=1
sample=10000000
s=np.random.normal(mu,sigma,sample)

(X,Y,Z) = plt.hist(s,100,density=True)

plt.plot(Y,1/(sigma*np.sqrt(2*np.pi))*np.exp(-((Y-mu)**2)/(2*sigma**2)))
print((1/(sigma*np.sqrt(2*np.pi))*np.exp(-((5-mu)**2)/(2*sigma**2))))
print(norm.cdf(2))
print(np.sum(s<2)/sample)

plt.show()

