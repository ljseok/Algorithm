from matplotlib import pyplot as plt
import numpy as np

step = 0.002
t=np.arange(step,1+step,step)
fs=20 # 샘플링 주파수
ts=1/fs
ds=ts/step # 얼마마다 신호를 따내야 하는가
num_samples=np.shape(t)[0]

sig=np.sin(2*np.pi*2*t)-2*np.sin(2*np.pi*5*t+3)
impulse_train=np.zeros(num_samples)
count=0
for i in impulse_train:
    if(count%int(ds))==(int(ds)-1): # ds 간격만큼 0이 아닌 1을 띄워줘라
        impulse_train[count]=1 #ds 간격만큼 1을 만들어 준다
    count+=1
sampled_signal=impulse_train*sig
rect_sig=[0,0,0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0]

plt.subplot(811) # 시간영역 원래신호
plt.plot(t,sig)

plt.subplot(812) # 시간영역 임펄스 주기신호
plt.stem(t,impulse_train)

plt.subplot(813) # 시간영역 원래 신호 *(곱) 임펄스 주기신호 = 임펄스 트레인 신호 (샘플링된 신호 )
plt.stem(t,sampled_signal)

freq_signal=np.abs(np.fft.fftshift(np.fft.fft(sig)))
plt.subplot(814) # 주파수영역 원래신호
plt.plot(t,freq_signal)

freq_sig=np.abs(np.fft.fftshift(np.fft.fft(sampled_signal)))
plt.subplot(815) # 주파수 영역 임펄스 트레인 신호 = 임펄스 트레인 간격 복사되어 나타난다.
plt.plot(t,freq_sig)

tmpSig=np.convolve(rect_sig,sampled_signal,'same')
plt.subplot(816) # 시간영역 rectangular 펄스 * 임펄스 트레인 신호를 컨볼루션한 신호
plt.plot(t,tmpSig)

freq_sig=np.abs(np.fft.fftshift(np.fft.fft(tmpSig)))
plt.subplot(817) # 주파수영역 rectangular 펄스 * 임펄스 트레인 신호를 컨볼루션한 신호
plt.plot(t,freq_sig)

LPF_f=10
t_ldf=np.arange(-0.5,0.5,step)
LPF=[]
for t1 in t_ldf:
    if(t1==0):
        tmp_LPF=1
    else:
        tmp_LDF=np.sin(2*np.pi*LPF_f*t1)/(2*np.pi*LPF_f*t1)
    LPF.append(tmp_LDF)
LPF_sig=np.convolve(sampled_signal,LPF,'same')
fil_sig=LPF_sig/np.sum(LPF)*2

LPF_f=10
t_ldf=np.arange(-0.5,0.5,step)
LPF=[]
for t1 in t_ldf:
    if(t1==0):
        tmp_LPF=1
    else:
        tmp_LDF=np.sin(2*np.pi*LPF_f*t1)/(2*np.pi*LPF_f*t1)
    LPF.append(tmp_LDF)
LPF_sig=np.convolve(fil_sig,LPF,'same')
Fil_sig=LPF_sig/np.sum(LPF)*2

LPF_f=10
t_ldf=np.arange(-0.5,0.5,step)
LPF=[]
for t1 in t_ldf:
    if(t1==0):
        tmp_LPF=1
    else:
        tmp_LDF=np.sin(2*np.pi*LPF_f*t1)/(2*np.pi*LPF_f*t1)
    LPF.append(tmp_LDF)
LPF_sig=np.convolve(Fil_sig,LPF,'same')
fFil_sig=LPF_sig/np.sum(LPF)*2

LPF_f=10
t_ldf=np.arange(-0.5,0.5,step)
LPF=[]
for t1 in t_ldf:
    if(t1==0):
        tmp_LPF=1
    else:
        tmp_LDF=np.sin(2*np.pi*LPF_f*t1)/(2*np.pi*LPF_f*t1)
    LPF.append(tmp_LDF)
LPF_sig=np.convolve(fFil_sig,LPF,'same')
ffFil_sig=LPF_sig/np.sum(LPF)*2

LPF_f=10
t_ldf=np.arange(-0.5,0.5,step)
LPF=[]
for t1 in t_ldf:
    if(t1==0):
        tmp_LPF=1
    else:
        tmp_LDF=np.sin(2*np.pi*LPF_f*t1)/(2*np.pi*LPF_f*t1)
    LPF.append(tmp_LDF)
LPF_sig=np.convolve(ffFil_sig,LPF,'same')
fffFil_sig=LPF_sig/np.sum(LPF)*2
plt.subplot(818)

plt.plot(t,fffFil_sig)
plt.show()











