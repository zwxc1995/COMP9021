# Written by Xingchen Wang for COMP9021
import os
import copy
import sys
from functools import reduce
H1=[]
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
		if i==len(H1)-1:
			t=reduce(lambda x, y:str(x)+str(y),H2)
			H3.append(int(t))
	else:
		if H2!=[]:
			t=reduce(lambda x, y:str(x)+str(y),H2)
			H3.append(int(t))
			H2=[]
H4 = [H3[i:i+4] for i in range(0,len(H3),4)]
def inrectangle(m,n):
	if m[0]>=n[0] and m[0]<=n[2]:
		if m[1]>=n[1] and m[1]<=n[3]:
			return True
	return False
H13=copy.deepcopy(H4)
for i in range(0,len(H4)):
	H9=copy.deepcopy(H4)
	H9.pop(i)
	for z in range(0,len(H9)):
		H10=0
		if inrectangle([H4[i][0],H4[i][1]],H9[z])==True:
			H10+=1
		if inrectangle([H4[i][2],H4[i][1]],H9[z])==True:
			H10+=1
		if inrectangle([H4[i][2],H4[i][3]],H9[z])==True:
			H10+=1
		if inrectangle([H4[i][0],H4[i][3]],H9[z])==True:
			H10+=1
		if H10==4:
			H13[i]=[0]
H11=[]
for i in range(0,len(H13)):
	if H13[i]!=[0]:
		H11.append(H13[i])
H12=0
for i in range(0,len(H11)):
	H13=copy.deepcopy(H11)
	H13.pop(i)
	for j in range(0,H11[i][2]-H11[i][0]):
		H14=0
		for z in range(0,len(H13)):
			if inrectangle([H11[i][0]+j,H11[i][1]],H13[z])==True and inrectangle([H11[i][0]+j+1,H11[i][1]],H13[z])==True:
				H14+=1
		if H14==0:
			H12+=1		
	for x in range(0,H11[i][2]-H11[i][0]):
		H14=0
		for z in range(0,len(H13)):
			if inrectangle([H11[i][0]+x,H11[i][3]],H13[z])==True and inrectangle([H11[i][0]+x+1,H11[i][3]],H13[z])==True:
				H14+=1
		if H14==0:
			H12+=1
	for y in range(0,H11[i][3]-H11[i][1]):
		H14=0
		for z in range(0,len(H13)):
			if inrectangle([H11[i][0],H11[i][1]+y],H13[z])==True and inrectangle([H11[i][0],H11[i][1]+y+1],H13[z])==True:
				H14+=1
		if H14==0:
			H12+=1
	for m in range(0,H11[i][3]-H11[i][1]):
		H14=0
		for z in range(0,len(H13)):
			if inrectangle([H11[i][2],H11[i][1]+m],H13[z])==True and inrectangle([H11[i][2],H11[i][1]+m+1],H13[z])==True:
				H14+=1
		if H14==0:
			H12+=1
print(f'The perimeter is: {H12}')
