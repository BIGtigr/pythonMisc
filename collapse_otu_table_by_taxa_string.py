#!/usr/local/bin/python

import pandas as pd
from pandas import DataFrame
import sys

"""Reads in tab delimited OTU table and returns OTU table collapsed by taxa string (useful for duplicates brought on by formatting issues. OTU table must have no commented out lines). Usage: python collapse_otu_table_by_taxa_string.py input_otu_table.txt
"""
#need to first remove comment lines and symbols from otu table. can re add in later. 

df = pd.read_csv(sys.argv[1], sep="\t")
collapsed_df = df.groupby("OTU ID").sum()

dups = df.shape[0] - collapsed_df.shape[0]

print "Number of duplicate rows to be collapsed: %i" %dups 

with open("collapsed_otu_table.txt", "w") as outfile:
	collapsed_df.to_csv(outfile, sep="\t")

outfile.close()
