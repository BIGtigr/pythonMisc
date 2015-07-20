import numpy as np
import sys
import pandas as pd
from pandas import Series, DataFrame

def perc_id_check():
	blast_in = sys.argv[1]
	arr = np.genfromtxt(blast_in, delimiter='\t', dtype=None)
	df = DataFrame(arr)

	keys = dict(df.groupby(['f0'], sort=True)['f2'].max())

	for k, v in keys.iteritems():
		print "Top hit:", k, v
		top_hits = [k,v]
		print top_hits

	collection = df[(df['f0'].isin(keys.keys())) & (df['f2'].isin(keys.values()))]

	print "Final collection contents: \n", df[(df['f0'].isin(keys.keys())) & (df['f2'].isin(keys.values()))]	
	np.savetxt('sorted_blast_out.txt', collection, delimiter='\t', fmt='%s')
	

perc_id_check()

#if df[0][0] == items[0][0] 



#keys = np.unique(sorted_df['f0'])
#print keys

#grouped = sorted_df.groupby(keys)
#print grouped
