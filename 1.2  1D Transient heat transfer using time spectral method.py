import numpy as np
import matplotlib.pyplot as plt
h = .25
k = .01
x = np.arange(0, 1+h, h)
t = np.arange(0, 1+k, k)
boundaryConditions = [np.sin(t), 1]
initialConditions = 0.5
n = len(x)
m = len(t)
T = np.zeros((n, m))
T[0, :] = boundaryConditions[0]
T[-1, :] = boundaryConditions[1]
T[:, 0] = initialConditions

factor = k/h**2
for j in range(1, m):
    for i in range(1, n-1):
        T[i, j] = factor*T[i-1, j-1] + \
            (1-2*factor)*T[i, j-1] + factor*T[i+1, j-1]
T.round(3)
plt.plot(T)
plt.legend(t)
plt.show()
