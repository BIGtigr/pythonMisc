# heterozygosity program for an infinite number of observations
# Allison Mann 9.4.12

# introduction
print 'Heterozygosity Calculator v. 1.0'
print '=========================='
print '(n/[n-1])(1-SUMpi^2)'
print '=========================='
print 'To use you will need to know the following:'
print '1. Sample size (n)'
print '2. Total number of observations (k)'
print '3. Probability or frequency of each observation (pi)'
print 

# input data
n = float(raw_input('Enter the sample size: '))
total_observations = int(raw_input('Enter the total number of observations: '))
i = float(raw_input('Enter the frequency of the first observation in decimal format: '))
i = (i**2)

# loop calculations
for observations in range (1,total_observations):
    j = float(raw_input('Frequency of next observation in decimal format: '))
    j = j**2
    i = i + j

# results of loop
print 'RESULTS'
# print 'Sum of Squares: ', str(round(i,2))
heterozygosity = (1-i)*(n/(n-1))
print 'Heterozygosity', str(round(heterozygosity,2))

### qualitive heterozygosity analysis
##if heterozygosity > .8 then:
##    print 'high heterozygosity'
## Also should have error message if heterozygosity score is in the negative or above one
