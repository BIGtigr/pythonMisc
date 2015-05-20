import pprint
"""Series of functions to parse blast tabular output and assign id key to values"""

def read_blast_line(filename):
	with open(filename) as file:
		return file.read().splitlines(True) #reads file and returns list split by new lines

def read_blast_entries(filename):
	return [line.partition('\n') for line in read_blast_line(filename)] #returns output of read_blast_line as list of tuples with each line a single element

def read_blast_clean_output(filename):
	return [(identifier[0:], line.replace('\n', '')) #removes newline character from output
		for identifier, ignore, line in
		read_blast_entries(filename)]

def split_blast_fields(filename):
	return pprint.pprint([[line[0].split('\t'), line[1]] for line in read_blast_clean_output(filename)]) #splits fields separated by tab character, pretty print

#def blast_dictionary(filename):
#	return {ident[0]: line for ident, line in split_blast_fields(filename)} #dictionary comprehensions must only contain two element lists or tuples so doesn't work :(

def id_match(filename):
	with open(filename) as file:
		contents = file.read().splitlines(True)
	split_contents = [line.partition('\n') for line in contents]
	clean_contents = [(identifier[0:], line.replace('\n', '')) for identifier, ignore, line in 				  split_contents]
	return pprint.pprint([[line[0].split('\t'), line[1]] for line in clean_contents])
