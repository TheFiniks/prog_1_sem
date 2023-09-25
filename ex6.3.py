from statistics import mean
def MNK(xdata, ydata):
    l = len(xdata)
    #a = (mean(x*y for x, y in zip(xdata, ydata)) - mean(ydata)*mean(xdata)) / (mean(x**2 for x in xdata) - mean(xdata)**2)
    a = (mean(x*y for x, y in zip(xdata, ydata))*l - mean(ydata)*l*mean(xdata)) / (mean(x**2 for x in xdata)*l - mean(xdata)**2*l)
    b = mean(ydata) - a * mean(xdata)
    return a, b
with open('measuarements.txt', 'r') as f:
    data = f.readlines()
current = [float(line.split()[0]) for line in data[1:]]
voltage = [float(line.split()[1]) for line in data[1:]]
print(MNK(current, voltage))
