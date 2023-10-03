import matplotlib.pyplot as plt
import numpy as np
values = np.random.normal(0, 5, 100)
plt.hist(values, 100, color='red')
values = np.random.normal(0, 5, 500)
plt.hist(values, 100, color='blue', alpha=0.75)
values = np.random.normal(0, 5, 1000)
plt.hist(values, 50, color='pink', alpha=0.5)
plt.show()
