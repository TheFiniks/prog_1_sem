import matplotlib.pyplot as plt
import numpy as np
from random import gauss
from statistics import mean
def MNK(xdata, ydata):
    l = len(xdata)
    a = (mean(x*y for x, y in zip(xdata, ydata))*l - mean(ydata)*l*mean(xdata)) / (mean(x**2 for x in xdata)*l - mean(xdata)**2*l)
    b = mean(ydata) - a * mean(xdata)
    return a, b
N = 25
current = [x*2.75/3 + gauss(0.0, 0.7) for x in range(N)]
voltage = [c * (562.79462 + gauss(0.0, 35)) + gauss(0.0, 100) for c in current]
a, b = MNK(current, voltage)
fig = plt.figure(figsize=(8, 4))
ax = fig.add_subplot(111)
ax.plot(current, voltage, '+', label='Exp.Data')
xdata = list(range(N))
ax.plot(xdata, [a*x+b for x in xdata], label='Approximation')
plt.xlabel('Current, A')
plt.ylabel('Voltage, V')
ax.grid()
plt.legend()
plt.show()
