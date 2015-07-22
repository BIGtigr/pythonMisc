import numpy as np
import sys, pylab, os
from Bio import SeqIO
import matplotlib.pyplot as plt

if len(sys.argv) != 3:
	print "Error: needs two input files"
	print "Usage --> python length_hist_with_insert_size.py assembled.fastq unassembled_insert_size.txt"
	sys.exit(1)

def length_histogram():
	fastq_input=sys.argv[1]
	freq_table=sys.argv[2]
	
	sizes=[len(seq) for seq in SeqIO.parse(fastq_input, "fastq")]
	print sizes	

	arr=np.loadtxt(freq_table, delimiter="\t", dtype=int)
	count=arr[:,0]
	length=arr[:,1]

	new_sizes=np.repeat(length,count,axis=0)
	merged_sizes=sizes+new_sizes.tolist()
	
	plt.hist(merged_sizes, bins=25, facecolor="green")
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
