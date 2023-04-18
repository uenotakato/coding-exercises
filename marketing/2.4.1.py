import numpy as np
import math
import matplotlib.pyplot as plt
np.random.seed(0)

generator = np.random.default_rng()
eps = generator.normal(0,0.3,100)

Z_t1 = np.random.uniform(0.5,1,100) #価格掛率
Z_t2 = np.empty(100) #山積み陳列の有無

u_t = np.random.rand(100)
y_t = np.empty(100) #販売個数

for i in range(100):
  '''
  Z_t1[i] <= 0.8は20%以上値引きされた際に山積み陳列がなされることを反映した設定。u_t[i] <= 0.3はそのときの山積み陳列の実施頻度に対応する。
  '''
  if u_t[i] <= 0.3 and Z_t1[i] <= 0.8:
    Z_t2[i] = 1
  else:
    Z_t2[i] = 0

  y_t[i] = math.exp(0.5 - 2.5*math.log(Z_t1[i]) + 0.8*Z_t2[i] + eps[i])

plt.scatter(Z_t1,y_t)
plt.show()
