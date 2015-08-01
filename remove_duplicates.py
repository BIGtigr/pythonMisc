#!/usr/local/bin/python

import pandas as pd
from pandas import DataFrame
import sys
import numpy as np

def find_pcr_opt_dups(dups):
	"""From a dataframe generated using read_sam_get_nondups splits putative PCR duplicates from
	putative optical duplicates
	"""
	#initalize empty lists
	optDups = []
	pcrDups = []
	possibleOptNames = []
	
	#add bin groups and group dataframe
	dupsBin = dups.assign(bin_group = dups['titleCig'] + dups['ref'])
	dupGroup = dupsBin.groupby(['bin_group', 'start'], as_index=False)

	#if there are duplicates but all from same sample == PCR duplicate, else add group name to list
	for name, group in dupGroup:
		grouped_samples = dupGroup.get_group(name)['sampleID']
		if len(grouped_samples.unique()) == 1:
			sameSamp = dupGroup.get_group(name)['record'].reset_index()
			pcrDups.append(sameSamp['record'][0]) 
		else:
			print "---------------------"
			print "Duplicate reads in group:"
			print name, "\n"
			print "Most likely from this sample:"
			print grouped_samples.value_counts().idxmax() #most common id in group
			print "---------------------"
			possibleOptNames.append(name)
	print "Found %i possible optical duplicates..." % len(possibleOptNames)
	print "Processing"

	nit = 0
	s = "."
	for i in range(0, len(possibleOptNames)):
		print s.join(s)
		xvals = dupGroup.get_group(possibleOptNames[nit])['x'].reset_index()
		yvals = dupGroup.get_group(possibleOptNames[nit])['y'].reset_index()
		records = dupGroup.get_group(possibleOptNames[nit])['record'].reset_index()
		nit += 1
		fin = 0
		sin = 1

		for k in range(0, len(xvals)):
			xi = xvals['x'][fin]
			xj = xvals['x'][sin]
			yi = yvals['y'][fin]
			yj = yvals['y'][sin]
			if abs(int(xi)-int(xj)) > 100:
				pcrDups.append(records['record'][fin])
				fin += 1
				sin += 1
			elif abs(int(yi)-int(yj)) <= 100:
				if records['record'][fin] not in optDups:			
					optDups.append(records['record'][fin])
				if records['record'][sin] not in optDups:			
					optDups.append(records['record'][sin])
				fin += 1
				sin += 1
				break
			else:
				print "other"


	print "Complete!"
	print "Found %i PCR duplicates" % len(pcrDups)
	print "Found %i optical duplicates" % len(optDups)

	with open("pcr_duplicates.txt", "w") as pcrOut:
		for record in pcrDups:
			print >> pcrOut, record
	pcrOut.close()
	with open("optical_duplicates.txt", "w") as optOut:
		for record in optDups:
			print >> optOut, record
	optOut.close()


def read_sam_get_nondups(inputfile):
	"""Loads and extracts data from sorted sam file
	"""
	data = []
	with open(inputfile, "r") as f:
		for line in f:
			try:
				record = line.split()
				t=record[2]
			except IndexError:
				break
	
			if line.startswith("@"):
				pass
			else:
				record = line.split()
				ref = record[2]
				start = record[3]
				cigar = record[5]
				read = record[0].split(":")
				sampleID = read[0]
				title = read[4]
				x = read[5]
				y = read[6]
				titleCig = title + "_" + cigar
				data.append([titleCig, ref, start, x, y, sampleID, line])
		dfSam = DataFrame(data)

	nondupsOut = "nonduplicates.txt"

	dfSam.columns = ['titleCig', 'ref', 'start', 'x', 'y', 'sampleID', 'record']
	dfSam['count'] = dfSam.groupby('start')['start'].transform('count')

	nondups = dfSam[dfSam['count'] == 1]
	nondups.record.to_csv(nondupsOut, index=False, header=False)
	dups = dfSam[dfSam['count'] > 1]
	find_pcr_opt_dups(dups)


def main():
	"""Script reads in sam file sorted by reference start location, extracts information from each
	record and processes to find nonduplicated, PCR duplicated, and optical duplicated records. 
	Useage: python remove_duplicates.py input.sam. Output files: nonduplicates.txt,
	pcr_duplicates.txt, optical_duplicates.txt 
	"""
	inputfile = sys.argv[1]
	read_sam_get_nondups(inputfile)

main()

	
		

	
		




		
	


		

