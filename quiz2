# Written by *** and Eric Martin for COMP9021


'''
Prompts the user for two strictly positive integers, numerator and denominator.

Determines whether the decimal expansion of numerator / denominator is finite or infinite.

Then computes integral_part, sigma and tau such that numerator / denominator is of the form
integral_part . sigma tau tau tau ...
where integral_part in an integer, sigma and tau are (possibly empty) strings of digits,
and sigma and tau are as short as possible.
'''


import sys
from math import gcd


try:
    numerator, denominator = input('Enter two strictly positive integers: ').split()
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    numerator, denominator = int(numerator), int(denominator)
    if numerator <= 0 or denominator <= 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()


has_finite_expansion = False
integral_part = 0
sigma = ''
tau = ''

H1 = denominator / gcd(numerator,denominator)
list1=[] 
list2=[] 
list3=[]
list4=[]
num=int(H1)
tmp=int(2)  
if num != tmp:
	while (num >= tmp):
		k=num % tmp  
		if( k == 0):  
			list1.append(int(tmp))  
			num=num / tmp    
		else:  
			tmp=tmp+1 
else:
	list1.append(int(tmp))
list2=list(set(list1))
for i in range(0,len(list2)):
	if list2[i] != 2:
		list3.append(list2[i])
for i in range(0,len(list3)):
	if list3[i] != 5:
		list4.append(list3[i])
if len(list4) == 0:
	has_finite_expansion = True

integral_part = numerator//denominator

x=numerator
y=denominator
x=x%y
list5=[x]
H2=False
while (1):
	if x==0:
		break
	x*=10
	z=x//y
	sigma+=str(z)
	x=x%y
	for i in range(0,len(list5)):
		if x==list5[i]:
			tau=sigma[i:len(list5)]
			sigma=sigma[0:i]
			H2=True
	if(H2):
		break
	list5.append(x)


if has_finite_expansion:
    print(f'\n{numerator} / {denominator} has a finite expansion')
else:
    print(f'\n{numerator} / {denominator} has no finite expansion')
if not tau:
    if not sigma:
        print(f'{numerator} / {denominator} = {integral_part}')
    else:
        print(f'{numerator} / {denominator} = {integral_part}.{sigma}')
else:
    print(f'{numerator} / {denominator} = {integral_part}.{sigma}({tau})*')
