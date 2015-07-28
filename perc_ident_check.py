import numpy as np
import sys
import pandas as pd
from pandas import Series, DataFrame

def perc_id_check():
	blast_in = sys.argv[1]
	arr = np.genfromtxt(blast_in, delimiter='\t', dtype=None)
	df = DataFrame(arr)

	keys = dict(df.groupby(['f0'], sort=True)['f2'].max())

	#for k, v in keys.iteritems():
	#	print "Top hit:", k, v
	#	top_hits = [k,v]
	#	print top_hits
	
	df2 = DataFrame(keys.items())
	merged_df = pd.merge(df, df2, left_on=['f0', 'f2'], right_on=[0,1])
	cleaned_df = merged_df.drop([0,1], axis=1)

	print "Final collection contents: \n", cleaned_df	
	np.savetxt('sorted_blast_out.txt', merged_df, delimiter='\t', fmt='%s')
	

perc_id_check()

