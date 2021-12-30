import matplotlib.pyplot as plt
import numpy as np

data_size=64 # 하나의 OFDM 심볼에 한번에 전송되는 OPSK 심볼의 수
max_snr=20
ber=[]

for snr_db in range(20,21): # snr을 높게 일단설정
    real = np.random.randint(0, 2, data_size) * 2 - 1 # 1과 -1을 생성
    imag = np.random.randint(0, 2, data_size) * 2 - 1 # 1과 -1을 생성

    qpsk_sym = (real + 1j * imag) / np.sqrt(2) # 64개의 QPSK
    ofdm_sym = np.fft.ifft(qpsk_sym) * np.sqrt(data_size) # 에너지가 손실된 만큼 곱해준다.


    noise_std = 10 ** (-snr_db / 20)  # 노이즈
    noise = np.random.randn(data_size) * noise_std / np.sqrt(2) + 1j * np.random.randn(data_size) * noise_std / np.sqrt(2)
    rcv_signal = ofdm_sym + noise
    rcv_signal = np.fft.fft(rcv_signal) / np.sqrt(data_size)
    # print(np.mean(np.abs(rcv) **2))

    plt.subplot(2,2,1)
    plt.plot(np.abs(qpsk_sym)**2)
    plt.subplot(2,2,2)
    plt.plot(np.abs(ofdm_sym) **2) # IFFT를 통과한 성상도
    plt.subplot(2,2,3)
    plt.scatter(ofdm_sym.real,ofdm_sym.imag)
    plt.subplot(2,2,4)
    plt.scatter(rcv_signal.real,rcv_signal.imag)
    #plt.subplot(2,2,5)
   #plt.plot()

    plt.show()

