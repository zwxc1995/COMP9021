 # Written by Xingchen Wang for COMP9021
import os 
import sys
from collections import defaultdict
from collections import deque
import copy

x=0
filename=input('Which data file do you want to use?')
if os.path.exists(filename)==True:
	x=1
else:
    print('Incorrect input, giving up.')
    sys.exit()
H1=[]
with open(filename) as f:
	for line in f:
		H2=[]
		for lline in line:
			if lline is not 'R' :
				if lline is not '(':
					if lline is not ')':
						if lline is not ',':
							if lline is not '\n':
								H2.append(int(lline))
		H1.append(H2)
H3=defaultdict(list)
for i in range(0,len(H1)):
	H3[H1[i][1]].append(H1[i][0])
H4=list(dict.keys(H3))
H5=[]
H6=[]
while 1:
	H5=[]
	for y in range(0,len(H4)):
		H5.append(len(H3[H4[y]]))
	for i in range(0,len(H4)):
		for j in range(0,len(H3[H4[i]])):
			if H3[H4[i]][j] not in H4:
				continue
			else:
				H3[H4[i]]+=(H3[H3[H4[i]][j]])
	for x in range(0,len(H4)):
		H3[H4[x]]=list(set(H3[H4[x]]))
	H6=[]
	for y in range(0,len(H4)):
		H6.append(len(H3[H4[y]]))
	if H5==H6:
		break
H7=[]
H8=[]
for i in range(0,len(H1)-1):
	for j in range(i+1,len(H1)):
		if H1[i][0]!=H1[j][0]:
			continue
		else:
			if H1[i][1] in H3[H1[j][1]]:
				H1[j]=[111,111]
			if H1[j][1] in H3[H1[i][1]]:
				H1[j]=[111,111]
H9=[]
H10=[]
for i in range(0,len(H1)):
	if H1[i][0]!=111:
		H9.append(H1[i][0])
	if H1[i][1]!=111:
		H10.append(H1[i][1])
print('The nonredundant facts are:')
for x in range(0,len(H9)):
	print(f'R({H9[x]},{H10[x]})')		
