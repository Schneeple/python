import random
import numpy as np
import matplotlib.pyplot as plt
import chart_studio.plotly as py

# Odds for Craps and Histogram graph

def roll():
	roll_one= random.randint(1,6)
	roll_two=random.randint(1,6)
	sum=roll_one+roll_two
	if sum > 12:
		print("Error, sum can not be above 12")
	return sum

x=0 # Starting number of rolls which is zero.
j=500 # Number of rolls, 
result=[] # Empty Matrix
for i in range (1,j):
	while x<j:
		result.append(roll())
		x+=1


plt.hist(result)
plt.title("Gaussian Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")
fig = plt.gcf()
plot_url = py.plot_mpl(fig, filename='Craps-histogram')