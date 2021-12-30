import matplotlib.pyplot as plt
import numpy as np

data_size = 1000000 # qpsk
max_snr = 14 # 최대 snr 13db 까지 실험
ber=[] # ber 배열
for snr_db in range(0,max_snr):
    real_signal = np.random.randint(0,2,data_size) * 2 - 1 #-1과 1을 발생
    imag_signal = np.random.randint(0,2,data_size) * 2 - 1

    qpsk_sym = (real_signal + 1j*imag_signal)/np.sqrt(2) # 에너지가 1짜리 QPSK symbol
    noise_std =10 ** (-snr_db / 20) # 노이즈
    noise = np.random.randn(data_size)*noise_std/np.sqrt(2) + 1j*np.random.randn(data_size)*noise_std/np.sqrt(2)
    # 실수부 노이즈 + 허수부 노이즈
    rcv_signal = qpsk_sym+noise # 수신신호 = QPSK symbol + 노이즈

    real_detected_sig = ((rcv_signal.real> 0 ) + 0) * 2 - 1
    imag_detected_sig = ((rcv_signal.imag > 0) + 0) * 2 - 1

    # 0보다 작다 크다 true false 나오는데 0을 더 더하게 되면 1,0으로 나타난다.
    # true 는 1로 나타나게 되고 false 는 0으로 나타나게 된다.

    num_error = np.sum(np.abs(real_signal-real_detected_sig))/2 + np.sum(np.abs(imag_signal-imag_detected_sig))/2
    ber.append(num_error/(data_size*2)) # 하나의 QPSK symbol은 두개의 비트을 가지고 있기때문에 *2를 한다. bit error rate


snr=np.arange(0,max_snr)
plt.semilogy(snr,ber)
plt.show()


