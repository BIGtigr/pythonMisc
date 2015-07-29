from Bio import SeqIO
import sys
import numpy as np
from pandas import DataFrame
import pandas as pd

"""Takes an interleaved fastq file with paired and singleton sequences and splits into singletons,
merged paired, split forward, and split reverse fastq files. 
Usage: python split_interleaved_fastq.py input.fastq
"""

def split_interleaved_fastq():
	infastq = sys.argv[1]
	headers = []

	for record in SeqIO.parse(infastq, "fastq"):
		headers.append(record.description)
	headersNL = '\n'.join(headers)

	with open("headers.txt", "w") as outfile:
		outfile.write(headersNL)

	headersDF = np.loadtxt("headers.txt", dtype="str")
	df = DataFrame(headersDF)

	grouped = df.groupby(df[1])

	reads1 = grouped.get_group(np.unique(df[1])[0])
	reads2 = grouped.get_group(np.unique(df[1])[1])

	merged_reads = pd.merge(reads1, reads2, on=0, how='outer')

	singletons = []
	paired = []

	indexed_reads = merged_reads.set_index(0)
	paired_ids = pd.DataFrame.dropna(indexed_reads).index.get_values()
	single_ids = indexed_reads[indexed_reads.isnull().any(axis=1)].index.get_values()

	with open("singleton_ids.txt", "w") as singlesOut:
		print >> singlesOut, "\n".join(str(i) for i in single_ids)

	with open("paired_ids.txt", "w") as pairedOut:
		print >> pairedOut, "\n".join(str(i) for i in paired_ids)
	
	paired_wanted = set(line.rstrip("\n").split(None,1)[0] for line in open("paired_ids.txt"))
	single_wanted = set(line.rstrip("\n").split(None,1)[0] for line in open("singleton_ids.txt"))

	print "Found %i paired reads " % len(paired_wanted)
	print "Found %i single reads " % len(single_wanted)

	paired_records = (r for r in SeqIO.parse(infastq, "fastq") if r.id in paired_wanted)
	single_records = (r for r in SeqIO.parse(infastq, "fastq") if r.id in single_wanted)
	
	pairedOut = "paired_out.fastq"
	singleOut = "singletons.fastq"
	pairedCount = SeqIO.write(paired_records, pairedOut, "fastq") 
	singleCount = SeqIO.write(single_records, singleOut, "fastq")

	print "Saved %i singleton sequences from %s to %s" % (singleCount, infastq, singleOut)

	#now split the paired into forward and reverse
	forwardReads = []
	reverseReads = []
	forwardOut = "forward_reads.fastq"
	reverseOut = "reverse_reads.fastq"

	for record in SeqIO.parse("paired_out.fastq", "fastq"):
		if "1:N:0:" in record.description:
			forwardReads.append(record)
		elif "2:N:0:" in record.description:
			reverseReads.append(record)
		else:
			print record.id, "has no forward/reverse info"

	forwardCount = SeqIO.write(forwardReads, forwardOut, "fastq")
	reverseCount = SeqIO.write(reverseReads, reverseOut, "fastq")	
		
	print "Saved %i forward reads from %s to %s" % (forwardCount, infastq, forwardOut)
	print "Saved %i reverse reads from %s to %s" % (reverseCount, infastq, reverseOut)

split_interleaved_fastq()
