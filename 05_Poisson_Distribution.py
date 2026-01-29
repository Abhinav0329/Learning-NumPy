from numpy import random
"""It is a discrete probability distribution used to predict the number of times an event will occur in a fixed interval of time or space.
e.g. If someone eats twice a day what is the probability he will eat thrice?"""

""" PARAMETERS:-
lam: The expectation of interval (must be ≥0).
size: The shape of the returned array. If you want 1,000 samples, set size=1000."""

import numpy as np
# Suppose a cafe gets an average of 5 customers per hour (lam = 5)
# Let's simulate 10 different hours
samples = np.random.poisson(lam=5, size=10)
print(samples)

#Visualisation of Poisson Distribution
import matplotlib.pyplot as plt
import seaborn as sns
sns.displot(random.poisson(lam=2, size=1000))
plt.show()
#NOTE : As λ increases, the distribution starts to look more like a Normal (Gaussian) distribution.