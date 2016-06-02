"""Iterates over mutliple taxon or OTU tables (like summary of summarize_taxa.py), transposes, merges on column name and get the median count for each sample for each taxa.
"""

import glob
import pandas as pd

fileList = glob.glob("*.txt")
dfList = []
print "Reading in %i files" % len(fileList)

for f in fileList:
	df = pd.read_csv(f, skiprows=1, delimiter="\t", skip_blank_lines=True, index_col=0)
	print "Now reading %s" % f
	trans = pd.DataFrame(df).transpose()
	dfList.append(trans)
	dfConcat = pd.concat(dfList)
	rowGroup = dfConcat.groupby(level=0).median()
	
print "Writing to medianCountsOTUtabe.txt"
rowGroup.to_csv("medianCountsOTUtable.txt", sep="\t", header=True, index=True)

