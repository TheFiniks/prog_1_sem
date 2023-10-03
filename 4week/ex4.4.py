import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from statistics import mean


def MNK(xdata, ydata):
    l = len(xdata)
    a = (mean(x * y for x, y in zip(xdata, ydata)) * l - mean(ydata) * l * mean(xdata)) / (
                mean(x ** 2 for x in xdata) * l - mean(xdata) ** 2 * l)
    b = mean(ydata) - a * mean(xdata)
    return a, b


with open('iris-data.txt', 'r') as f:
    data = f.readlines()
l = 150
Petal = [['0'] * 2 for i in range(l)]
Petal_L = [float(line.split(',')[1]) for line in data[1:]]
Petal_W = [float(line.split(',')[2]) for line in data[1:]]
for j in range(l):
    Petal[j][0]=Petal_L[j]
    Petal[j][1]=Petal_W[j]
Petal = sorted(Petal)
Petal_L = [float(line[0]) for line in Petal]
Petal_W = [float(line[1]) for line in Petal]
Sepal_L = [float(line.split(',')[3]) for line in data[1:]]
Sepal_W = [float(line.split(',')[4]) for line in data[1:]]
a_P, b_P = MNK(Petal_W, Petal_L)
a_S, b_S = MNK(Sepal_W, Sepal_L)
xdata = np.arange(0, 5, 0.1)
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(Petal_W, Petal_L, '+', label='Petal')
ax.plot(xdata, [a_P * x + b_P for x in xdata], label=f'k={a_P}')
ax.plot(Sepal_W, Sepal_L, 'o', label='Sepal')
ax.plot(xdata, [a_S * y + b_S for y in xdata], label=f'k={a_S}')
plt.xlabel('Width, sm')
plt.ylabel('Length, sm')
ax.grid()
plt.legend()
plt.show()

