def validate_base_sequence(base_sequence, RNAflag):
	"""Return TRUE if the string base_sequence contains only upper- or lowercase T (or U if RNAflag), C, A, and G characters, otherwise FALSE"""
	seq = base_sequence.upper()
	return len(seq) == (seq.count('U' if RNAflag else 'T') +
		seq.count('C') + 
		seq.count('A') +
		seq.count('G'))	

def extract_matching_sequences(filename, string):
	"""From a FASTA file named filename, extract all sequences whose descriptions contain string"""
	sequences = []
	seq = ''
	with open(filename) as file:
		for line in file:
			if line[0] == '>':
				if seq:
					sequences.append(seq)
				seq = ''
				includeflag = string in line
			else:
				if includeflag:
					seq += line[:-1]
		if seq:
			sequences.append(seq)
	return sequences
