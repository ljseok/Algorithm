import matplotlib.pyplot as plt
import numpy as np

data_size = 100000 # data size
max_snr = 11 # snr을 몇  db 까지 실험
ber=[] # bit error rate

for snr_db in range(0,max_snr):
    signal = np.random.randint(0,2,data_size)*2-1
    noise_std = 10**(-snr_db/20)
    noise = np.random.randn(data_size)*noise_std/np.sqrt(2) # 노이즈를 신호의 갯수 만큼 생성하고 s^2 = 1 , snr 일정 노이즈를 감소
    rcv_sig = signal+noise
    detected_sig =((rcv_sig>0)+0)*2-1
    num_error = np.sum(np.abs(detected_sig-signal))/2
    ber.append(num_error/data_size)

snr = np.arange(0,max_snr)
plt.semilogy(snr,ber)
plt.show()