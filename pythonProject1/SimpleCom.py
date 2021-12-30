import numpy as np

num_data = 1000000
data=np.random.randint(0,2,num_data) # 0이상 2미만 num_data만큼 생성
noise_power=0.2 # 노이즈 크기
noise=np.random.randn(num_data)*noise_power
rcv_data=data+noise
demod_data=(rcv_data>0.5)*1 # 0.5 미만이면 0 0.5 넘으면 1
# 0-->0 = 0 0-->1 = -1 1-->0 = 1

print("원래데이터", data)
print("수신데이터", demod_data)
print("오류데이터 수", np.sum(np.abs(demod_data-data)))