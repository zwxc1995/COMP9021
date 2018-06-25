# Uses National Data on the relative frequency of given names in the population of U.S. births,
# stored in a directory "names", in files named "yobxxxx.txt with xxxx being the year of birth.
#
# Prompts the user for a first name, and finds out the first year
# when this name was most popular in terms of frequency of names being given,
# as a female name and as a male name.
# 
# Written by *** and Eric Martin for COMP9021


import os


first_name = input('Enter a first name: ')
directory = 'names'
min_male_frequency = 0
male_first_year = None
min_female_frequency = 0
female_first_year = None


H1 = []
H2 = []
for filename in os.listdir(directory):
	H3 = 0
	H4 = 0
	year = str(filename)[3:7]
	if not filename.endswith('.txt'):
		continue
	with open(directory + '/' + filename) as data_file:
			for line in data_file:
				name, gender, count = line.split(',')
				if gender == 'M':
					H3 += int(count)
				else:  
					H4 += int(count)
	with open(directory + '/' + filename) as data_file:
			for line in data_file:
				name, gender, count = line.split(',')
				if name == first_name and gender == 'M':
					H5 = int(count) / H3 * 100
					H1.append((H5, year))
				if name == first_name and gender == 'F':
					H6 = int(count) / H4 * 100
					H2.append((H6, year))
if H1 != []:
	min_male_frequency = max(H1)[0]
	male_first_year = max(H1)[1]
if H2 != []:
	min_female_frequency = max(H2)[0]
	female_first_year = max(H2)[1]

if not female_first_year:
    print(f'In all years, {first_name} was never given as a female name.')
else:
    print(f'In terms of frequency, {first_name} was the most popular '
          f'as a female name first in the year {female_first_year}.\n'
          f'  It then accounted for {min_female_frequency:.2f}% of all female names.'
         )
if not male_first_year:
    print(f'In all years, {first_name} was never given as a male name.')
else:
    print(f'In terms of frequency, {first_name} was the most popular '
          f'as a male name first in the year {male_first_year}.\n'
          f'  It then accounted for {min_male_frequency:.2f}% of all male names.'
         )
