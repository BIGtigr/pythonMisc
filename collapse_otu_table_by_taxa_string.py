#!/usr/local/bin/python

import pandas as pd
from pandas import DataFrame
import sys

"""Reads in tab delimited OTU table and returns OTU table collapsed by taxa string (useful for duplicates brought on by formatting issues). Usage: python collapse_otu_table_by_taxa_string.py input_otu_table.txt
"""

class bcolors:
	COMPLETE = '\033[92m'

df = pd.read_csv(sys.argv[1], sep="\t", skiprows=1)
collapsed_df = df.groupby("#OTU ID").sum()

dups = df.shape[0] - collapsed_df.shape[0]

print "Number of duplicate rows to be collapsed: %i" %dups 

with open("collapsed_otu_table.txt", "w") as outfile:
	collapsed_df.to_csv(outfile, sep="\t")

outfile.close()
print bcolors.COMPLETE + "Complete, collapsed OTU table written to: collapsed_otu_table.txt"
