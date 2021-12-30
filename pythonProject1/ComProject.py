from matplotlib import pyplot as plt
import numpy as np

t=np.arange(0,1,0.0001)
sig=np.sin(4*t)-2*np.sin(7*t-0.01)+1.5*np.sin(15*t+0.05)
plt.subplot(411)
plt.plot(t,sig)

carrier=np.sin(2*np.pi*100*t) # 반송파
plt.subplot(412)
plt.plot(t,carrier)

am_sig=sig*carrier # 송신신호 , AM신호 = 신호 * 반송파
plt.subplot(413)
plt.plot(t,am_sig)

dem_am=am_sig*carrier # 원래신호 = am * 반송파
plt.subplot(414)
plt.plot(t,dem_am)

plt.show()







