import random
import sys
import numpy as np

"""Pseudo-random number generator without replacement. Useage: python random_number.py <upper limit range> <number of draws>. Outputs to text file random_numbers.txt
"""

with open("random_numbers.txt", "w") as f:
	list = random.sample(xrange(1,int(sys.argv[1])+1), int(sys.argv[2]))
	for item in list:
		print >> f, item

	f.close()

#Numpy solution
with open("randomNumber.txt", "w") as f1:
	nums = np.random.randint(1, high=int(sys.argv[1])+1, size=int(sys.argv[2])
	for item in nums:
		print >> f1, item 	

	f1.close()
