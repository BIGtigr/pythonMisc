import sys
import csv

"""Function reads in a query and match file, finds matching IDs and replaces based on new key value pairs in output file. Both query and match file must be tab delimited."""

def id_match(queryfile, matchfile, outputfile):
	with open(queryfile) as file:
		contents = file.read().splitlines(True)
	split_tab = [line.partition('\t') for line in contents]
	clean_newline = [(identifier[0:], line.replace('\n', '')) for identifier, ignore, line in split_tab]
	match_dict = {identifier[0:]: line for identifier, line in clean_newline}
	
	with open(matchfile) as f:
		data = [tuple(line) for line in csv.reader(f, delimiter = '\t')]
	trans_data = zip(*data) #tranform data so each row is captured
	full_list = [x[0] for x in trans_data]
#	ids_list = full_list[1] #only second element in biom file is needed (second row of tabbed output)
#	print ids_list[1]
	for i in full_list:
		if i in match_dict:
			print i, match_dict[i]
	new_dict = {i: match_dict[i] for i in full_list if i in match_dict}
	
	infile = open(matchfile)
	outfile = open(outputfile, 'w')

	replacements = new_dict
	for line in infile:
		for src, target in replacements.iteritems():
			line = line.replace(src, target)
		outfile.write(line)
	infile.close()
	outfile.close()

#	matches = len(full_list) 
#	check = int(matches)-3 #minus three non-id strings
#	print "%s elements in query file" % matches
#	print "%s elements matched between query and match file" % check

if __name__ == '__main__':
    # Map command line arguments to function arguments.
	id_match(*sys.argv[1:])
