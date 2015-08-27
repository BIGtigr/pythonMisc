import random
import sys

"""Random number generator without replacement. Useage: python random_number.py <upper limit range> <number of draws>. Outputs to text file random_numbers.txt
"""

with open("random_numbers.txt", "w") as f:
	list = random.sample(xrange(1,int(sys.argv[1])), int(sys.argv[2]))
	for item in list:
		print >> f, item



