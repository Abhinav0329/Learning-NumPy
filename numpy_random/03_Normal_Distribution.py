from numpy import random
"""Normal Distribution (also known as the Bell Curve or Gaussian Distribution) is a way to generate data where most numbers cluster around a central average
and fewer numbers appear as you move toward the extremes."""

x = random.normal(loc = 1, scale = 2, size = (2,3))
print(x)

"""1.loc (Mean): This is the average value where most data points will sit and peak of the bell exists.
2.scale (Standard Deviation): The "spread" or width of the curve. A higher number means the data is more spread out; a lower number means it is tightly packed around the center.
3.size: The shape of the returned array."""

#Visualisation of normal distribution
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
data = np.random.normal(loc = 1, scale = 2, size = 1000)
sns.displot(data,kind="kde")
plt.show()
#The curve of a Normal Distribution is also known as the Bell Curve because of the bell-shaped curve.