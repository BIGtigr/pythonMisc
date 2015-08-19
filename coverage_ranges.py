#!/usr/local/bin/python

"""Reads in coverage depth file (eg samtools) where second column is position and third column is coverage depth. Prints VCF formatted coverage ranges to screen.
"""

import pandas as pd
from pandas import DataFrame
import sys
from operator import itemgetter
from itertools import groupby

#colors
class bcolors:
	COMPLETE = '\033[92m'
	ENDC = '\033[0m'

#initalize lists
ranges = []

#read in depth file (output from samtools)
f = pd.read_csv(sys.argv[1], sep="\t", header=None)
notzero = f.loc[f[2] != 0]
data = notzero[1].tolist() 

#get ranges
for k, g in groupby(enumerate(data), lambda(i,x):i-x):
	group = map(itemgetter(1), g)
	ranges.append((group[0], group[-1]))

#get into correct format for vcf file and print string to screen
range_stripped = ''.join(str(i) for i in ranges)
print bcolors.COMPLETE + "Coverage ranges %s: " % sys.argv[1] + bcolors.ENDC
print range_stripped.replace(", ", "-").replace("(", "").replace(")", ";")

