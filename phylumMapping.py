import pandas as pd
import argparse

'''Usage: python phylumMapping.py -c collapsedTable.txt -p pairedTable.txt -t truncactedTable.txt -o output.txt'''
parser = argparse.ArgumentParser()

parser.add_argument('-c', '--collapsedTable', required=True)
parser.add_argument('-p', '--pairedTable', required=True)
parser.add_argument('-t', '--truncatedTable')
parser.add_argument('-o', '--outputTable', default='mergedOut.txt')

args = parser.parse_args()

collapsed = pd.read_csv(args.collapsedTable, sep="\t", index_col=0)
paired = pd.read_csv(args.pairedTable, sep="\t", index_col=0)
trunc = pd.read_csv(args.truncatedTable, sep="\t", index_col=0)

midasMap = pd.read_csv("midas_phylumMap.txt", sep="\t", index_col=0)

wantedPhyla = ['Actinobacteria', 'Bacteroidetes', 'Chlamydiae', 'Chlorobi', 'Chloroflexi', 'Euryarchaeota', 'Firmicutes', 'GN02', 'Gracilibacteria', 'Proteobacteria', 'Saccharibacteria', 'TM7', 'Spirochaetes', 'SR1', 'Synergistetes', 'WPS-2']

intermediate = collapsed.add(paired)
speciesProfile = intermediate.add(trunc)

merged = pd.merge(speciesProfile, midasMap, left_index=True, right_index=True)

mergeCollapse = merged.groupby("phylum").sum()

#clean up merged table
mergeCollapse.drop(['relative_abundance', 'coverage'], 1, inplace=True)

#get rid of phyla with zero counts
clean = mergeCollapse[(mergeCollapse.T != 0).any()]

#reset index so we can access phyla as column
clean.reset_index(inplace=True)

#get rid of phyla we don't want to include
mask = clean['phylum'].isin(wantedPhyla)
finalClean = clean[mask]

#get total counts
totCount = finalClean['count_reads'].sum()

#add new relative abundance column
finalClean['relativeAbundance'] = finalClean['count_reads']/totCount*100

with open(args.outputTable, "w") as outfile:
	finalClean.to_csv(outfile, sep="\t", index=False)

print("New phylum map written to %s" % args.outputTable) 
