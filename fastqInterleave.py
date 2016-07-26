#!/usr/bin/python
"""Script takes two paired end and one singleton fastq file, interleaves the pair 1 and pair 2 matches, and concatenates the singletons to the end. Must have same number of pair 1 and pair 2 reads. Usage: python fastqInterleave.py pair1.fastq pair2.fastq singleton.fastq > interleave.fastq
"""

import sys

if __name__ == '__main__':
        try:
                pair1 = sys.argv[1]
                pair2 = sys.argv[2]
                singleton = sys.argv[3]
        except:
                print __doc__
                sys.exit(1)

        with open(pair1, "r") as p1:
                with open(pair2, "r") as p2:
                        while True:
                                line = p1.readline()
                                if line.strip() == "":
                                        break
                                print line.strip()

                                for i in xrange(3):
                                        print p1.readline().strip()
                                for i in xrange(4):
                                        print p2.readline().strip()

                        with open(singleton, "r") as se:
                                while True:
                                        line = se.readline()
                                        if line.strip() == "":
                                                break
                                        print line.strip()

                                        for i in se:
                                                print i.strip()


