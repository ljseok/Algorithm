from matplotlib import pyplot as plt
import numpy as np


t=np.arange(0.004,1.004,0.004)
f = 30

sig = np.sin(2*np.pi *3*t)+np.cos(2*np.pi*7*t)-np.sin(2*np.pi*10*t)

plt.subplot(811)
plt.plot(t,sig)

freq_sig = np.abs(np.fft.fftshift(np.fft.fft(sig)))
plt.subplot(812)
plt.plot(t,freq_sig)

carr = np.cos(2*np.pi*f*2*t)

am = carr * sig
plt.subplot(813)
plt.plot(t,am)

fr_am = np.abs(np.fft.fftshift(np.fft.fft(am)))
plt.subplot(814)
plt.plot(t,fr_am)

ori = am * carr
plt.subplot(815)
plt.plot(t,ori)

fr_ori = np.abs(np.fft.fftshift(np.fft.fft(ori)))
plt.subplot(816)
plt.plot(t,fr_ori)


LPF_f = 30
t_ldf=np.arange(-0.5,0.5,0.004)
LPF=[]
for t1 in t_ldf:
    if(t1==0):
       T_LPF=1
    else:
       T_LPF=np.sin(2*np.pi*LPF_f*t1)/(2*np.pi*LPF_f*t1)

    LPF.append(T_LPF)
LPF_sig=np.convolve(ori,LPF,'same')

fil_sig=LPF_sig/np.sum(LPF)*2

plt.subplot(817)
plt.plot(t,fil_sig)

freq_fil_sig = np.abs(np.fft.fftshift(np.fft.fft(fil_sig)))
plt.subplot(818)
plt.plot(t,freq_fil_sig)
plt.show()
