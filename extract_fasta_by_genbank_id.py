"""From Model 2010, Bioinformatics Programming Using Python"""

def search_FASTA_file_by_gi_id(id, filename):
    id = str(id)
    with open(filename) as file:
        return FASTA_search_by_gi_id(id, file)

def FASTA_search_by_gi_id(id, file):
    for line in file:
        if (line[0] == ">' and
            str(id) == get_gi_id(line)):
                return \
                    read_FASTA_sequence(file)

def read_FASTA_sequence(file):
    seq = ''
    for line in file:
        if not line or line[0] == ">":
		return seq
	seq += line[:-1]

def get_gi_id(description):
	fields = description[1:].split('|')
	if fields and 'gi' in fields:
		return fields[(1 + fields.index('gi')] 
