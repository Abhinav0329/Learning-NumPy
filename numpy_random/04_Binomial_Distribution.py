from numpy import random
"""It is a way to calculate the probability of getting a specific number of "successes" in a fixed number of tries,
 where each try has only two possible outcomes"""

"""n : Number of trials (must be ≥0).
p : Probability of success in each trial (range [0,1]).
size : The shape of the returned array (e.g., 1000 for a thousand samples)."""
import numpy as np
# n=10 trials, p=0.5 probability, 5 experiments
results = np.random.binomial(n=10, p=0.5, size=5)
print(results)

#Visualisation of Binomial distribution
import matplotlib.pyplot as plt
import seaborn as sns
sns.displot(random.binomial(n=10, p=0.5, size=1000))
plt.show()