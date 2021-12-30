import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm # 정규분포 , normal distribution

mu=0 # 평균값 = 0
sigma=1 # 표준편차 = 1
num_sample=10000000 # 샘플 수 = 1000
s=np.random.normal(mu,sigma,num_sample) # 랜덤 변수들을 생성
# 평균 mu , 표준편차 sigma 인 정규분포를 따르는 랜덤 변수 num_sample 생성
(A,B,C) = plt.hist(s,100,density=True)  #수식없이 pdf를 그리는 방법


plt.plot(B,1/(sigma*np.sqrt(2*np.pi))*np.exp(-((B-mu)**2)/(2*sigma**2)))

#normal pdf 그리기
#PDF=1
print((1/(sigma*np.sqrt(2*np.pi))*np.exp(-((5-mu)**2)/(2*sigma**2))))
#CDF 계산
print(norm.cdf(2)) # 수학적계산
print((np.sum(s<2)/num_sample)) # 실험적 계산


plt.show()