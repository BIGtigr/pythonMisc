import numpy as np

def perc_ident_check():
	"""Checks tablular output from blast. Keeps all hits that have the same sequence ID and equivalent percent identity. Sequence ID must be first column, percent identity third column
	Output saved as tab separated file: sorted_blast_by_perc_id.txt
	"""
	arr = np.genfromtxt('test_array.txt', delimiter="\t", dtype=None)
	i = 0
	j = 1
	row_length = arr.shape[0]
	collection = []

	for row in range(1, row_length):
		#check to see if indexed value exists, if not break loop		
		try:
			t=arr[j]
		except IndexError: 
			print "end of list"
			break
		#if sequence ids do not match skip
		if arr[i][0] != arr[j][0]:
			print "Sequence IDs do not match"
			i += 1
			j += 1
			continue
		#if sequence id's match and percent identity is the same 
		elif arr[i][2] == arr[j][2]:
			print "Rows match exactly"
			#both the first and second match append to collection
			collection.append(arr[i])
			if arr[j] not in collection:
				print "Second row matches and is not in collection"
				collection.append(arr[j])			
			i += 2
			j += 2
			continue			
		elif arr[i][2] > arr[j][2] and arr[i][0] not in collection:
			print "First row is greater than second"
			collection.append(arr[i])
			i += 2
			j += 2
			continue
		else:
			print "something is wrong"
			break
	print "Final collection contents: \n", collection
	
	np.savetxt('sorted_blast_by_perc_id.txt', collection, delimiter="\t", fmt="%s")

perc_ident_check()
