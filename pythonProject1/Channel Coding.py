import matplotlib.pyplot as plt
import numpy as np
import ConvCode as cc

data_size = 100
max_snr = 10
ber=[]

for snr_db in range(0,max_snr):
    data = np.random.randint(0, 2, data_size)
    encoded_bit = cc.Encoder(data)

    real = encoded_bit[0, :] * 2 - 1
    imag = encoded_bit[0, :] * 2 - 1

    qpsk_sym = (real + 1j * imag) / np.sqrt(2)
    ofdm_sym = np.fft.ifft(qpsk_sym) * np.sqrt(data_size)

    noise_std = 10 ** (-snr_db / 20)
    noise = np.random.randn(data_size) * noise_std / np.sqrt(2) + 1j * np.random.randn(data_size) * noise_std / np.sqrt(2)

    rcv_signal = ofdm_sym
    rcv_signal = np.fft.fft(rcv_signal) / np.sqrt(data_size)

    real_detected_sig = np.array(((rcv_signal.real > 0) + 0)).reshape(1, data_size + 4)
    imag_detected_sig = np.array(((rcv_signal.real > 0) + 0)).reshape(1, data_size + 4)

    error = np.sum(np.abs(real - real_detected_sig)) / 2 + np.sum(np.abs(imag - imag_detected_sig)) /2
    ber.append(error / (data_size * 10000)) # 데이터를 10^-5승까지 나타내기 위해

snr = np.arange(0, max_snr)
plt.semilogy(snr,ber)
plt.show()



