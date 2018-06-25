# Written by Xingchen Wang for COMP9021
import os
import copy
import sys
H1=[]
H3=[]
H6=[]
H7=0
x=0
filename=input('Which data file do you want to use?')
if os.path.exists(filename)==True:
	x=1
else:
    print('Incorrect input, giving up.')
    sys.exit()
with open(filename) as f:
	for line in f:
		H2=[]
		for lline in line:
			if lline is not ' ' :
				if lline is not '\n':
					H2.append(int(lline))
		H1.append(H2)
	H6.append(H1[0][0])
	H3=list(reversed(H1))
	H5=copy.deepcopy(H3)
	for i in range(1,len(H3)):
		for j in range(0,len(H3[i])):
			H3[i][j] = max(H3[i-1][j],H3[i-1][j+1])+H3[i][j]
	y = 0
	for x in range(len(H3)-2,-1,-1):
		if H3[x][y] > H3[x][y+1]:
			H6.append(H5[x][y])
		elif H3[x][y] < H3[x][y+1]:
			H6.append(H5[x][y+1])
			y+=1
		else:
			H6.append(H5[x][y])
H4=	H3[len(H3)-1][0]
H8=copy.deepcopy(H3)
for m in range(0,len(H3)):
	for n in range(0,len(H3[m])):
		H8[m][n]=1
for x in range(0,len(H3)):
	for y in range(0,len(H3[x])-1):
		if H3[x][y] == H3[x][y+1]:
			H8[x+1][y]=H8[x][y]+H8[x][y+1]
H7=H8[len(H8)-1][0]
print(f'The largest sum is: {H4}')
print(f'The number of paths yielding this sum is: {H7}')
print(f'The leftmost path yielding this sum is: {H6}')
