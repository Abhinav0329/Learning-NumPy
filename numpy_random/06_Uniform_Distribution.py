from numpy import random
"""It Used to describe probability where every event has equal chances of occuring.
It has three parameters:
low - lower bound - default 0.0
high - upper bound - default 1.0
size - The shape of the returned array"""

import numpy as np
x = np.random.uniform(size=(2,3))
print(x)

#Visualising the Uniform distribution
import matplotlib.pyplot as plt
import seaborn as sns
sns.displot(random.uniform(size=1000), kind="kde")
plt.show()