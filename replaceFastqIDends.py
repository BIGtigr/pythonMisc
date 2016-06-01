"""Adds those annoying /1 and /2 to your id file (old SRA format) before filtering your reads from your pair1 and pair2 fastq files
"""
import glob

flist = glob.glob('*ids')
for f in flist:
	inf = open(f, 'r')
	outf = open(f.replace('ids', 'fixed.ids'), 'w')
	for line in inf:
		l = line.rstrip()
		if l.endswith('/1'):
			outf.write(l + '\n')
		else:
			outf.write(l + '/1\n' + l + '/2\n')
	inf.close()
	outf.close()
