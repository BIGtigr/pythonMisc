#!/usr/bin/env python

"""Script generates summary statistics on sequence lengths in a single fastq or fasta file, generates a length histogram using matplot lib that can be optionally saved as a png or pdf. The file can also be trimmed according to the calculated median sequence length. 
Two arguments passed to script: the fastq or fasta file and (optionally) a string indicating the file type. Example
useage: python seq_len_hist_trim.py input.fasta fasta.
"""

from Bio import SeqIO
import sys, pylab, os
import numpy as np
import matplotlib.pyplot as plt

if len(sys.argv) != 2: #checks that input file passed to script
	print "Error: no input file specified"
	print "Usage --> python seq_len_hist_trim.py input.fast[a|q] <fastq/fasta>"
	sys.exit(1)

def main():
	fasta_extensions = ('.fasta', '.fna', '.fa')
	fastq_extensions = ('.fastq', '.fq')
	input = sys.argv[1]
	#make sure file exists in path/working directory
	assert os.path.exists(input), 'File does not exist: %s. Do you need to provide the path?' %input	

	if input.endswith(fasta_extensions) or "fasta" in sys.argv[1:]:
		fasta_trim_length()
	elif input.endswith(fastq_extensions) or "fastq" in sys.argv[1:]:
		fastq_trim_length()
	else:
		print "File extension not recognized: Please rerun and specify if fastq or fasta file"

def fastq_trim_length():
        input = sys.argv[1]

        sizes = [len(rec) for rec in SeqIO.parse(input, "fastq")]
        print "---------------------------"
	print "Summary Statistics: "
	print "--------------------------"
	print "Number of sequences: ", len(sizes)
	print "Minumum length: ", min(sizes)
	print "Maximum length: ", max(sizes)
        print "Median length: ", np.median(sizes)
	print "Mean length: ", np.mean(sizes)
	print "25th percentile: ", np.percentile(sizes, 25)
	print "75th percentile: ", np.percentile(sizes, 75)
        print "Standard deviation: ", np.std(sizes)
        print "Variance: ", np.var(sizes)
	print "---------------------------"

        plt.hist(sizes, bins=25, facecolor='green')
        plt.xlabel('fragment length')
        plt.ylabel('count')
        #plt.grid(True) #uncomment to include background grid
        plt.title(input)
	print "Error: no file passed to script"
	#	sys.exit()
        plt.show(block=False)
        next = raw_input("Save histogram?: ")

        if 'y' in next:
                save_name = raw_input("Save as (default is png, to save as pdf add file extension): ")
                plt.savefig(save_name)

        next = raw_input("Do you want to trim your fastq file by the median length?: ")

        if 'y' in next:
                #trim fasta based on median size
                trim_metric = np.median(sizes)
                print "Keeping sequences that are more than or equal to: ", trim_metric
                kept_seqs = []

                for i in SeqIO.parse(open(input, "rU"), "fastq"):
                        if len(i.seq) >= trim_metric:
                                kept_seqs.append(i)

                print "Kept %i sequences" % len(kept_seqs)

                output_fastq = open("len_trimmed.fastq", "w")
                SeqIO.write(kept_seqs, output_fastq, "fastq")
                output_fastq.close()

        else:
                print "Successful completion, no trim"

def fasta_trim_length():
        input = sys.argv[1]

        #get size statistics and generate length histogram
        sizes = [len(rec) for rec in SeqIO.parse(input, "fasta")]
	print "---------------------------"
        print "Summary Statistics: "
        print "--------------------------"
        print "Number of sequences: ", len(sizes)
	print "Minimum length: ",  min(sizes)
	print "Maximum length: ", max(sizes)
        print "Median length: ", np.median(sizes)
        print "Mean length: ", np.mean(sizes)
        print "25th percentile: ", np.percentile(sizes, 25)
        print "75th percentile: ", np.percentile(sizes, 75)
	print "Standard deviation: ", np.std(sizes)
	print "Variance: ", np.var(sizes)
        print "---------------------------"

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

                for i in SeqIO.parse(open(input, "rU"), "fasta"):
                        if len(i.seq) >= trim_metric:
                                kept_seqs.append(i)

                print "Kept %i sequences" % len(kept_seqs)

                output_fasta = open("len_trimmed.fasta", "w")
                SeqIO.write(kept_seqs, output_fasta, "fasta")
                output_fasta.close()
        else:
                print "Successful completion, no trim"

main()
