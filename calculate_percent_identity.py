#!/usr/local/bin/python
"""Read in alignment file of two sequences (fasta format), output percent identity. Useage: python input.fasta
"""

from Bio import AlignIO
import sys

align = AlignIO.read(sys.argv[1], "fasta")
first = list(align[0])
next = list(align[1])

matches = 0
gaps = 0

for n in range(0, len(first)):
	if first[n] == next[n]:
			matches += 1

perc_id = (matches*100)/float((len(first)))

print "Percent identity: %.2f" %perc_id

