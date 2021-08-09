import numpy as np
from math import pi


class Statistics:
	def __init__(self):
		pass
				
	def mean(self,vals):
		vals = np.array(vals)
		calc_mean=np.sum(vals)/len(vals)
		print "The mean is:", calc_mean
		return calc_mean
		
	def std(self,vals):
		vals = np.array(vals)
		m = self.mean(vals)
		n = len(vals)
		print n
		sub_square=[]
 		for i in range(0,n):
			sub_square.append((vals[i]-m)**2)
		sub_square=np.sum(sub_square)	
		std = np.sqrt(sub_square/(n-1))
		print "The standard deviation is:", std
		
	def range(self):
		print "range"
		
	def occurences(self,vals):
		occr=[]
		for i in (len(vals)-1):
			occr.append(occr.count(i))
			
		print occr 
		return occr
		
# print "ran through"
# Statistics().mean()
stats = Statistics()
stats.std([1,2,3,4.])
stats.mean([1,2,3,4.])
stats.occurences([1,2,3,4,5.])





























































































































































































































































