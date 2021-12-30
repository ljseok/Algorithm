from matplotlib import pyplot as plt
import numpy as np

step = 0.002
t=np.arange(step,1+step,step)
fs= 20
sig = np.sin(2*np.pi *3*t)+np.cos(2*np.pi*7*t)-np.sin(2*np.pi*10*t)

plt.subplot(811)
plt.plot(t,sig)

carr=np.cos(2*np.pi*fs*2*t)

am = sig * carr
plt.subplot(812)
plt.plot(am)

ori = am * carr
plt.subplot(813)
plt.plot(t,ori)

freq_sig = np.abs(np.fft.fftshift(np.fft.fft(sig)))
plt.subplot(814)
plt.plot(t,freq_sig)

fr_am = np.abs(np.fft.fftshift(np.fft.fft(am)))
plt.subplot(815)
plt.plot(t,fr_am)

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

freq_fil_sig = np.abs(np.fft.fftshift(np.fft.fft(fil_sig))) # 필터를 통과한 주파수 영역 에서의 신호

plt.subplot(818)
plt.plot(t,freq_fil_sig)



plt.show()



