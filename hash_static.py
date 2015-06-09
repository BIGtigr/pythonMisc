import sys
import csv
import os

"""Script reads in a query and match file, finds matching IDs and replaces based on new key value pairs in output file. Both query and match file must be tab delimited. Command line run: python hash_static.py queryfile matchfile outputfile column_number_of_id"""

def id_match():
	print "Working Directory: ", os.getcwd()
	if __name__ == '__main__':
		if len(sys.argv) < 4:
			print "Error!! Unacceptable number of arguments passed to script. Usage --> python hash_static.py queryfile.txt matchfile.txt outputfile.txt"
		else:
			pass

	queryfile = sys.argv[1]
	matchfile = sys.argv[2]
	outputfile = sys.argv[3]

	with open(queryfile) as file:
		contents = file.read().splitlines(True) #read in file, split by line
	split_tab = [line.partition('\t') for line in contents] #split contents by tab
	clean_newline = [(identifier[0:], line.replace('\n', '')) for identifier, ignore, line in split_tab] #clean up, remove new line characters
	match_dict = {identifier[0:]: line for identifier, line in clean_newline} #transform into dictionary	

	with open(matchfile) as f:
		data = [tuple(line) for line in csv.reader(f, delimiter = '\t')] #read in match file, split by tab
	full_list = [x[0] for x in data] #capture the first element of data (keys to match)
	print "IDs to be replaced:"
	for i in full_list:
		if i in match_dict:
			print i, match_dict[i] #if key from matchfile is same as query file print both
		else:
			if i not in match_dict:
				print i, "--> not found!"
	replacements = {i: match_dict[i] for i in full_list if i in match_dict} #new dictionary with old key and new value
	
	infile = open(matchfile)
	outfile = open(outputfile, 'w')

	for line in infile: 
		for old, new in replacements.iteritems(): #for each old and new value in replacements
			line = line.replace(old, new) #replace old key with new value
		outfile.write(line) #write each line to new file 
	infile.close()
	outfile.close()

id_match()
