#!/usr/local/bin/python

import pandas as pd
import glob

"""Reads in all *.txt files in a directory (OTU tables tab deliniated), merges them on the column headers and then finds median counts for each taxa. Usage: python median_rarefied_counts_from_otu_table.py
"""

class colors:
	COMPLETE = '\033[92m'
	ENDC = '033[0m'

#read in all files in directory that end with .txt
files = glob.glob("*.txt")

#initialize empty dataframe and list
frame = pd.DataFrame()
list = []

#read in files, append to list
for f in files:
	print "Reading in %s" % f
	df = pd.read_csv(f, sep="\t", skiprows=1, header=0)
	list.append(df)

print colors.COMPLETE + "Total number of files read: %i" % len(list) + colors.ENDC

frame = pd.concat(list)
print colors.COMPLETE + "Concatenated Data Frame Constructed" + colors.ENDC

#now get median and collapse by OTU ID
median_data = frame.groupby("#OTU ID").median() 

#write to file
with open("median_otu_table.txt", "w") as outfile:
	median_data.to_csv(outfile, sep="\t")

outfile.close()

print + colors.COMPLETE "Complete, written to median_otu_table.txt" + colors.ENDC	


