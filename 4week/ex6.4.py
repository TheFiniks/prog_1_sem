import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
data = pd.read_csv('BTC.csv')
data.drop(['open', 'high', 'low'], axis=1, inplace=True)
data['time'] = pd.to_datetime(data['time'])
data.set_index('time', inplace=True)
ax = plt.subplot()
ax.plot_date(data.index, data.values, fmt='-', color='r')
plt.xlabel('DATE, year')
plt.ylabel('PRICE, $')
time_ax = []
for i in data.index:
    time_ax.append(pd.Timestamp(i).timestamp())
data = data.assign(time_int = time_ax)
polynomial_approximation = np.poly1d(np.polyfit(data['time_int'], data['close'], 18))
ax.plot(data.index, polynomial_approximation(data['time_int']), color='green')
ax.grid()
plt.show()
