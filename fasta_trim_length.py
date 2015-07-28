from Bio import SeqIO
import sys, pylab
import numpy as np
import matplotlib.pyplot as plt

def fasta_trim_length():
	infasta = sys.argv[1]

	#get size statistics and generate length histogram
	sizes = [len(rec) for rec in SeqIO.parse(infasta, "fasta")]
	print "Number of sequences: ", len(sizes), "\n", "Minimum length: ",  min(sizes), "\n", "Maximum length: ", max(sizes)
	print "Median length: ", np.median(sizes)
	plt.hist(sizes, bins=25)
	plt.show(block=False)
	next = raw_input("Save histogram?: ")

	if 'y' in next:
		save_name = raw_input("Save as (default is png, to save as pdf add file extension): ")
		plt.savefig(save_name)

	next = raw_input("Do you want to trim your fasta file by the median length?: ")

	if 'y' in next:
		#trim fasta based on median size
		trim_metric = np.median(sizes)
		print "Keeping sequences that are more than or equal to: ", trim_metric
		kept_seqs = []

		for i in SeqIO.parse(open(infasta, "rU"), "fasta"):
			if len(i.seq) >= trim_metric:
				kept_seqs.append(i)

		print "Kept %i sequences" % len(kept_seqs)
	
		output_fasta = open("len_trimmed.fasta", "w")
		SeqIO.write(kept_seqs, output_fasta, "fasta")
		output_fasta.close()
	else:
		print "Successful completion, no trim"
		
fasta_trim_length()
