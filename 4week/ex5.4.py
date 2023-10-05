import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
data = pd.read_csv('BTC.csv')
date = list(data['time'])
for i in range(len(date)):
    date[i] = f'{date[i][8:10]}-{date[i][5:7]}-{date[i][:4]}'
price = list(data['close'])
fig = plt.figure()
ax = fig.add_subplot(111)
xdata = list(range(len(price)))
ax.plot(date, price, color='r')
plt.xlabel('DATE, day')
plt.ylabel('PRICE, $')
plt.xticks([0, 200, 400, 600, 800, 1000, 1200, len(date)-1])
ax.grid()
plt.show()

