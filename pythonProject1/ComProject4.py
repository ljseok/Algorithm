import numpy as np

mu=0 # 평균
sigma=0.3#variance = sigma**2
DataSize=10000 # 데이터갯수

noise=np.random.normal(mu,sigma,DataSize) # 평균 0 , vari 0.7 , 데이터갯수 만큼 생성
#print(np.mean(noise**2))


signal = 2*np.random.randint(0,2,DataSize) -1 # 1--> 1 , 0--> -1
rcv_sig=signal+noise # 수신 신호 = 신호 + 노이즈
posi_si=(rcv_sig>0)+0 # rcv_sig가 0보다 큰 것을 찾아라 , 0보다 큰것은 1로 바뀐다.
ng_sig=-(rcv_sig<0)+0 # rcv_sig가 0보다 작은 것은 찾아라, 0보다 작은것은 1로 바뀐다.

final=posi_si+ng_sig

recovery = (np.sum(np.abs(signal-final)/2)/DataSize) # 오류

print(signal)

#print(noise)

#print(rcv_sig)

#print(posi_si) #0보다 커지면 -->1 0보다 작이지면 -->0

#print(ng_sig) #0보다 작아지면 --> -1 0보다 커지면-->0

print(final)

print(recovery)

