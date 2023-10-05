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


data = pd.read_csv('iris_data.csv')
Petal_L = list(data['SepalLengthCm'])
Petal_W = list(data['SepalWidthCm'])
Sepal_L = list(data['PetalLengthCm'])
Sepal_W = list(data['PetalWidthCm'])
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

