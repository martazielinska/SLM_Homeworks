import numpy as np
from sklearn.linear_model import LinearRegression
import time
import matplotlib.pyplot as plt


sizes= np.arange(10,210,10).tolist()
reps=10000

def sim_r_squared(n):
    x = np.random.normal(0, 1, n)

    y = [i + 1 + np.random.normal(0, 1) for i in x]
    print(y)

    x=x.reshape((-1,1))
    print(x.shape)
    model = LinearRegression().fit(x, y)
    return model.score(x, y)

r_squared_q95 = list(range(len(sizes)))
r_squared_q5 = list(range(len(sizes)))
r_squared_mean = list(range(len(sizes)))

start=time.time()

for i in range(len(sizes)):
    print(sizes[i])
    result = [sim_r_squared(sizes[i]) for j in range(reps)]
    r_squared_mean[i] = np.mean(result)
    r_squared_q5[i] = np.quantile(result, 0.05)
    r_squared_q95[i] = np.quantile(result, 0.95)

end=time.time()-start
print(end)

plt.plot(sizes, r_squared_mean)
plt.plot(sizes,  r_squared_q5)
plt.plot(sizes,  r_squared_q95)
plt.ylabel('R^2')
plt.xlabel('Sample Size')
plt.show()