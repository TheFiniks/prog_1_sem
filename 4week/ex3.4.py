import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
with open('iris-data.txt', 'r') as f:
    data = f.readlines()
iris_length = [float(line.split(',')[3]) for line in data[1:]]
less = 0
more_and_less = 0
more = 0
for length in iris_length:
    if length < 1.2:
        less+=1
    elif length > 1.5:
        more+=1
    else:
        more_and_less+=1
plt.pie([less, more_and_less, more], labels = ['<1.2sm','>1.2sm and <1.5sm','>1.5sm'])
plt.show()
