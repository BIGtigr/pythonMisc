import random
import sys

with open("random_numbers.txt", "w") as f:
	list = random.sample(range(1,int(sys.argv[1])), 5000000)
	for item in list:
		print >> f, item



