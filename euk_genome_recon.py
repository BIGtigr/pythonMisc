#Skeleton version
import sys, os, subprocess
#import optparse

def main():
	if '-paired' in sys.argv:
		bowtie2_paired()
	else:
		bowtie2_single()

def bowtie2_paired():
	print "Working Directory: ", os.getcwd()
	if __name__ == '__main__':
		if len(sys.argv) < 7:
			print "Unacceptable number of arguments passed to script"
		else:
			pass

	ref = sys.argv[1]
	R1 = sys.argv[2]
	R2 = sys.argv[3]
	SE = sys.argv[4]
	sam_file = sys.argv[5] 
	stats_file = sys.argv[6]
	command = ('bowtie2 --no-unal -x' + ' ' + ref + ' ' + '-1' + ' ' + R1 + ' ' + '-2' + ' ' + R2 + ' ' + '-U' + SE)
	print "\n"
	print "Running paired end bowtie2 mapping: ", command	
	
	with open('bowtie2_out.sam', 'w') as sam, open('bowtie2_out.stats', 'w') as stats:
		subprocess.call(command, shell=True, stdout=sam, stderr=stats)

main()

#def bowtie2_single(reference, reads):
#	ref = reference
#	R1 = reads
#	command = pass
#	subprocess.call(command)

#def filter_hits():
#	pass

#def blast_align():
#	pass

#def gen_consensus():
#	pass

#def per_base_coverage():
#	pass

#graphics options
