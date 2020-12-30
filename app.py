import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

data  = pd.read_csv("nutrition_dataset.csv")

x = data.name
y = data.total_fat

X = np.array(x)
Y = np.array(y)

axis_X = X[1:10]
axis_Y = Y[1:10]

bar = plt.bar(axis_X,axis_Y)
plt.xticks(rotation=90 , linespacing= 1)
plt.xlabel('Food items')
plt.ylabel('Calories')
plt.title('Calories Requirement')
plt.show()