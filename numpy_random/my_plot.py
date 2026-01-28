#Plotting a (displot : It tells you where your numbers are crowded together and where they are spread out)
import matplotlib.pyplot as plt# It provides the window and the tools needed to display a window on your screen
import seaborn as sns# It is built on top of Matplotlib and is designed to make data look beautiful and easy to read
sns.displot([0, 1, 2, 3, 4, 5])# This tells Seaborn to create a Distribution Plot. It looks at your list of numbers and draws a bar (histogram) for each number to show how often it appears
plt.show()# This actually opens the window to show you the final drawing.

#Plotting a displot without a histogram
sns.displot([0, 1, 2, 3, 4, 5],kind="kde")
plt.show()