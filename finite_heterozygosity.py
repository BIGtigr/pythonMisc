# heterozygosity program for an infinite number of observations

print 'This program calculates the heterozygosity for genetic data'
n = float(raw_input('Enter the sample size: '))
total_observations = int(raw_input('Enter the total number of observations: '))
i = float(raw_input('Enter the frequency of the first observation in decimal format: '))
i = (i*i)

for observations in range (1,total_observations):
    j = float(raw_input('Frequency of next observation in decimal format: '))
    j = j*j
    i = i + j

print 'RESULTS'
print 'Sum of Squares: ', str(round(i,2))
corrected_sum_of_squares = i*(n/(n-1))
print 'Sum of Squares Corrected for Sample Size: ', str(round(corrected_sum_of_squares,2))
heterozygosity = 1-corrected_sum_of_squares
print 'Heterozygosity', str(round(heterozygosity,2))
