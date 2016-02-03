#!/usr/local/bin/python

from Bio import SeqIO
import sys

"""Renames entries in a fasta file with the name of the file (minus the extension) and enummerates 
each sequence. For example, if you run a file named SRS001112.fa through this program each 
sequence name will be redone as >SRS001112_1, >SRS001112_2, etc.. Usage: python rename_fasta.py 
input.fa
"""

filehandle = sys.argv[1]
sep = '.'
new_name = filehandle.split(sep, 1)[0]
i = 1
fixed_seqs = []

for record in SeqIO.parse(sys.argv[1], 'fasta'):
	record.id = new_name + "_" + str(i)
	fixed_seqs.append(record)
	i += 1 

outputhandle = open(new_name+".fixed.fasta", "w")
SeqIO.write(fixed_seqs, outputhandle, "fasta")
outputhandle.close()
