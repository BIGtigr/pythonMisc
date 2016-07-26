#!/usr/bin/python3

'''Script used to split out phyla specific reads (taken from sam files) and get read ids -- used for shotgun source assembly test, July 2, 2016'''

import glob
import pandas as pd

flist = glob.glob('*split')

dfList = [pd.read_table(file) for file in flist]

phylaList = {}

for file in flist:
     f = open(file, 'r')
     phylaList[file] = f.read().splitlines()

samFile = pd.read_csv('gutSam.txt', sep="\t")

#convert values to int
phylaDict = {}
for key, value in phylaList.iteritems():
     phylaDict[key] = [int(item) for item in value]

#loop
phylaDF = {}
for key in phylaList.keys():
     phylaDF[key] = samFile[samFile['refID'].isin(phylaDict.get(key))]

#write out
outList = [w.replace('split', 'out') for w in flist]

for i in range(0, len(outList)):
     pd.DataFrame(phylaDF.values()[i]).to_csv(outList[i], header=False, index=False, sep='\t')

