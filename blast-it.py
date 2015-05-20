##LAST UPDATE MAY 17, 2003: ALLISON E. MANN
##Copyright Allison E. Mann 2013
##This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation. This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with this program. If not, see <http://www.gnu.org/licenses/>.

print "Shotgun sequence pull from BLAST results v. 1.0"
print "====================================="
print "This program will use a Blast result file to pull wanted sequences from large fasta files"
print "====================================="
##print "Type 'help' if you are stuck"
print "To use this program you will need to know the following"
print "1. Name of the blast results file"
print "1. Name of the original fasta file"
print "====================================="
print "All files (*.py, *.txt, *fa) must be located in the same directory"
print
blastfilein = str(raw_input("Enter the file name of the blast results file: "))
fasta_file = str(raw_input("Enter the file name of the original fasta file: "))

#Pulls node names from BLAST text file
with open(blastfilein) as infile, open("wanted_seq.txt", "w") as outfile:
    collector=[]
    for line in infile:
        if line.startswith(""):
            collector = []
        collector.append(line)
        if line.startswith("Query= "):
            for outline in collector:
                outfile.write(outline)
#modifies wanted_seq file to remove Query= prefix
filein = open("wanted_seq.txt")
fileout = open("mod_wanted_seq.txt","wt")
for line in filein:
    fileout.write(line.replace("Query= ", ""))
filein.close()
fileout.close()
#pulls node names from original fasta file
from Bio import SeqIO
wanted_file = "mod_wanted_seq.txt"
result_file = "OUTFILE.fa"
wanted = set()
with open(wanted_file) as f:
    for line in f:
        line = line.strip()
        if line != "":
            wanted.add(line)

fasta_sequences = SeqIO.parse(open(fasta_file),'fasta')
with open(result_file, "w") as f:
    for seq in fasta_sequences:
        if seq.id in wanted:
            SeqIO.write([seq], f, "fasta")
