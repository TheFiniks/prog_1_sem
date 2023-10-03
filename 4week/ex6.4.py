import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
with open('BTC.txt') as f:
    data = f.readlines()
date = [line[:10].split(',')[0] for line in data[1:]]
for i in range(len(date)):
    date[i] = f'{date[i][8:]}-{date[i][5:7]}-{date[i][:4]}'
price = [int(line.split(',')[4]) for line in data[1:]]
fig = plt.figure()
ax = fig.add_subplot(111)
xdata = list(range(len(price)))
ax.plot(date, price, color='r')
plt.xlabel('DATE, day')
plt.ylabel('PRICE, $')
plt.xticks([0, 200, 400, 600, 800, 1000, 1200, len(date)-1])
# z = np.polyfit(xdata, price, 3)
# p = np.poly1d(z)
# ax.plot(p(x) for x in xdata)
ax.grid()
plt.show()

