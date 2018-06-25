# Written by Xingchen Wang for COMP9021
import os 
import sys
import copy
from functools import reduce
#coast_1.txt
filename=input('Which data file do you want to use?')
if os.path.exists(filename)==False:
    print('Incorrect input, giving up.')
    sys.exit()
H1=[]
H2=[]
H3=[]
with open(filename) as f:
	for line in f:
		for lline in line:
			H1.append(lline)
for i in range(0,len(H1)):
	if H1[i]!=' ' and H1[i]!='\n':
		H2.append(H1[i])
	else:
		if H2!=[]:
			t=reduce(lambda x, y:str(x)+str(y),H2)
			H3.append(int(t))
			H2=[]
H4 = [H3[i:i+2] for i in range(0,len(H3),2)]
global H5
H5=[]
def fact(n):
	if len(n)==1:
		H5.append(n[0][1])
		return
	elif len(n)==0:
		return	
	for i in range(len(n),0,-1):
		H6=0
		H7=[]
		for j in range(0,i):
			H6+=n[j][1]
			H7.append(n[j][1])
		H8=min(H7)
		if (H6-n[i-1][0]+n[0][0])/i>=H8:
			H5.append((H6-n[i-1][0]+n[0][0])/i)
			n=n[i:len(n)]
			break
	return fact(n)		
fact(H4)
H9=[]
for i in range(0,len(H5)):
	H9.append(int(H5[i]))
H10=min(H9)
print(f'The maximum quantity of fish that each town can have is {H10}.')
