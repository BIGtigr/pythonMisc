from Bio import SeqIO
import sys
import pylab
import numpy as np

sizes = [len(rec) for rec in SeqIO.parse("test.fasta", "fasta")]
print "Number of sequences: ", len(sizes), "\n", "Minimum length: ",  min(sizes), "\n", "Maximum length: ", max(sizes)
print "Median length: ", np.median(sizes)
pylab.hist(sizes, bins=20)
pylab.show()

trim_metric = np.median(sizes)
print trim_metric

"""Trim fasta file based on length of sequence."""
kept_seqs = []

for i in SeqIO.parse(open("test.fasta", "rU"), "fasta"):
	if len(i.seq) >= trim_metric:
		kept_seqs.append(i)

print "Kept %i sequences" % len(kept_seqs)
	
output_fasta = open("len_trimmed.fasta", "w")
SeqIO.write(kept_seqs, output_fasta, "fasta")
output_fasta.close()
