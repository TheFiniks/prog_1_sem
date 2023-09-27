from random import gauss
from statistics import mean
def MNK(xdata, ydata):
    l = len(xdata)
    #a = (mean(x*y for x, y in zip(xdata, ydata)) - mean(ydata)*mean(xdata)) / (mean(x**2 for x in xdata) - mean(xdata)**2)
    a = (mean(x*y for x, y in zip(xdata, ydata))*l - mean(ydata)*l*mean(xdata)) / (mean(x**2 for x in xdata)*l - mean(xdata)**2*l)
    b = mean(ydata) - a * mean(xdata)
    return a, b
N = int(input())
current = [x*2.75/3 + gauss(0.0, 0.7) for x in range(N)]
voltage = [c * (562.79462 + gauss(0.0, 35)) + gauss(0.0, 100) for c in current]
print(MNK(current, voltage))
