import sys, csv

"""Function reads in a query and match file, finds matching IDs and replaces based on new key value pairs in output file. Both query and match file must be tab delimited. Specifically for changing ids from pc plot output from qiime"""

def id_match(queryfile, matchfile, outputfile):
	with open(queryfile) as file:
		contents = file.read().splitlines(True)
	split_tab = [line.partition('\t') for line in contents]
	clean_newline = [(identifier[0:], line.replace('\n', '')) for identifier, ignore, line in split_tab]
	match_dict = {identifier[0:]: line for identifier, line in clean_newline}
	

#this should be reassigned as own function value_replace, create new dictionary with values from matchfile
	with open(matchfile) as f:
		data = [list(line) for line in csv.reader(f, delimiter = '\t')]
#		print data
	trans_data = map(None, *data)[0]
#	print trans_data
	fixed_trans_data = trans_data[9:52] #transpose
	for i in fixed_trans_data:
		if i in match_dict:
			print i, match_dict[i]
	new_dict = {i: match_dict[i] for i in fixed_trans_data if i in match_dict}
	print new_dict


#now open output file and replace all instances of key in dictionary with value in dictionary.
	infile = open(matchfile)
	outfile = open(outputfile, 'w')

	replacements = new_dict
	for line in infile:
		for src, target in replacements.iteritems():
			line = line.replace(src, target)
		outfile.write(line)
	infile.close()
	outfile.close()

	matches = len(new_dict) 
	check = len(match_dict)
	print "%s elements in query file" % check
	print "%s elements matched between query and match file" % matches


if __name__ == '__main__':
    # Map command line arguments to function arguments.
	id_match(*sys.argv[1:])










