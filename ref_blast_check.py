#!/usr/local/bin/python

import pandas as pd
from pandas import DataFrame
import sys
import csv

"""This program reads in a list of GI accession numbers from NCBI and a tab separated blast output file where the query sequence ID is the first column, reference ID in second, and percent identity is fourth from the last column. Returns a list of query IDs that are either the only match or represent the top matches for some taxa or group of taxa as represented in the GI query list. Usage: python ref_blast_check.py gi_accession.list blast_output.txt
"""

gi_list = []

with open(sys.argv[1], "r") as f:
	for line in f:
		line = line.strip()
		gi_list.append(line)

blast_dat = []
with open(sys.argv[2], "r") as f:
	for line in f:
		if not line.strip():
			continue
		else:
			try:
				record = line.split()
				t = record[1]
			except IndexError:
				break
		record = line.split()
		ref = record[1].split("|")
		seqID = record[0]
		percID = record[-4]
		giNum = ref[1]
		blast_dat.append([seqID, giNum, percID])
	blastData = DataFrame(blast_dat)
	blastData.columns = ['seqID', 'giNum', 'percID']


#get singleton list
blastData['counts'] = blastData.groupby('seqID')['seqID'].transform('count')
singletons = blastData.loc[blastData['counts'] == 1]

singleHits = singletons[singletons['giNum'].isin(gi_list)]

#get double list
doubles = blastData.loc[blastData['counts'] >=2]

groups = doubles.groupby('seqID')
seqID_list = []

for name, group in groups:
	seqID_list.append(name)

hit_list = []

#run thorough duplicate list, sort rows by percent id, if top two values are in gi list, add to hit list
init = 0
for i in range(0, len(seqID_list)):
	groupedHits = groups.get_group(seqID_list[init]).sort('percID').reset_index()
	first = groupedHits['giNum'][0]
	second = groupedHits['giNum'][1]
	if first and second in gi_list:
		hit_list.append(groupedHits['seqID'][0])
        init += 1

hit_list.append(singleHits['seqID'].tolist())

for line in hit_list:
	print "".join(str(item) for item in line)
