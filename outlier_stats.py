#!/usr/bin/python

"""Pulls sequences that are shorter than a specified limit. Requires an input file in fasta format and a integer length limit provided as the first and second argument after the script is called. Additionally, you must provide an output file name as the third argument. For example: $python outlier_stats.py input.fasta 135 outliers.fasta. An additional file with just unique file names will also be created as outlier_ids.txt
"""

from sys import argv
from Bio import SeqIO

script, reads, limit, outliers_out = argv

#import argparse
#parser = argparse.ArgumentParser()
#parser.add_argument("echo")
#args = parser.parse_args()
#print args.echo
#NEED TO UPDATE THIS WITH BETTER ARGUMENTS
			
def pull_outliers():
#	reads = raw_input("Input fasta file: ")
#	limit = raw_input("Length limit: ")


	outliers = []
	for record in SeqIO.parse(open(reads), "fasta"):
		if len(record.seq) < limit:
			outliers.append(record)

	print "Found %i outliers" % len(outliers)

	output_handle = open(outliers_out, "w")
	SeqIO.write(outliers, output_handle, "fasta")
	output_handle.close()


def get_outlier_ids():

	with open(outliers_out, "r") as infile:
		outlier_ids = []		
		for line in infile:
			if line.startswith(">"):
				outlier_ids.append(line)
		print "Found %i unique outlier ids" % len(outlier_ids)
		infile.close()
	with open("outlier_ids.txt", "w") as outfile:
		for ids in outlier_ids:
			outfile.write("".join(map(str, sorted(set(outlier_ids))))+"\n") #writes to file without quotes and adds newline after every entry, sorted for unique (set) ids only
		outfile.close()

pull_outliers()
get_outlier_ids()




