import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
data = pd.read_csv('iris_data.csv')
iris_length = list(data['PetalLengthCm'])
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
