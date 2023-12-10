from statistics import mean


def MNK(xdata, ydata):
    l = len(xdata)
    if l != len(ydata):
        return 'dif size'
    if l == 0 or len(ydata) == 0:
        return 'no data'
    if l == 1 and xdata[0] == 0:
        return (0.0, float(ydata[0]))
    if len(xdata) == 1 and len(ydata) == 1:
        return ydata[0] / xdata[0]
    a = (mean(x * y for x, y in zip(xdata, ydata)) * l - mean(ydata) * l * mean(xdata)) / (
            mean(x ** 2 for x in xdata) * l - mean(xdata) ** 2 * l)
    b = mean(ydata) - a * mean(xdata)
    return a, b

