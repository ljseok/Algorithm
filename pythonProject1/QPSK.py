import matplotlib.pyplot as plt
import numpy as np

data=100000
snr=10
ber=[]

for snr_db in range(0,snr):
    real = np.random.randint(0,2,data) * 2 - 1
    imag = np.random.randint(0,2,data) * 2 - 1

    qpsk = (real + 1j * imag) / np.sqrt(2)
    ofdm = np.fft.ifft(qpsk) * np.sqrt(data)

    noise_ori = 10 ** (-snr_db / 20)
    noise = np.random.randn(data) * noise_ori / np.sqrt(2) + 1j * np.random.randn(data) * noise_ori / np.sqrt(2)

    rcv_signal = ofdm + noise
    rcv_signal = np.fft.fft(rcv_signal) / np.sqrt(data)

    real_det = ((rcv_signal.real > 0) +0) * 2 - 1
    imag_det = ((rcv_signal.imag > 0) +0) * 2 - 1

    error = np.sum(np.abs(real - real_det)) / 2 + np.sum(np.abs(imag - imag_det)) / 2
    ber.append(error / (data * 10000))

snr = np.arange(0,snr)
plt.semilogy(snr,ber)
plt.show()

