import numpy as np
import sys
import pylab
import os
from Bio import SeqIO
import matplotlib.pyplot as plt

"""Generates fragment length histogram from two files: 1) an assembled fastq file (eg from pear output),
2) a two column, tab separated frequency table where the first column is a list of insert sizes and the
second is a list of counts per insert size (eg from picard tools insert size metrics output). 
Useful if you want to get the true distribution of paired fragment lengths and have sequences that are 
too long or too short to assemble properly with pear
"""

if len(sys.argv) != 3:
	print "Error: needs two input files"
	print "Usage --> python length_hist_with_insert_size.py assembled.fastq unassembled_insert_size.txt"
	sys.exit(1)

def length_histogram():
	fastq_input=sys.argv[1]
	freq_table=sys.argv[2]
	
	sizes=[len(seq) for seq in SeqIO.parse(fastq_input, "fastq")]
	#print sizes	

	arr=np.loadtxt(freq_table, delimiter="\t", dtype=int)
	count=arr[:,1]
	length=arr[:,0]

	new_sizes=np.repeat(length,count,axis=0)
	merged_sizes=sizes+new_sizes.tolist()
	
	plt.hist(merged_sizes, bins=range(min(merged_sizes), max(merged_sizes) + 5, 5), histtype='step')
	plt.xlabel("length")
	plt.ylabel("count")
	plt.title("Insert Size/Merged Fragment Length")
	plt.show(block=False)

	next=raw_input("Save histogram?: ")
	
	if 'y' in next:
		save_name=raw_input("Save as: ")
		plt.savefig(save_name)
	else:	
		print "Finished"

length_histogram()
