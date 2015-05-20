## Simple program to help me double check my stats homework
## Allison Mann 9/7/12

# Introduction
print 'Central Tendencies Calculator'
print '============================='
print 'This program caculates mean, sum of squares, variance, and standard deviation'
print ' '

# Inputs
n = int(raw_input('Enter sample size (n): '))
y = float(raw_input('Enter first observation: '))
k = y**2

# Loops
for i in range(0, n-1):
    j = float(raw_input('Enter next observation: '))
    k = k+(j**2)
    y = y+j


# Calculations
##print 'y', y
##print 'k', k
ss = k - (y**2)/n
##print 'ss', ss
s2 = ss/(n-1)
##print 's2', s2
import math
s = math.sqrt(s2)

# Results
print ' '
print 'RESULTS'
print '========================='
print ' '
print 'Mean: ', round(y/n,2)
print 'Sum of squares: ', str(round(ss,1))
print 'Variance: ', str(round(s2,1))
print 'Standard deviation: ', str(round(s,1))
