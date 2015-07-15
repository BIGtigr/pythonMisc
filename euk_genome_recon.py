#Skeleton version
import sys, os, subprocess
from Bio import SeqIO
import numpy as np


def main():
	"""BRIG genome reconstruction clone. Suitable for short fragmented reads (eg aDNA), forward and reverse."""
	if '-paired' in sys.argv:
		bowtie2_paired()
	else:
		bowtie2_single()

def bowtie2_paired():
	print "Working Directory: ", os.getcwd()
	print "\n"
	if __name__ == '__main__':
		if len(sys.argv) < 7:
			sys.exit("Error: Unacceptable number of arguments passed to script")
		else:
			pass

	ref = sys.argv[1]
	R1 = sys.argv[2]
	R2 = sys.argv[3]
	SE = sys.argv[4]
	sam_file = sys.argv[5] 
	stats_file = sys.argv[6]

	command = ('bowtie2 --no-unal -x' + ' ' + ref + ' ' + '-1' + ' ' + R1 + ' ' + '-2' + ' ' + R2 + ' ' + '-U'+ ' ' + SE)
	print "Running paired end bowtie2 mapping: ", command	
	
	with open('bowtie2_out.sam', 'w') as sam, open('bowtie2_out.stats', 'w') as stats:
		subprocess.call(command, shell=True, stdout=sam, stderr=stats)
	sam.close()
	stats.close()

	filter_hits()


def bowtie2_single():
	print "Working Directory: ", os.getcwd()
	print "\n"
	if __name__ == '__main__':
		if len(sys.argv) < 5:
			sys.exit("Error: Unacceptable number of arguments passed to script")
		else:
			pass	

	ref = sys.argv[1]
	read = sys.argv[2]
	sam_file = sys.argv[3]
	stats_file = sys.argv[4]

	command = ('bowtie2 --no-unal -x' + ' ' + ref + ' ' + '-U' + ' ' + read)
	print "Running single end bowtie2 mapping: ", command

	with open('bowtie2_out.sam', 'w') as sam, open('bowtie2_out.stats', 'w') as stats:
		subprocess.call(command, shell=True, stdout=sam, stderr=stats)
	sam.close()
	stats.close()

	filter_hits()

def filter_hits():
	with open('bowtie2_out.sam') as f:
		contents = f.read().splitlines(True)
		
		#get just hit IDs (first column of blast output)
		hits = ''
		for line in (line for line in contents if not line.startswith('@')):
			hits += line
			part_hits = hits.partition("\t")[0]
			split_hits = part_hits.splitlines()
		print "Number of sequences that mapped to the reference: ", len(split_hits)

		#filter sequences corresponding to hit IDs from original fastq files
		#NEED TO TEST THIS CHUNK
		fw_records = (i for i in SeqIO.parse(sys.argv[2], "fastq") if i.id in split_hits)
		rw_records = (i for i in SeqIO.parse(sys.argv[3], "fastq") if i.id in split_hits) 
		se_records = (i for i in SeqIO.parse(sys.argv[4], "fastq") if i.id in split_hits) 		
	

#filter_hits()

def blast_align():
	pass


def perc_ident_check():
	#check if hits after first hit are at same percent idenity, if so keep and check next if not only pull first hit
	arr = np.loadtxt('test_array.txt', delimiter='\t')
	print arr

perc_ident_check()

def gen_xml():
	#sort by start and end ranges 
	with open('BLASTOUT', 'r') as f, open ('sortedRing', 'w') as out:
		command = ("awk '{if($9>$10) print $10,$9,$3; else if($9<$10) print $9,$10,$3}'" f > out)
		print "Number of sorted reads to be mapped: %d" %d len(out)
		
		subprocess.call(command, shell=True, stdout=out)
	f.close()

	#generate feature list
	with open('sortedRing', 'r') as f, open('featurelist.xml', 'w') as feat:
		command = ("awk '{if($3>=95.0 && $3<97.0) print "<feature color=\"rgb(254,230,206)\" decoration=\"arc\"><featureRange start=\""$1"\" stop=\""$2"\" label=\""$3"\" /></feature>"; else if($3>=97.0 && $3<100.0) print "<feature color=\"rgb(253,174,107)\" decoration=\"arc\"><featureRange start=\""$1"\" stop=\""$2"\" label=\""$3"\" /></feature>"; else if($3 == 100.0) print "<feature color=\"rgb(230,85,13)\" decoration=\"arc\"><featureRange start=\""$1"\" stop=\""$2"\" label=\""$3"\" /></feature>"}' f > feat)
		subprocess.call(command, shell=True, stdout=out)
	feat.close()

	#generate full XML file

def draw_genome():
	pass ##cgviewer script (are there better options to this?

def get_consensus():
	pass

def per_base_coverage():
	pass

#main()
