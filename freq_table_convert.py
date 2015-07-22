import numpy as np
import sys

def freq_table_convert():
	input=sys.argv[1]

	arr=np.loadtxt(input, delimiter="\t", dtype=int)
	#text file must be in following format, 1st column is counts, 2nd lengths, tab separated
	count=arr[:,0]
	length=arr[:,1]
	
	new_sizes=[]
	new_sizes=np.repeat(length, count)
	return new_sizes

freq_table_convert()
