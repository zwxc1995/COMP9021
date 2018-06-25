# Insert your code here
from functools import reduce
import os
import string
from collections import defaultdict
import operator
import copy

class FriezeError(Exception):
	def __init__(self, message):
		self.message = message

class Frieze:
	def __init__(self,filename):
		self.filename=filename
		H1=[]
		H2=[]
		H3=[]
		H4=0
		H=[]
		HH=[]
		HHH=[]
		with open(filename) as f:
			for line in f:
				for lline in line:
					H1.append(lline)
					if lline!=' ' and lline!='\n':
						if lline.isdigit():
							HHH.append(lline)
					else:
						if HHH!=[]:
							t=reduce(lambda x, y:str(x)+str(y),HHH)
							H.append(int(t))
							HHH=[]
				if len(H)!=0:
					H4+=1
					HH.append(len(H))
				H=[]
		for i in range(len(H1)):
			if i==len(H1)-1 and H1[i]!='\n':
				H1.append('\n')
				HH[H4-1]+=1
		for i in range(0,len(H1)):
			if H1[i]!=' ' and H1[i]!='\n':
				if H1[i].isdigit():
					H2.append(H1[i])
			else:
				if H2!=[]:
					t=reduce(lambda x, y:str(x)+str(y),H2)
					H3.append(int(t))
					H2=[]
		H7=int(len(H3)/H4)
		self.LL = [H3[i:i+H7] for i in range(0,len(H3),H7)]
		self.LL_length=H7
		self.LL_length_length=H4
		if self.LL_length_length<3 or self.LL_length_length>17:
			raise FriezeError('Incorrect input.')
		if self.LL_length<5 or self.LL_length>51:
			raise FriezeError('Incorrect input.')
		if len(set(HH))!=1:
			raise FriezeError('Incorrect input.')
		if self.LL[0][self.LL_length-1]!=0:
			raise FriezeError('Input does not represent a frieze.')
		for i in range(1,self.LL_length_length):
			if self.LL[i][self.LL_length-1]!=0:
				if self.LL[i][self.LL_length-1]!=1:
					raise FriezeError('Input does not represent a frieze.')
		for i in range(0,self.LL_length-1):
			if self.LL[0][i]&4!=4:
					raise FriezeError('Input does not represent a frieze.')
			else:
				if self.LL[0][i]&1==1:
					raise FriezeError('Input does not represent a frieze.')
				if self.LL[0][i]&2==2:
					raise FriezeError('Input does not represent a frieze.')
		for i in range(0,self.LL_length-1):
			if self.LL[self.LL_length_length-1][i]&4!=4:
					raise FriezeError('Input does not represent a frieze.')
			else:
				if self.LL[self.LL_length_length-1][i]&8==8:
					raise FriezeError('Input does not represent a frieze.')
		for i in range(0,self.LL_length_length-1):
			for j in range(0,self.LL_length):
				if self.LL[i][j]&8==8:
					if self.LL[i+1][j]&2==2:
						raise FriezeError('Input does not represent a frieze.')
		AH=defaultdict(list)
		AHH=[]
		for m in range(self.LL_length_length):
			AH1=defaultdict(list)
			for j in range(self.LL_length):
				if j!=self.LL_length-1:
					AH1[str(self.LL[m][j])].append(j+1)
				else:
					AH1[str(self.LL[m][j])].append('E')
			AT=0
			AH11=copy.deepcopy(AH1)
			AH12=0
			yy=0
			for i in list(AH11.keys()):
				AH7=[]
				for j in range(len(AH11[i])-1):
					if AH11[i][j+1]=='E':
						AH11[i][j+1]=self.LL_length
					AH6=AH11[i][j+1]-AH11[i][j]
					AH7.append(AH6)
				AH8=list(set(AH7))
				if len(AH8)==1:
					AT=AH8[0]
					AH9=(tuple(AH1[i]))
				else:
					AH4=defaultdict(list)
					AHHHH=0
					while 1:
						for i in list(AH1.keys()):
							for j in range(len(AH1[i])):
								if AH1[i][j]!='E':
									if AH1[i][j]!=self.LL_length-1:
										AH2=str(self.LL[m][AH1[i][j]])
										AH3=i+AH2
										AH4[AH3].append(AH1[i][j]+1)
									else:
										AH2=str(self.LL[m][AH1[i][j]])
										AH3=i+AH2
										AH4[AH3].append('E')
						AH1=copy.deepcopy(AH4)
						yy+=1
						AH11=copy.deepcopy(AH4)
						AH4=defaultdict(list)
						for i in list(AH11.keys()):
							AH5=yy+1
							AH7=[]
							for j in range(len(AH11[i])-1):
								if	j==0:
									AH7.append(AH11[i][j])
								if AH11[i][j+1]=='E':
									AH11[i][j+1]=self.LL_length
								AH6=AH11[i][j+1]-AH11[i][j]
								AH7.append(AH6)
							AH8=list(set(AH7))
							if len(AH8)!=1:
								continue
							else:
								if AH5!=AH8[0]:
									continue
								else:
									AT=AH8[0]
									AHHHH=1
									AH9=(tuple(AH1[i]))
									AH12=1
						if AHHHH==1:
							break
						AH10=[]
						for i in list(AH1.keys()):
							AH10.append(len(AH1[i]))
						AH111=list(set(AH10))
						if len(AH111)==1 and AH111[0]==1:
							AH12=1
							break
					if AH12==1:
						break	
			AH[m]=(AH9)
			AHH.append(AT)
		ATsT=max(AHH)
		ATs=False
		ATT=0
		if 0 not in AHH:
			for i in range(self.LL_length_length):
				for j in range(self.LL_length_length):
					if i!=j:
						if len(list(set(AH[i])&set(AH[j])))>=(self.LL_length//max(AHH[i],AHH[j])-1):
							ATs=True
						else:
							ATT=1
							break
				if ATT==1:
					break
		self.T=ATsT
		self.Ts=ATs
		if self.Ts==False:
			raise FriezeError('Input does not represent a frieze.')
		if self.T<2:
			raise FriezeError('Input does not represent a frieze.')
		if self.LL_length%self.T!=1:
			raise FriezeError('Input does not represent a frieze.')
	def analyse(self):
		H=False
		H1=0
		if self.LL_length_length%2==0:
			for i in range(int(self.LL_length_length/2)+1):
				for j in range(self.T):
					if self.LL[i][j]==0:
						if self.LL[self.LL_length_length-i-1][j]==0 or self.LL[self.LL_length_length-i-1][j]==1:
							if self.LL[self.LL_length_length-i-1][j]==1:
								if self.LL[i+1][j]&1==1:
									continue
								else:
									H1=1
									break
						else:
							H1=1
							break
					if self.LL[i][j]==4:
						if self.LL[self.LL_length_length-i-1][j]==4 or self.LL[self.LL_length_length-i-1][j]==5:
							if self.LL[self.LL_length_length-i-1][j]==5:
								if self.LL[i+1][j]&1==1:
									continue
								else:
									H1=1
									break
						else:
							H1=1
							break
					if self.LL[i][j]==8:
						if self.LL[self.LL_length_length-i-1][j]==2 or self.LL[self.LL_length_length-i-1][j]==3:
							if self.LL[self.LL_length_length-i-1][j]==3:
								if self.LL[i+1][j]&1==1:
									continue
								else:
									H1=1
									break
						else:
							H1=1
							break
					if self.LL[i][j]==12:
						if self.LL[self.LL_length_length-i-1][j]==6 or self.LL[self.LL_length_length-i-1][j]==7:
							if self.LL[self.LL_length_length-i-1][j]==7:
								if self.LL[i+1][j]&1==1:
									continue
								else:
									H1=1
									break
						else:
							H1=1
							break
					if self.LL[i][j]==1:
						if self.LL[self.LL_length_length-i][j]&1==1:
							if self.LL[self.LL_length_length-i-1][j]==0 or self.LL[self.LL_length_length-i-1][j]==1:
								if self.LL[self.LL_length_length-i-1][j]==1:
									if self.LL[i+1][j]&1==1:
										continue
									else:
										H1=1
										break
							else:
								H1=1
								break
						else:
							H1=1
							break
					if self.LL[i][j]==5:
						if self.LL[self.LL_length_length-i][j]&1==1:
							if self.LL[self.LL_length_length-i-1][j]==4 or self.LL[self.LL_length_length-i-1][j]==5:
								if self.LL[self.LL_length_length-i-1][j]==5:
									if self.LL[i+1][j]&1==1:
										continue
									else:
										H1=1
										break
							else:
								H1=1
								break
						else:
							H1=1
							break
					if self.LL[i][j]==9:
						if self.LL[self.LL_length_length-i][j]&1==1:
							if self.LL[self.LL_length_length-i-1][j]==2 or self.LL[self.LL_length_length-i-1][j]==3:
								if self.LL[self.LL_length_length-i-1][j]==3:
									if self.LL[i+1][j]&1==1:
										continue
									else:
										H1=1
										break
							else:
								H1=1
								break
						else:
							H1=1
							break
					if self.LL[i][j]==13:
						if self.LL[self.LL_length_length-i][j]&1==1:
							if self.LL[self.LL_length_length-i-1][j]==6 or self.LL[self.LL_length_length-i-1][j]==7:
								if self.LL[self.LL_length_length-i-1][j]==7:
									if self.LL[i+1][j]&1==1:
										continue
									else:
										H1=1
										break
							else:
								H1=1
								break
						else:
							H1=1
							break
					if self.LL[i][j]==2:
						if self.LL[self.LL_length_length-i-1][j]==8 or self.LL[self.LL_length_length-i-1][j]==9:
							if self.LL[self.LL_length_length-i-1][j]==9:
								if self.LL[i+1][j]&1==1:
									continue
								else:
									H1=1
									break
						else:
							H1=1
							break
					if self.LL[i][j]==6:
						if self.LL[self.LL_length_length-i-1][j]==12 or self.LL[self.LL_length_length-i-1][j]==13:
							if self.LL[self.LL_length_length-i-1][j]==13:
								if self.LL[i+1][j]&1==1:
									continue
								else:
									H1=1
									break
						else:
							H1=1
							break
					if self.LL[i][j]==10:
						if self.LL[self.LL_length_length-i-1][j]==10 or self.LL[self.LL_length_length-i-1][j]==11:
							if self.LL[self.LL_length_length-i-1][j]==11:
								if self.LL[i+1][j]&1==1:
									continue
								else:
									H1=1
									break
						else:
							H1=1
							break
					if self.LL[i][j]==14:
						if self.LL[self.LL_length_length-i-1][j]==14 or self.LL[self.LL_length_length-i-1][j]==15:
							if self.LL[self.LL_length_length-i-1][j]==15:
								if self.LL[i+1][j]&1==1:
									continue
								else:
									H1=1
									break
						else:
							H1=1
							break
					if self.LL[i][j]==3:
						if self.LL[self.LL_length_length-i][j]&1==1:
							if self.LL[self.LL_length_length-i-1][j]==8 or self.LL[self.LL_length_length-i-1][j]==9:
								if self.LL[self.LL_length_length-i-1][j]==9:
									if self.LL[i+1][j]&1==1:
										continue
									else:
										H1=1
										break
							else:
								H1=1
								break
						else:
							H1=1
							break
					if self.LL[i][j]==7:
						if self.LL[self.LL_length_length-i][j]&1==1:
							if self.LL[self.LL_length_length-i-1][j]==12 or self.LL[self.LL_length_length-i-1][j]==13:
								if self.LL[self.LL_length_length-i-1][j]==13:
									if self.LL[i+1][j]&1==1:
										continue
									else:
										H1=1
										break
							else:
								H1=1
								break
						else:
							H1=1
							break
					if self.LL[i][j]==11:
						if self.LL[self.LL_length_length-i][j]&1==1:
							if self.LL[self.LL_length_length-i-1][j]==10 or self.LL[self.LL_length_length-i-1][j]==11:
								if self.LL[self.LL_length_length-i-1][j]==11:
									if self.LL[i+1][j]&1==1:
										continue
									else:
										H1=1
										break
							else:
								H1=1
								break
						else:
							H1=1
							break
					if self.LL[i][j]==15:
						if self.LL[self.LL_length_length-i][j]&1==1:
							if self.LL[self.LL_length_length-i-1][j]==14 or self.LL[self.LL_length_length-i-1][j]==15:
								if self.LL[self.LL_length_length-i-1][j]==15:
									if self.LL[i+1][j]&1==1:
										continue
									else:
										H1=1
										break
							else:
								H1=1
								break
						else:
							H1=1
							break
				if H1==1:
					break
			if H1==0:
				H=True
		if self.LL_length_length%2==1:
			xx=int(self.LL_length_length/2)
			Hxx=0
			ii=0
			for i in self.LL[xx]:
				if i==2 or i==3 or i==6 or i==7 or i==9 or i==9 or i==12 or i==13:
					Hxx=1
					break
				elif i==1:
					if self.LL[xx+1][ii]&1!=1:
						Hxx=1
						break
				ii+=1
			if Hxx!=1:	
				for i in range(int((self.LL_length_length-1)/2)):
					for j in range(self.T):
						if self.LL[i][j]==0:
							if self.LL[self.LL_length_length-i-1][j]==0 or self.LL[self.LL_length_length-i-1][j]==1:
								if self.LL[self.LL_length_length-i-1][j]==1:
									if self.LL[i+1][j]&1==1:
										continue
									else:
										H1=1
										break
							else:
								H1=1
								break
						if self.LL[i][j]==4:
							if self.LL[self.LL_length_length-i-1][j]==4 or self.LL[self.LL_length_length-i-1][j]==5:
								if self.LL[self.LL_length_length-i-1][j]==5:
									if self.LL[i+1][j]&1==1:
										continue
									else:
										H1=1
										break
							else:
								H1=1
								break
						if self.LL[i][j]==8:
							if self.LL[self.LL_length_length-i-1][j]==2 or self.LL[self.LL_length_length-i-1][j]==3:
								if self.LL[self.LL_length_length-i-1][j]==3:
									if self.LL[i+1][j]&1==1:
										continue
									else:
										H1=1
										break
							else:
								H1=1
								break
						if self.LL[i][j]==12:
							if self.LL[self.LL_length_length-i-1][j]==6 or self.LL[self.LL_length_length-i-1][j]==7:
								if self.LL[self.LL_length_length-i-1][j]==7:
									if self.LL[i+1][j]&1==1:
										continue
									else:
										H1=1
										break
							else:
								H1=1
								break
						if self.LL[i][j]==1:
							if self.LL[self.LL_length_length-i][j]&1==1:
								if self.LL[self.LL_length_length-i-1][j]==0 or self.LL[self.LL_length_length-i-1][j]==1:
									if self.LL[self.LL_length_length-i-1][j]==1:
										if self.LL[i+1][j]&1==1:
											continue
										else:
											H1=1
											break
								else:
									H1=1
									break
							else:
								H1=1
								break
						if self.LL[i][j]==5:
							if self.LL[self.LL_length_length-i][j]&1==1:
								if self.LL[self.LL_length_length-i-1][j]==4 or self.LL[self.LL_length_length-i-1][j]==5:
									if self.LL[self.LL_length_length-i-1][j]==5:
										if self.LL[i+1][j]&1==1:
											continue
										else:
											H1=1
											break
								else:
									H1=1
									break
							else:
								H1=1
								break
						if self.LL[i][j]==9:
							if self.LL[self.LL_length_length-i][j]&1==1:
								if self.LL[self.LL_length_length-i-1][j]==2 or self.LL[self.LL_length_length-i-1][j]==3:
									if self.LL[self.LL_length_length-i-1][j]==3:
										if self.LL[i+1][j]&1==1:
											continue
										else:
											H1=1
											break
								else:
									H1=1
									break
							else:
								H1=1
								break
						if self.LL[i][j]==13:
							if self.LL[self.LL_length_length-i][j]&1==1:
								if self.LL[self.LL_length_length-i-1][j]==6 or self.LL[self.LL_length_length-i-1][j]==7:
									if self.LL[self.LL_length_length-i-1][j]==7:
										if self.LL[i+1][j]&1==1:
											continue
										else:
											H1=1
											break
								else:
									H1=1
									break
							else:
								H1=1
								break
						if self.LL[i][j]==2:
							if self.LL[self.LL_length_length-i-1][j]==8 or self.LL[self.LL_length_length-i-1][j]==9:
								if self.LL[self.LL_length_length-i-1][j]==9:
									if self.LL[i+1][j]&1==1:
										continue
									else:
										H1=1
										break
							else:
								H1=1
								break
						if self.LL[i][j]==6:
							if self.LL[self.LL_length_length-i-1][j]==12 or self.LL[self.LL_length_length-i-1][j]==13:
								if self.LL[self.LL_length_length-i-1][j]==13:
									if self.LL[i+1][j]&1==1:
										continue
									else:
										H1=1
										break
							else:
								H1=1
								break
						if self.LL[i][j]==10:
							if self.LL[self.LL_length_length-i-1][j]==10 or self.LL[self.LL_length_length-i-1][j]==11:
								if self.LL[self.LL_length_length-i-1][j]==11:
									if self.LL[i+1][j]&1==1:
										continue
									else:
										H1=1
										break
							else:
								H1=1
								break
						if self.LL[i][j]==14:
							if self.LL[self.LL_length_length-i-1][j]==14 or self.LL[self.LL_length_length-i-1][j]==15:
								if self.LL[self.LL_length_length-i-1][j]==15:
									if self.LL[i+1][j]&1==1:
										continue
									else:
										H1=1
										break
							else:
								H1=1
								break
						if self.LL[i][j]==3:
							if self.LL[self.LL_length_length-i][j]&1==1:
								if self.LL[self.LL_length_length-i-1][j]==8 or self.LL[self.LL_length_length-i-1][j]==9:
									if self.LL[self.LL_length_length-i-1][j]==9:
										if self.LL[i+1][j]&1==1:
											continue
										else:
											H1=1
											break
								else:
									H1=1
									break
							else:
								H1=1
								break
						if self.LL[i][j]==7:
							if self.LL[self.LL_length_length-i][j]&1==1:
								if self.LL[self.LL_length_length-i-1][j]==12 or self.LL[self.LL_length_length-i-1][j]==13:
									if self.LL[self.LL_length_length-i-1][j]==13:
										if self.LL[i+1][j]&1==1:
											continue
										else:
											H1=1
											break
								else:
									H1=1
									break
							else:
								H1=1
								break
						if self.LL[i][j]==11:
							if self.LL[self.LL_length_length-i][j]&1==1:
								if self.LL[self.LL_length_length-i-1][j]==10 or self.LL[self.LL_length_length-i-1][j]==11:
									if self.LL[self.LL_length_length-i-1][j]==11:
										if self.LL[i+1][j]&1==1:
											continue
										else:
											H1=1
											break
								else:
									H1=1
									break
							else:
								H1=1
								break
						if self.LL[i][j]==15:
							if self.LL[self.LL_length_length-i][j]&1==1:
								if self.LL[self.LL_length_length-i-1][j]==14 or self.LL[self.LL_length_length-i-1][j]==15:
									if self.LL[self.LL_length_length-i-1][j]==15:
										if self.LL[i+1][j]&1==1:
											continue
										else:
											H1=1
											break
								else:
									H1=1
									break
							else:
								H1=1
								break
					if H1==1:
						break
				for i in range(int((self.LL_length_length-1)/2)):
					for j in range(self.T):
						self.LL[i][j]
						self.LL[self.LL_length_length-i-1][j]
						if self.LL[self.LL_length_length-i-1][j]==0:
							if self.LL[i][j]==0 or self.LL[i][j]==1:
								if self.LL[i][j]==1:
									if self.LL[self.LL_length_length-i][j]&1==1:
										continue
									else:
										H1=1
										break
							else:
								H1=1
								break
						if self.LL[self.LL_length_length-i-1][j]==4:
							if self.LL[i][j]==4 or self.LL[i][j]==5:
								if self.LL[i][j]==5:
									if self.LL[self.LL_length_length-i][j]&1==1:
										continue
									else:
										H1=1
										break
							else:
								H1=1
								break
						if self.LL[self.LL_length_length-i-1][j]==8:
							if self.LL[i][j]==2 or self.LL[i][j]==3:
								if self.LL[i][j]==3:
									if self.LL[self.LL_length_length-i][j]&1==1:
										continue
									else:
										H1=1
										break
							else:
								H1=1
								break
						if self.LL[self.LL_length_length-i-1][j]==12:
							if self.LL[i][j]==6 or self.LL[i][j]==7:
								if self.LL[i][j]==7:
									if self.LL[self.LL_length_length-i][j]&1==1:
										continue
									else:
										H1=1
										break
							else:
								H1=1
								break
						if self.LL[self.LL_length_length-i-1][j]==1:
							if self.LL[i+1][j]&1==1:
								if self.LL[i][j]==0 or self.LL[i][j]==1:
									if self.LL[i][j]==1:
										if self.LL[self.LL_length_length-i][j]&1==1:
											continue
										else:
											H1=1
											break
								else:
									H1=1
									break
							else:
								H1=1
								break
						if self.LL[self.LL_length_length-i-1][j]==5:
							if self.LL[i+1][j]&1==1:
								if self.LL[i][j]==4 or self.LL[i][j]==5:
									if self.LL[i][j]==5:
										if self.LL[self.LL_length_length-i][j]&1==1:
											continue
										else:
											H1=1
											break
								else:
									H1=1
									break
							else:
								H1=1
								break
						if self.LL[self.LL_length_length-i-1][j]==9:
							if self.LL[i+1][j]&1==1:
								if self.LL[i][j]==2 or self.LL[i][j]==3:
									if self.LL[i][j]==3:
										if self.LL[self.LL_length_length-i][j]&1==1:
											continue
										else:
											H1=1
											break
								else:
									H1=1
									break
							else:
								H1=1
								break
						if self.LL[self.LL_length_length-i-1][j]==13:
							if self.LL[i+1][j]&1==1:
								if self.LL[i][j]==6 or self.LL[i][j]==7:
									if self.LL[i][j]==7:
										if self.LL[self.LL_length_length-i][j]&1==1:
											continue
										else:
											H1=1
											break
								else:
									H1=1
									break
							else:
								H1=1
								break
						if self.LL[self.LL_length_length-i-1][j]==2:
							if self.LL[i][j]==8 or self.LL[i][j]==9:
								if self.LL[i][j]==9:
									if self.LL[self.LL_length_length-i][j]&1==1:
										continue
									else:
										H1=1
										break
							else:
								H1=1
								break
						if self.LL[self.LL_length_length-i-1][j]==6:
							if self.LL[i][j]==12 or self.LL[i][j]==13:
								if self.LL[i][j]==13:
									if self.LL[self.LL_length_length-i][j]&1==1:
										continue
									else:
										H1=1
										break
							else:
								H1=1
								break
						if self.LL[self.LL_length_length-i-1][j]==10:
							if self.LL[i][j]==10 or self.LL[i][j]==11:
								if self.LL[i][j]==11:
									if self.LL[self.LL_length_length-i][j]&1==1:
										continue
									else:
										H1=1
										break
							else:
								H1=1
								break
						if self.LL[self.LL_length_length-i-1][j]==14:
							if self.LL[i][j]==14 or self.LL[i][j]==15:
								if self.LL[i][j]==15:
									if self.LL[self.LL_length_length-i][j]&1==1:
										continue
									else:
										H1=1
										break
							else:
								H1=1
								break
						if self.LL[self.LL_length_length-i-1][j]==3:
							if self.LL[i+1][j]&1==1:
								if self.LL[i][j]==8 or self.LL[i][j]==9:
									if self.LL[i][j]==9:
										if self.LL[self.LL_length_length-i][j]&1==1:
											continue
										else:
											H1=1
											break
								else:
									H1=1
									break
							else:
								H1=1
								break
						if self.LL[self.LL_length_length-i-1][j]==7:
							if self.LL[i+1][j]&1==1:
								if self.LL[i][j]==12 or self.LL[i][j]==13:
									if self.LL[i][j]==13:
										if self.LL[self.LL_length_length-i][j]&1==1:
											continue
										else:
											H1=1
											break
								else:
									H1=1
									break
							else:
								H1=1
								break
						if self.LL[self.LL_length_length-i-1][j]==11:
							if self.LL[i+1][j]&1==1:
								if self.LL[i][j]==10 or self.LL[i][j]==11:
									if self.LL[i][j]==11:
										if self.LL[self.LL_length_length-i][j]&1==1:
											continue
										else:
											H1=1
											break
								else:
									H1=1
									break
							else:
								H1=1
								break
						if self.LL[self.LL_length_length-i-1][j]==15:
							if self.LL[i+1][j]&1==1:
								if self.LL[i][j]==14 or self.LL[i][j]==15:
									if self.LL[i][j]==15:
										if self.LL[self.LL_length_length-i][j]&1==1:
											continue
										else:
											H1=1
											break
								else:
									H1=1
									break
							else:
								H1=1
								break
					if H1==1:
						break
				if H1==0:
					H=True
		GH=False
		H1=0
		if self.LL_length_length%2==1 and self.T%2==0:
			for i in range(int(self.LL_length_length/2)+1):
				for j in range(self.T):
					if self.LL[i][j]==0:
						if self.LL[self.LL_length_length-i-1][j+int(self.T/2)]==0 or self.LL[self.LL_length_length-i-1][j+int(self.T/2)]==1:
							if self.LL[self.LL_length_length-i-1][j+int(self.T/2)]==1:
								if self.LL[i+1][j]&1==1:
									continue
								else:
									H1=1
									break
						else:
							H1=1
							break
					if self.LL[i][j]==4:
						if self.LL[self.LL_length_length-i-1][j+int(self.T/2)]==4 or self.LL[self.LL_length_length-i-1][j+int(self.T/2)]==5:
							if self.LL[self.LL_length_length-i-1][j+int(self.T/2)]==5:
								if self.LL[i+1][j]&1==1:
									continue
								else:
									H1=1
									break
						else:
							H1=1
							break
					if self.LL[i][j]==8:
						if self.LL[self.LL_length_length-i-1][j+int(self.T/2)]==2 or self.LL[self.LL_length_length-i-1][j+int(self.T/2)]==3:
							if self.LL[self.LL_length_length-i-1][j+int(self.T/2)]==3:
								if self.LL[i+1][j]&1==1:
									continue
								else:
									H1=1
									break
						else:
							H1=1
							break
					if self.LL[i][j]==12:
						if self.LL[self.LL_length_length-i-1][j+int(self.T/2)]==6 or self.LL[self.LL_length_length-i-1][j+int(self.T/2)]==7:
							if self.LL[self.LL_length_length-i-1][j+int(self.T/2)]==7:
								if self.LL[i+1][j]&1==1:
									continue
								else:
									H1=1
									break
						else:
							H1=1
							break
					if self.LL[i][j]==1:
						if self.LL[self.LL_length_length-i][j+int(self.T/2)]&1==1:
							if self.LL[self.LL_length_length-i-1][j+int(self.T/2)]==0 or self.LL[self.LL_length_length-i-1][j+int(self.T/2)]==1:
								if self.LL[self.LL_length_length-i-1][j+int(self.T/2)]==1:
									if self.LL[i+1][j]&1==1:
										continue
									else:
										H1=1
										break
							else:
								H1=1
								break
						else:
							H1=1
							break
					if self.LL[i][j]==5:
						if self.LL[self.LL_length_length-i][j+int(self.T/2)]&1==1:
							if self.LL[self.LL_length_length-i-1][j+int(self.T/2)]==4 or self.LL[self.LL_length_length-i-1][j+int(self.T/2)]==5:
								if self.LL[self.LL_length_length-i-1][j+int(self.T/2)]==5:
									if self.LL[i+1][j]&1==1:
										continue
									else:
										H1=1
										break
							else:
								H1=1
								break
						else:
							H1=1
							break
					if self.LL[i][j]==9:
						if self.LL[self.LL_length_length-i][j+int(self.T/2)]&1==1:
							if self.LL[self.LL_length_length-i-1][j+int(self.T/2)]==2 or self.LL[self.LL_length_length-i-1][j+int(self.T/2)]==3:
								if self.LL[self.LL_length_length-i-1][j+int(self.T/2)]==3:
									if self.LL[i+1][j]&1==1:
										continue
									else:
										H1=1
										break
							else:
								H1=1
								break
						else:
							H1=1
							break
					if self.LL[i][j]==13:
						if self.LL[self.LL_length_length-i][j+int(self.T/2)]&1==1:
							if self.LL[self.LL_length_length-i-1][j+int(self.T/2)]==6 or self.LL[self.LL_length_length-i-1][j+int(self.T/2)]==7:
								if self.LL[self.LL_length_length-i-1][j+int(self.T/2)]==7:
									if self.LL[i+1][j]&1==1:
										continue
									else:
										H1=1
										break
							else:
								H1=1
								break
						else:
							H1=1
							break
					if self.LL[i][j]==2:
						if self.LL[self.LL_length_length-i-1][j+int(self.T/2)]==8 or self.LL[self.LL_length_length-i-1][j+int(self.T/2)]==9:
							if self.LL[self.LL_length_length-i-1][j+int(self.T/2)]==9:
								if self.LL[i+1][j]&1==1:
									continue
								else:
									H1=1
									break
						else:
							H1=1
							break
					if self.LL[i][j]==6:
						if self.LL[self.LL_length_length-i-1][j+int(self.T/2)]==12 or self.LL[self.LL_length_length-i-1][j+int(self.T/2)]==13:
							if self.LL[self.LL_length_length-i-1][j+int(self.T/2)]==13:
								if self.LL[i+1][j]&1==1:
									continue
								else:
									H1=1
									break
						else:
							H1=1
							break
					if self.LL[i][j]==10:
						if self.LL[self.LL_length_length-i-1][j+int(self.T/2)]==10 or self.LL[self.LL_length_length-i-1][j+int(self.T/2)]==11:
							if self.LL[self.LL_length_length-i-1][j+int(self.T/2)]==11:
								if self.LL[i+1][j]&1==1:
									continue
								else:
									H1=1
									break
						else:
							H1=1
							break
					if self.LL[i][j]==14:
						if self.LL[self.LL_length_length-i-1][j+int(self.T/2)]==14 or self.LL[self.LL_length_length-i-1][j+int(self.T/2)]==15:
							if self.LL[self.LL_length_length-i-1][j+int(self.T/2)]==15:
								if self.LL[i+1][j]&1==1:
									continue
								else:
									H1=1
									break
						else:
							H1=1
							break
					if self.LL[i][j]==3:
						if self.LL[self.LL_length_length-i][j+int(self.T/2)]&1==1:
							if self.LL[self.LL_length_length-i-1][j+int(self.T/2)]==8 or self.LL[self.LL_length_length-i-1][j+int(self.T/2)]==9:
								if self.LL[self.LL_length_length-i-1][j+int(self.T/2)]==9:
									if self.LL[i+1][j]&1==1:
										continue
									else:
										H1=1
										break
							else:
								H1=1
								break
						else:
							H1=1
							break
					if self.LL[i][j]==7:
						if self.LL[self.LL_length_length-i][j+int(self.T/2)]&1==1:
							if self.LL[self.LL_length_length-i-1][j+int(self.T/2)]==12 or self.LL[self.LL_length_length-i-1][j+int(self.T/2)]==13:
								if self.LL[self.LL_length_length-i-1][j+int(self.T/2)]==13:
									if self.LL[i+1][j]&1==1:
										continue
									else:
										H1=1
										break
							else:
								H1=1
								break
						else:
							H1=1
							break
					if self.LL[i][j]==11:
						if self.LL[self.LL_length_length-i][j+int(self.T/2)]&1==1:
							if self.LL[self.LL_length_length-i-1][j+int(self.T/2)]==10 or self.LL[self.LL_length_length-i-1][j+int(self.T/2)]==11:
								if self.LL[self.LL_length_length-i-1][j+int(self.T/2)]==11:
									if self.LL[i+1][j]&1==1:
										continue
									else:
										H1=1
										break
							else:
								H1=1
								break
						else:
							H1=1
							break
					if self.LL[i][j]==15:
						if self.LL[self.LL_length_length-i][j+int(self.T/2)]&1==1:
							if self.LL[self.LL_length_length-i-1][j+int(self.T/2)]==14 or self.LL[self.LL_length_length-i-1][j+int(self.T/2)]==15:
								if self.LL[self.LL_length_length-i-1][j+int(self.T/2)]==15:
									if self.LL[i+1][j]&1==1:
										continue
									else:
										H1=1
										break
							else:
								H1=1
								break
						else:
							H1=1
							break
				if H1==1:
					break
			if H1==0:
				GH=True
		if self.LL_length_length%2==0 and self.T%2==0:
			for i in range(int((self.LL_length_length-1)/2)):
				for j in range(self.T):
					if self.LL[i][j]==0:
						if self.LL[self.LL_length_length-i-1][j+int(self.T/2)]==0 or self.LL[self.LL_length_length-i-1][j+int(self.T/2)]==1:
							if self.LL[self.LL_length_length-i-1][j+int(self.T/2)]==1:
								if self.LL[i+1][j]&1==1:
									continue
								else:
									H1=1
									break
						else:
							H1=1
							break
					if self.LL[i][j]==4:
						if self.LL[self.LL_length_length-i-1][j+int(self.T/2)]==4 or self.LL[self.LL_length_length-i-1][j+int(self.T/2)]==5:
							if self.LL[self.LL_length_length-i-1][j+int(self.T/2)]==5:
								if self.LL[i+1][j]&1==1:
									continue
								else:
									H1=1
									break
						else:
							H1=1
							break
					if self.LL[i][j]==8:
						if self.LL[self.LL_length_length-i-1][j+int(self.T/2)]==2 or self.LL[self.LL_length_length-i-1][j+int(self.T/2)]==3:
							if self.LL[self.LL_length_length-i-1][j+int(self.T/2)]==3:
								if self.LL[i+1][j]&1==1:
									continue
								else:
									H1=1
									break
						else:
							H1=1
							break
					if self.LL[i][j]==12:
						if self.LL[self.LL_length_length-i-1][j+int(self.T/2)]==6 or self.LL[self.LL_length_length-i-1][j+int(self.T/2)]==7:
							if self.LL[self.LL_length_length-i-1][j+int(self.T/2)]==7:
								if self.LL[i+1][j]&1==1:
									continue
								else:
									H1=1
									break
						else:
							H1=1
							break
					if self.LL[i][j]==1:
						if self.LL[self.LL_length_length-i][j+int(self.T/2)]&1==1:
							if self.LL[self.LL_length_length-i-1][j+int(self.T/2)]==0 or self.LL[self.LL_length_length-i-1][j+int(self.T/2)]==1:
								if self.LL[self.LL_length_length-i-1][j+int(self.T/2)]==1:
									if self.LL[i+1][j]&1==1:
										continue
									else:
										H1=1
										break
							else:
								H1=1
								break
						else:
							H1=1
							break
					if self.LL[i][j]==5:
						if self.LL[self.LL_length_length-i][j+int(self.T/2)]&1==1:
							if self.LL[self.LL_length_length-i-1][j+int(self.T/2)]==4 or self.LL[self.LL_length_length-i-1][j+int(self.T/2)]==5:
								if self.LL[self.LL_length_length-i-1][j+int(self.T/2)]==5:
									if self.LL[i+1][j]&1==1:
										continue
									else:
										H1=1
										break
							else:
								H1=1
								break
						else:
							H1=1
							break
					if self.LL[i][j]==9:
						if self.LL[self.LL_length_length-i][j+int(self.T/2)]&1==1:
							if self.LL[self.LL_length_length-i-1][j+int(self.T/2)]==2 or self.LL[self.LL_length_length-i-1][j+int(self.T/2)]==3:
								if self.LL[self.LL_length_length-i-1][j+int(self.T/2)]==3:
									if self.LL[i+1][j]&1==1:
										continue
									else:
										H1=1
										break
							else:
								H1=1
								break
						else:
							H1=1
							break
					if self.LL[i][j]==13:
						if self.LL[self.LL_length_length-i][j+int(self.T/2)]&1==1:
							if self.LL[self.LL_length_length-i-1][j+int(self.T/2)]==6 or self.LL[self.LL_length_length-i-1][j+int(self.T/2)]==7:
								if self.LL[self.LL_length_length-i-1][j+int(self.T/2)]==7:
									if self.LL[i+1][j]&1==1:
										continue
									else:
										H1=1
										break
							else:
								H1=1
								break
						else:
							H1=1
							break
					if self.LL[i][j]==2:
						if self.LL[self.LL_length_length-i-1][j+int(self.T/2)]==8 or self.LL[self.LL_length_length-i-1][j+int(self.T/2)]==9:
							if self.LL[self.LL_length_length-i-1][j+int(self.T/2)]==9:
								if self.LL[i+1][j]&1==1:
									continue
								else:
									H1=1
									break
						else:
							H1=1
							break
					if self.LL[i][j]==6:
						if self.LL[self.LL_length_length-i-1][j+int(self.T/2)]==12 or self.LL[self.LL_length_length-i-1][j+int(self.T/2)]==13:
							if self.LL[self.LL_length_length-i-1][j+int(self.T/2)]==13:
								if self.LL[i+1][j]&1==1:
									continue
								else:
									H1=1
									break
						else:
							H1=1
							break
					if self.LL[i][j]==10:
						if self.LL[self.LL_length_length-i-1][j+int(self.T/2)]==10 or self.LL[self.LL_length_length-i-1][j+int(self.T/2)]==11:
							if self.LL[self.LL_length_length-i-1][j+int(self.T/2)]==11:
								if self.LL[i+1][j]&1==1:
									continue
								else:
									H1=1
									break
						else:
							H1=1
							break
					if self.LL[i][j]==14:
						if self.LL[self.LL_length_length-i-1][j+int(self.T/2)]==14 or self.LL[self.LL_length_length-i-1][j+int(self.T/2)]==15:
							if self.LL[self.LL_length_length-i-1][j+int(self.T/2)]==15:
								if self.LL[i+1][j]&1==1:
									continue
								else:
									H1=1
									break
						else:
							H1=1
							break
					if self.LL[i][j]==3:
						if self.LL[self.LL_length_length-i][j+int(self.T/2)]&1==1:
							if self.LL[self.LL_length_length-i-1][j+int(self.T/2)]==8 or self.LL[self.LL_length_length-i-1][j+int(self.T/2)]==9:
								if self.LL[self.LL_length_length-i-1][j+int(self.T/2)]==9:
									if self.LL[i+1][j]&1==1:
										continue
									else:
										H1=1
										break
							else:
								H1=1
								break
						else:
							H1=1
							break
					if self.LL[i][j]==7:
						if self.LL[self.LL_length_length-i][j+int(self.T/2)]&1==1:
							if self.LL[self.LL_length_length-i-1][j+int(self.T/2)]==12 or self.LL[self.LL_length_length-i-1][j+int(self.T/2)]==13:
								if self.LL[self.LL_length_length-i-1][j+int(self.T/2)]==13:
									if self.LL[i+1][j]&1==1:
										continue
									else:
										H1=1
										break
							else:
								H1=1
								break
						else:
							H1=1
							break
					if self.LL[i][j]==11:
						if self.LL[self.LL_length_length-i][j+int(self.T/2)]&1==1:
							if self.LL[self.LL_length_length-i-1][j+int(self.T/2)]==10 or self.LL[self.LL_length_length-i-1][j+int(self.T/2)]==11:
								if self.LL[self.LL_length_length-i-1][j+int(self.T/2)]==11:
									if self.LL[i+1][j]&1==1:
										continue
									else:
										H1=1
										break
							else:
								H1=1
								break
						else:
							H1=1
							break
					if self.LL[i][j]==15:
						if self.LL[self.LL_length_length-i][j+int(self.T/2)]&1==1:
							if self.LL[self.LL_length_length-i-1][j+int(self.T/2)]==14 or self.LL[self.LL_length_length-i-1][j+int(self.T/2)]==15:
								if self.LL[self.LL_length_length-i-1][j+int(self.T/2)]==15:
									if self.LL[i+1][j]&1==1:
										continue
									else:
										H1=1
										break
							else:
								H1=1
								break
						else:
							H1=1
							break
				if H1==1:
					break
			if H1==0:
				GH=True
		V=False
		i=int(self.T/2)
		while i<self.T:
			H1=0
			m=int(i//1)
			n=i%1
			if n==0.0:
				r=m
				for x in range(self.LL_length_length):
					for j in range(r+1):
						if self.LL[x][j]==0:
							if self.LL[x][2*r-j]&1==1:
								H1=1
								break
						if self.LL[x][j]==4:
							if self.LL[x][2*r-j-1]&4!=4:
								H1=1
								break
						if self.LL[x][j]==8:
							if self.LL[x+1][2*r-j-1]&2!=2:
								H1=1
								break 		
						if self.LL[x][j]==12:
							if self.LL[x+1][2*r-j-1]&2!=2:
								H1=1
								break	
							if self.LL[x][2*r-j-1]&4!=4:
								H1=1
								break
						if self.LL[x][j]==1:
							if self.LL[x][2*r-j]&1!=1:
								H1=1
								break
						if self.LL[x][j]==5:
							if self.LL[x][2*r-j]&1!=1:
								H1=1
								break	
							if self.LL[x][2*r-j-1]&4!=4:
								H1=1
								break	
						if self.LL[x][j]==9:
							if self.LL[x][2*r-j]&1!=1:
								H1=1
								break	
							if self.LL[x+1][2*r-j-1]&2!=2:
								H1=1
								break	
						if self.LL[x][j]==13:
							if self.LL[x][2*r-j]&1!=1:
								H1=1
								break	
							if self.LL[x+1][2*r-j-1]&2!=2:
								H1=1
								break
							if self.LL[x][2*r-j-1]&4!=4:
								H1=1
								break
						if self.LL[x][j]==2:
							if self.LL[x-1][2*r-j-1]&8!=8:
								H1=1
								break
						if self.LL[x][j]==6:
							if self.LL[x-1][2*r-j-1]&8!=8:
								H1=1
								break		
							if self.LL[x][2*r-j-1]&4!=4:
								H1=1
								break
						if self.LL[x][j]==10:
							if self.LL[x-1][2*r-j-1]&8!=8:
								H1=1
								break		
							if self.LL[x+1][2*r-j-1]&2!=2:
								H1=1
								break		
						if self.LL[x][j]==14:
							if self.LL[x-1][2*r-j-1]&8!=8:
								H1=1
								break		
							if self.LL[x+1][2*r-j-1]&2!=2:
								H1=1
								break		
							if self.LL[x][2*r-j-1]&4!=4:
								H1=1
								break
						if self.LL[x][j]==3:
							if self.LL[x-1][2*r-j-1]&8!=8:
								H1=1
								break		
							if self.LL[x][2*r-j]&1!=1:
								H1=1
								break
						if self.LL[x][j]==7:
							if self.LL[x-1][2*r-j-1]&8!=8:
								H1=1
								break		
							if self.LL[x][2*r-j]&1!=1:
								H1=1
								break
							if self.LL[x][2*r-j-1]&4!=4:
								H1=1
								break
						if self.LL[x][j]==11:
							if self.LL[x-1][2*r-j-1]&8!=8:
								H1=1
								break		
							if self.LL[x][2*r-j]&1!=1:
								H1=1
								break
							if self.LL[x+1][2*r-j-1]&2!=2:
								H1=1
								break
						if self.LL[x][j]==15:
							if self.LL[x-1][2*r-j-1]&8!=8:
								H1=1
								break		
							if self.LL[x][2*r-j]&1!=1:
								H1=1
								break
							if self.LL[x+1][2*r-j-1]&2!=2:
								H1=1
								break
							if self.LL[x][2*r-j-1]&4!=4:
								H1=1
								break
					if H1==1:
						break
				for x in range(self.LL_length_length):
					for j in range(1,r+1):
						if self.LL[x][2*r-j]==0:
							if self.LL[x][j]&1==1:
								H1=1
								break
						if self.LL[x][2*r-j]==4:
							if self.LL[x][j-1]&4!=4:
								H1=1
								break
						if self.LL[x][2*r-j]==8:
							if self.LL[x+1][j-1]&2!=2:
								H1=1
								break 	
						if self.LL[x][2*r-j]==12:
							if self.LL[x+1][j-1]&2!=2:
								H1=1
								break	
							if self.LL[x][j-1]&4!=4:
								H1=1
								break
						if self.LL[x][2*r-j]==1:
							if self.LL[x][j]&1!=1:
								H1=1
								break
						if self.LL[x][2*r-j]==5:
							if self.LL[x][j]&1!=1:
								H1=1
								break	
							if self.LL[x][j-1]&4!=4:
								H1=1
								break	
						if self.LL[x][2*r-j]==9:
							if self.LL[x][j]&1!=1:
								H1=1
								break	
							if self.LL[x+1][j-1]&2!=2:
								H1=1
								break	
						if self.LL[x][2*r-j]==13:
							if self.LL[x][j]&1!=1:
								H1=1
								break	
							if self.LL[x+1][j-1]&2!=2:
								H1=1
								break
							if self.LL[x][j-1]&4!=4:
								H1=1
								break
						if self.LL[x][2*r-j]==2:
							if self.LL[x-1][j-1]&8!=8:
								H1=1
								break
						if self.LL[x][2*r-j]==6:
							if self.LL[x-1][j-1]&8!=8:
								H1=1
								break		
							if self.LL[x][j-1]&4!=4:
								H1=1
								break
						if self.LL[x][2*r-j]==10:
							if self.LL[x-1][j-1]&8!=8:
								H1=1
								break		
							if self.LL[x+1][j-1]&2!=2:
								H1=1
								break		
						if self.LL[x][2*r-j]==14:
							if self.LL[x-1][j-1]&8!=8:
								H1=1
								break		
							if self.LL[x+1][j-1]&2!=2:
								H1=1
								break		
							if self.LL[x][j-1]&4!=4:
								H1=1
								break
						if self.LL[x][2*r-j]==3:
							if self.LL[x-1][j-1]&8!=8:
								H1=1
								break		
							if self.LL[x][j]&1!=1:
								H1=1
								break
						if self.LL[x][2*r-j]==7:
							if self.LL[x-1][j-1]&8!=8:
								H1=1
								break		
							if self.LL[x][j]&1!=1:
								H1=1
								break
							if self.LL[x][j-1]&4!=4:
								H1=1
								break
						if self.LL[x][2*r-j]==11:
							if self.LL[x-1][j-1]&8!=8:
								H1=1
								break		
							if self.LL[x][j]&1!=1:
								H1=1
								break
							if self.LL[x+1][j-1]&2!=2:
								H1=1
								break
						if self.LL[x][2*r-j]==15:
							if self.LL[x-1][j-1]&8!=8:
								H1=1
								break		
							if self.LL[x][j]&1!=1:
								H1=1
								break
							if self.LL[x+1][j-1]&2!=2:
								H1=1
								break
							if self.LL[x][j-1]&4!=4:
								H1=1
								break
					if H1==1:
						break		
			else:
				r=int(2*(m+n))
				for x in range(self.LL_length_length):
					for j in range(m+1):
						if self.LL[x][j]==0:
							if self.LL[x][r-j]&1==1:
								H1=1
								break
						if self.LL[x][j]==4:
							if self.LL[x][r-j-1]&4!=4:
								H1=1
								break
						if self.LL[x][j]==8:
							if self.LL[x+1][r-j-1]&2!=2:
								H1=1
								break 		
						if self.LL[x][j]==12:
							if self.LL[x+1][r-j-1]&2!=2:
								H1=1
								break	
							if self.LL[x][r-j-1]&4!=4:
								H1=1
								break
						if self.LL[x][j]==1:
							if self.LL[x][r-j]&1!=1:
								H1=1
								break
						if self.LL[x][j]==5:
							if self.LL[x][r-j]&1!=1:
								H1=1
								break	
							if self.LL[x][r-j-1]&4!=4:
								H1=1
								break	
						if self.LL[x][j]==9:
							if self.LL[x][r-j]&1!=1:
								H1=1
								break	
							if self.LL[x+1][r-j-1]&2!=2:
								H1=1
								break	
						if self.LL[x][j]==13:
							if self.LL[x][r-j]&1!=1:
								H1=1
								break	
							if self.LL[x+1][r-j-1]&2!=2:
								H1=1
								break
							if self.LL[x][r-j-1]&4!=4:
								H1=1
								break
						if self.LL[x][j]==2:
							if self.LL[x-1][r-j-1]&8!=8:
								H1=1
								break
						if self.LL[x][j]==6:
							if self.LL[x-1][r-j-1]&8!=8:
								H1=1
								break		
							if self.LL[x][r-j-1]&4!=4:
								H1=1
								break
						if self.LL[x][j]==10:
							if self.LL[x-1][r-j-1]&8!=8:
								H1=1
								break		
							if self.LL[x+1][r-j-1]&2!=2:
								H1=1
								break		
						if self.LL[x][j]==14:
							if self.LL[x-1][r-j-1]&8!=8:
								H1=1
								break		
							if self.LL[x+1][r-j-1]&2!=2:
								H1=1
								break		
							if self.LL[x][r-j-1]&4!=4:
								H1=1
								break
						if self.LL[x][j]==3:
							if self.LL[x-1][r-j-1]&8!=8:
								H1=1
								break		
							if self.LL[x][r-j]&1!=1:
								H1=1
								break
						if self.LL[x][j]==7:
							if self.LL[x-1][r-j-1]&8!=8:
								H1=1
								break		
							if self.LL[x][r-j]&1!=1:
								H1=1
								break
							if self.LL[x][r-j-1]&4!=4:
								H1=1
								break
						if self.LL[x][j]==11:
							if self.LL[x-1][r-j-1]&8!=8:
								H1=1
								break		
							if self.LL[x][r-j]&1!=1:
								H1=1
								break
							if self.LL[x+1][r-j-1]&2!=2:
								H1=1
								break
						if self.LL[x][j]==15:
							if self.LL[x-1][r-j-1]&8!=8:
								H1=1
								break		
							if self.LL[x][r-j]&1!=1:
								H1=1
								break
							if self.LL[x+1][r-j-1]&2!=2:
								H1=1
								break
							if self.LL[x][r-j-1]&4!=4:
								H1=1
								break
					if H1==1:
						break
				for x in range(self.LL_length_length):
					for j in range(1,m+1):
						if self.LL[x][r-j]==0:
							if self.LL[x][j]&1==1:
								H1=1
								break
						if self.LL[x][r-j]==4:
							if self.LL[x][j-1]&4!=4:
								H1=1
								break
						if self.LL[x][r-j]==8:
							if self.LL[x+1][j-1]&2!=2:
								H1=1
								break 	
						if self.LL[x][r-j]==12:
							if self.LL[x+1][j-1]&2!=2:
								H1=1
								break	
							if self.LL[x][j-1]&4!=4:
								H1=1
								break
						if self.LL[x][r-j]==1:
							if self.LL[x][j]&1!=1:
								H1=1
								break
						if self.LL[x][r-j]==5:
							if self.LL[x][j]&1!=1:
								H1=1
								break	
							if self.LL[x][j-1]&4!=4:
								H1=1
								break	
						if self.LL[x][r-j]==9:
							if self.LL[x][j]&1!=1:
								H1=1
								break	
							if self.LL[x+1][j-1]&2!=2:
								H1=1
								break	
						if self.LL[x][r-j]==13:
							if self.LL[x][j]&1!=1:
								H1=1
								break	
							if self.LL[x+1][j-1]&2!=2:
								H1=1
								break
							if self.LL[x][j-1]&4!=4:
								H1=1
								break
						if self.LL[x][r-j]==2:
							if self.LL[x-1][j-1]&8!=8:
								H1=1
								break
						if self.LL[x][r-j]==6:
							if self.LL[x-1][j-1]&8!=8:
								H1=1
								break		
							if self.LL[x][j-1]&4!=4:
								H1=1
								break
						if self.LL[x][r-j]==10:
							if self.LL[x-1][j-1]&8!=8:
								H1=1
								break		
							if self.LL[x+1][j-1]&2!=2:
								H1=1
								break		
						if self.LL[x][r-j]==14:
							if self.LL[x-1][j-1]&8!=8:
								H1=1
								break		
							if self.LL[x+1][j-1]&2!=2:
								H1=1
								break		
							if self.LL[x][j-1]&4!=4:
								H1=1
								break
						if self.LL[x][r-j]==3:
							if self.LL[x-1][j-1]&8!=8:
								H1=1
								break		
							if self.LL[x][j]&1!=1:
								H1=1
								break
						if self.LL[x][r-j]==7:
							if self.LL[x-1][j-1]&8!=8:
								H1=1
								break		
							if self.LL[x][j]&1!=1:
								H1=1
								break
							if self.LL[x][j-1]&4!=4:
								H1=1
								break
						if self.LL[x][r-j]==11:
							if self.LL[x-1][j-1]&8!=8:
								H1=1
								break		
							if self.LL[x][j]&1!=1:
								H1=1
								break
							if self.LL[x+1][j-1]&2!=2:
								H1=1
								break
						if self.LL[x][r-j]==15:
							if self.LL[x-1][j-1]&8!=8:
								H1=1
								break		
							if self.LL[x][j]&1!=1:
								H1=1
								break
							if self.LL[x+1][j-1]&2!=2:
								H1=1
								break
							if self.LL[x][j-1]&4!=4:
								H1=1
								break
					if H1==1:
						break
			if H1==0:
				break
			i+=0.5
		if H1==0:
			V=True		
		if V==True and H==True:
			R=True
		elif V==True and GH==True:
			R=True
		else:
			R=False
			i=int(self.T/2)
			if self.LL_length_length%2==0:
				rr=int(self.LL_length_length-1)
				while i<self.T:
					H1=0
					m=int(i//1)
					n=i%1
					if n==0.0:
						r=m
						for x in range(self.LL_length_length):
							for j in range(r+1):
								if self.LL[x][j]==0:
									if self.LL[rr-x+1][2*r-j]&1==1:
										H1=1
										break
								if self.LL[x][j]==4:
									if self.LL[rr-x][2*r-j-1]&4!=4:
										H1=1
										break
								if self.LL[x][j]==8:
									if self.LL[rr-x-1][2*r-j-1]&8!=8:
										H1=1
										break
								if self.LL[x][j]==12:
									if self.LL[rr-x][2*r-j-1]&4!=4:
										H1=1
										break	
									if self.LL[rr-x-1][2*r-j-1]&8!=8:
										H1=1
										break
								if self.LL[x][j]==1:
									if self.LL[rr-x+1][2*r-j]&1!=1:
										H1=1
										break
								if self.LL[x][j]==5:
									if self.LL[rr-x+1][2*r-j]&1!=1:
										H1=1
										break	
									if self.LL[rr-x][2*r-j-1]&4!=4:
										H1=1
										break	
								if self.LL[x][j]==9:
									if self.LL[rr-x+1][2*r-j]&1!=1:
										H1=1
										break	
									if self.LL[rr-x-1][2*r-j-1]&8!=8:
										H1=1
										break	
								if self.LL[x][j]==13:
									if self.LL[rr-x+1][2*r-j]&1!=1:
										H1=1
										break	
									if self.LL[rr-x-1][2*r-j-1]&8!=8:
										H1=1
										break
									if self.LL[rr-x][2*r-j-1]&4!=4:
										H1=1
										break
								if self.LL[x][j]==2:
									if self.LL[rr-x+1][2*r-j-1]&2!=2:
										H1=1
										break
								if self.LL[x][j]==6:
									if self.LL[rr-x+1][2*r-j-1]&2!=2:
										H1=1
										break		
									if self.LL[rr-x][2*r-j-1]&4!=4:
										H1=1
										break
								if self.LL[x][j]==10:
									if self.LL[rr-x+1][2*r-j-1]&2!=2:
										H1=1
										break		
									if self.LL[rr-x-1][2*r-j-1]&8!=8:
										H1=1
										break		
								if self.LL[x][j]==14:
									if self.LL[rr-x-1][2*r-j-1]&8!=8:
										H1=1
										break		
									if self.LL[rr-x+1][2*r-j-1]&2!=2:
										H1=1
										break		
									if self.LL[rr-x][2*r-j-1]&4!=4:
										H1=1
										break
								if self.LL[x][j]==3:
									if self.LL[rr-x+1][2*r-j-1]&2!=2:
										H1=1
										break		
									if self.LL[rr-x+1][2*r-j]&1!=1:
										H1=1
										break
								if self.LL[x][j]==7:
									if self.LL[rr-x+1][2*r-j]&1!=1:
										H1=1
										break		
									if self.LL[rr-x][2*r-j-1]&4!=4:
										H1=1
										break
									if self.LL[rr-x+1][2*r-j-1]&2!=2:
										H1=1
										break
								if self.LL[x][j]==11:
									if self.LL[rr-x+1][2*r-j]&1!=1:
										H1=1
										break		
									if self.LL[rr-x-1][2*r-j-1]&8!=8:
										H1=1
										break
									if self.LL[rr-x+1][2*r-j-1]&2!=2:
										H1=1
										break
								if self.LL[x][j]==15:
									if self.LL[rr-x-1][2*r-j-1]&8!=8:
										H1=1
										break		
									if self.LL[rr-x][2*r-j-1]&4!=4:
										H1=1
										break
									if self.LL[rr-x+1][2*r-j]&1!=1:
										H1=1
										break
									if self.LL[rr-x+1][2*r-j-1]&2!=2:
										H1=1
										break
							if H1==1:
								break
						for x in range(self.LL_length_length):
							for j in range(1,r+1):
								if self.LL[rr-x][2*r-j]==0:
									if self.LL[x+1][j]&1==1:
										H1=1
										break
								if self.LL[rr-x][2*r-j]==4:
									if self.LL[x][j-1]&4!=4:
										H1=1
										break
								if self.LL[rr-x][2*r-j]==8:
									if self.LL[x-1][j-1]&8!=8:
										H1=1
										break 		
								if self.LL[rr-x][2*r-j]==12:
									if self.LL[x][j-1]&4!=4:
										H1=1
										break	
									if self.LL[x-1][j-1]&8!=8:
										H1=1
										break
								if self.LL[rr-x][2*r-j]==1:
									if self.LL[x+1][j]&1!=1:
										H1=1
										break
								if self.LL[rr-x][2*r-j]==5:
									if self.LL[x+1][j]&1!=1:
										H1=1
										break	
									if self.LL[x][j-1]&4!=4:
										H1=1
										break	
								if self.LL[rr-x][2*r-j]==9:
									if self.LL[x+1][j]&1!=1:
										H1=1
										break	
									if self.LL[x-1][j-1]&8!=8:
										H1=1
										break	
								if self.LL[rr-x][2*r-j]==13:
									if self.LL[x+1][j]&1!=1:
										H1=1
										break	
									if self.LL[x-1][j-1]&8!=8:
										H1=1
										break
									if self.LL[x][j-1]&4!=4:
										H1=1
										break
								if self.LL[rr-x][2*r-j]==2:
									if self.LL[x+1][j-1]&2!=2:
										H1=1
										break
								if self.LL[rr-x][2*r-j]==6:
									if self.LL[x+1][j-1]&2!=2:
										H1=1
										break		
									if self.LL[x][j-1]&4!=4:
										H1=1
										break
								if self.LL[rr-x][2*r-j]==10:
									if self.LL[x+1][j-1]&2!=2:
										H1=1
										break		
									if self.LL[x-1][j-1]&8!=8:
										H1=1
										break		
								if self.LL[rr-x][2*r-j]==14:
									if self.LL[x-1][j-1]&8!=8:
										H1=1
										break		
									if self.LL[x+1][j-1]&2!=2:
										H1=1
										break		
									if self.LL[x][j-1]&4!=4:
										H1=1
										break
								if self.LL[rr-x][2*r-j]==3:
									if self.LL[x+1][j-1]&2!=2:
										H1=1
										break		
									if self.LL[x+1][j]&1!=1:
										H1=1
										break
								if self.LL[rr-x][2*r-j]==7:
									if self.LL[x+1][j]&1!=1:
										H1=1
										break		
									if self.LL[x][j-1]&4!=4:
										H1=1
										break
									if self.LL[x+1][j-1]&2!=2:
										H1=1
										break
								if self.LL[rr-x][2*r-j]==11:
									if self.LL[x+1][j]&1!=1:
										H1=1
										break		
									if self.LL[x-1][j-1]&8!=8:
										H1=1
										break
									if self.LL[x+1][j-1]&2!=2:
										H1=1
										break
								if self.LL[rr-x][2*r-j]==15:
									if self.LL[x-1][j-1]&8!=8:
										H1=1
										break		
									if self.LL[x][j-1]&4!=4:
										H1=1
										break
									if self.LL[x+1][j]&1!=1:
										H1=1
										break
									if self.LL[x+1][j-1]&2!=2:
										H1=1
										break
							if H1==1:
								break		
					else:
						r=int(2*(m+n))
						for x in range(self.LL_length_length):
							for j in range(m+1):
								if self.LL[x][j]==0:
									if self.LL[rr-x+1][r-j]&1==1:
										H1=1
										break
								if self.LL[x][j]==4:
									if self.LL[rr-x][r-j-1]&4!=4:
										H1=1
										break
								if self.LL[x][j]==8:
									if self.LL[rr-x-1][r-j-1]&8!=8:
										H1=1
										break 		
								if self.LL[x][j]==12:
									if self.LL[rr-x][r-j-1]&4!=4:
										H1=1
										break	
									if self.LL[rr-x-1][r-j-1]&8!=8:
										H1=1
										break
								if self.LL[x][j]==1:
									if self.LL[rr-x+1][r-j]&1!=1:
										H1=1
										break
								if self.LL[x][j]==5:
									if self.LL[rr-x+1][r-j]&1!=1:
										H1=1
										break	
									if self.LL[rr-x][r-j-1]&4!=4:
										H1=1
										break	
								if self.LL[x][j]==9:
									if self.LL[rr-x+1][r-j]&1!=1:
										H1=1
										break	
									if self.LL[rr-x-1][r-j-1]&8!=8:
										H1=1
										break	
								if self.LL[x][j]==13:
									if self.LL[rr-x+1][r-j]&1!=1:
										H1=1
										break	
									if self.LL[rr-x-1][r-j-1]&8!=8:
										H1=1
										break
									if self.LL[rr-x][r-j-1]&4!=4:
										H1=1
										break
								if self.LL[x][j]==2:
									if self.LL[rr-x+1][r-j-1]&2!=2:
										H1=1
										break
								if self.LL[x][j]==6:
									if self.LL[rr-x+1][r-j-1]&2!=2:
										H1=1
										break		
									if self.LL[rr-x][r-j-1]&4!=4:
										H1=1
										break
								if self.LL[x][j]==10:
									if self.LL[rr-x+1][r-j-1]&2!=2:
										H1=1
										break		
									if self.LL[rr-x-1][r-j-1]&8!=8:
										H1=1
										break		
								if self.LL[x][j]==14:
									if self.LL[rr-x-1][r-j-1]&8!=8:
										H1=1
										break		
									if self.LL[rr-x+1][r-j-1]&2!=2:
										H1=1
										break		
									if self.LL[rr-x][r-j-1]&4!=4:
										H1=1
										break
								if self.LL[x][j]==3:
									if self.LL[rr-x+1][r-j-1]&2!=2:
										H1=1
										break		
									if self.LL[rr-x+1][r-j]&1!=1:
										H1=1
										break
								if self.LL[x][j]==7:
									if self.LL[rr-x+1][r-j]&1!=1:
										H1=1
										break		
									if self.LL[rr-x][r-j-1]&4!=4:
										H1=1
										break
									if self.LL[rr-x+1][r-j-1]&2!=2:
										H1=1
										break
								if self.LL[x][j]==11:
									if self.LL[rr-x+1][r-j]&1!=1:
										H1=1
										break		
									if self.LL[rr-x-1][r-j-1]&8!=8:
										H1=1
										break
									if self.LL[rr-x+1][r-j-1]&2!=2:
										H1=1
										break
								if self.LL[x][j]==15:
									if self.LL[rr-x-1][r-j-1]&8!=8:
										H1=1
										break		
									if self.LL[rr-x][r-j-1]&4!=4:
										H1=1
										break
									if self.LL[rr-x+1][r-j]&1!=1:
										H1=1
										break
									if self.LL[rr-x+1][r-j-1]&2!=2:
										H1=1
										break
							if H1==1:
								break
						for x in range(self.LL_length_length):
							for j in range(1,m+1):
								if self.LL[rr-x][r-j]==0:
									if self.LL[x+1][j]&1==1:
										H1=1
										break
								if self.LL[rr-x][r-j]==4:
									if self.LL[x][j-1]&4!=4:
										H1=1
										break
								if self.LL[rr-x][r-j]==8:
									if self.LL[x-1][j-1]&8!=8:
										H1=1
										break 		
								if self.LL[rr-x][r-j]==12:
									if self.LL[x][j-1]&4!=4:
										H1=1
										break	
									if self.LL[x-1][j-1]&8!=8:
										H1=1
										break
								if self.LL[rr-x][r-j]==1:
									if self.LL[x+1][j]&1!=1:
										H1=1
										break
								if self.LL[rr-x][r-j]==5:
									if self.LL[x+1][j]&1!=1:
										H1=1
										break	
									if self.LL[x][j-1]&4!=4:
										H1=1
										break	
								if self.LL[rr-x][r-j]==9:
									if self.LL[x+1][j]&1!=1:
										H1=1
										break	
									if self.LL[x-1][j-1]&8!=8:
										H1=1
										break	
								if self.LL[rr-x][r-j]==13:
									if self.LL[x+1][j]&1!=1:
										H1=1
										break	
									if self.LL[x-1][j-1]&8!=8:
										H1=1
										break
									if self.LL[x][j-1]&4!=4:
										H1=1
										break
								if self.LL[rr-x][r-j]==2:
									if self.LL[x+1][j-1]&2!=2:
										H1=1
										break
								if self.LL[rr-x][r-j]==6:
									if self.LL[x+1][j-1]&2!=2:
										H1=1
										break		
									if self.LL[x][j-1]&4!=4:
										H1=1
										break
								if self.LL[rr-x][r-j]==10:
									if self.LL[x+1][j-1]&2!=2:
										H1=1
										break		
									if self.LL[x-1][j-1]&8!=8:
										H1=1
										break		
								if self.LL[rr-x][r-j]==14:
									if self.LL[x-1][j-1]&8!=8:
										H1=1
										break		
									if self.LL[x+1][j-1]&2!=2:
										H1=1
										break		
									if self.LL[x][j-1]&4!=4:
										H1=1
										break
								if self.LL[rr-x][r-j]==3:
									if self.LL[x+1][j-1]&2!=2:
										H1=1
										break		
									if self.LL[x+1][j]&1!=1:
										H1=1
										break
								if self.LL[rr-x][r-j]==7:
									if self.LL[x+1][j]&1!=1:
										H1=1
										break		
									if self.LL[x][j-1]&4!=4:
										H1=1
										break
									if self.LL[x+1][j-1]&2!=2:
										H1=1
										break
								if self.LL[rr-x][r-j]==11:
									if self.LL[x+1][j]&1!=1:
										H1=1
										break		
									if self.LL[x-1][j-1]&8!=8:
										H1=1
										break
									if self.LL[x+1][j-1]&2!=2:
										H1=1
										break
								if self.LL[rr-x][r-j]==15:
									if self.LL[x-1][j-1]&8!=8:
										H1=1
										break		
									if self.LL[x][j-1]&4!=4:
										H1=1
										break
									if self.LL[x+1][j]&1!=1:
										H1=1
										break
									if self.LL[x+1][j-1]&2!=2:
										H1=1
										break
							if H1==1:
								break
					if H1==0:
						break
					i+=0.5
			else:
				rr=int(self.LL_length_length-1)
				while i<self.T+1:
					H1=0
					m=int(i//1)
					n=i%1
					if n==0.0:
						r=m
						for x in range(self.LL_length_length):
							for j in range(r+1):
								if self.LL[x][j]==0:
									if self.LL[rr-x+1][2*r-j]&1==1:
										H1=1
										break
								if self.LL[x][j]==4:
									if self.LL[rr-x][2*r-j-1]&4!=4:
										H1=1
										break
								if self.LL[x][j]==8:
									if self.LL[rr-x-1][2*r-j-1]&8!=8:
										H1=1
										break
								if self.LL[x][j]==12:
									if self.LL[rr-x][2*r-j-1]&4!=4:
										H1=1
										break	
									if self.LL[rr-x-1][2*r-j-1]&8!=8:
										H1=1
										break
								if self.LL[x][j]==1:
									if self.LL[rr-x+1][2*r-j]&1!=1:
										H1=1
										break
								if self.LL[x][j]==5:
									if self.LL[rr-x+1][2*r-j]&1!=1:
										H1=1
										break	
									if self.LL[rr-x][2*r-j-1]&4!=4:
										H1=1
										break	
								if self.LL[x][j]==9:
									if self.LL[rr-x+1][2*r-j]&1!=1:
										H1=1
										break	
									if self.LL[rr-x-1][2*r-j-1]&8!=8:
										H1=1
										break	
								if self.LL[x][j]==13:
									if self.LL[rr-x+1][2*r-j]&1!=1:
										H1=1
										break	
									if self.LL[rr-x-1][2*r-j-1]&8!=8:
										H1=1
										break
									if self.LL[rr-x][2*r-j-1]&4!=4:
										H1=1
										break
								if self.LL[x][j]==2:
									if self.LL[rr-x+1][2*r-j-1]&2!=2:
										H1=1
										break
								if self.LL[x][j]==6:
									if self.LL[rr-x+1][2*r-j-1]&2!=2:
										H1=1
										break		
									if self.LL[rr-x][2*r-j-1]&4!=4:
										H1=1
										break
								if self.LL[x][j]==10:
									if self.LL[rr-x+1][2*r-j-1]&2!=2:
										H1=1
										break		
									if self.LL[rr-x-1][2*r-j-1]&8!=8:
										H1=1
										break		
								if self.LL[x][j]==14:
									if self.LL[rr-x-1][2*r-j-1]&8!=8:
										H1=1
										break		
									if self.LL[rr-x+1][2*r-j-1]&2!=2:
										H1=1
										break		
									if self.LL[rr-x][2*r-j-1]&4!=4:
										H1=1
										break
								if self.LL[x][j]==3:
									if self.LL[rr-x+1][2*r-j-1]&2!=2:
										H1=1
										break		
									if self.LL[rr-x+1][2*r-j]&1!=1:
										H1=1
										break
								if self.LL[x][j]==7:
									if self.LL[rr-x+1][2*r-j]&1!=1:
										H1=1
										break		
									if self.LL[rr-x][2*r-j-1]&4!=4:
										H1=1
										break
									if self.LL[rr-x+1][2*r-j-1]&2!=2:
										H1=1
										break
								if self.LL[x][j]==11:
									if self.LL[rr-x+1][2*r-j]&1!=1:
										H1=1
										break		
									if self.LL[rr-x-1][2*r-j-1]&8!=8:
										H1=1
										break
									if self.LL[rr-x+1][2*r-j-1]&2!=2:
										H1=1
										break
								if self.LL[x][j]==15:
									if self.LL[rr-x-1][2*r-j-1]&8!=8:
										H1=1
										break		
									if self.LL[rr-x][2*r-j-1]&4!=4:
										H1=1
										break
									if self.LL[rr-x+1][2*r-j]&1!=1:
										H1=1
										break
									if self.LL[rr-x+1][2*r-j-1]&2!=2:
										H1=1
										break
							if H1==1:
								break
						for x in range(self.LL_length_length):
							for j in range(1,r+1):
								if self.LL[rr-x][2*r-j]==0:
									if self.LL[x+1][j]&1==1:
										H1=1
										break
								if self.LL[rr-x][2*r-j]==4:
									if self.LL[x][j-1]&4!=4:
										H1=1
										break
								if self.LL[rr-x][2*r-j]==8:
									if self.LL[x-1][j-1]&8!=8:
										H1=1
										break 		
								if self.LL[rr-x][2*r-j]==12:
									if self.LL[x][j-1]&4!=4:
										H1=1
										break	
									if self.LL[x-1][j-1]&8!=8:
										H1=1
										break
								if self.LL[rr-x][2*r-j]==1:
									if self.LL[x+1][j]&1!=1:
										H1=1
										break
								if self.LL[rr-x][2*r-j]==5:
									if self.LL[x+1][j]&1!=1:
										H1=1
										break	
									if self.LL[x][j-1]&4!=4:
										H1=1
										break	
								if self.LL[rr-x][2*r-j]==9:
									if self.LL[x+1][j]&1!=1:
										H1=1
										break	
									if self.LL[x-1][j-1]&8!=8:
										H1=1
										break	
								if self.LL[rr-x][2*r-j]==13:
									if self.LL[x+1][j]&1!=1:
										H1=1
										break	
									if self.LL[x-1][j-1]&8!=8:
										H1=1
										break
									if self.LL[x][j-1]&4!=4:
										H1=1
										break
								if self.LL[rr-x][2*r-j]==2:
									if self.LL[x+1][j-1]&2!=2:
										H1=1
										break
								if self.LL[rr-x][2*r-j]==6:
									if self.LL[x+1][j-1]&2!=2:
										H1=1
										break		
									if self.LL[x][j-1]&4!=4:
										H1=1
										break
								if self.LL[rr-x][2*r-j]==10:
									if self.LL[x+1][j-1]&2!=2:
										H1=1
										break		
									if self.LL[x-1][j-1]&8!=8:
										H1=1
										break		
								if self.LL[rr-x][2*r-j]==14:
									if self.LL[x-1][j-1]&8!=8:
										H1=1
										break		
									if self.LL[x+1][j-1]&2!=2:
										H1=1
										break		
									if self.LL[x][j-1]&4!=4:
										H1=1
										break
								if self.LL[rr-x][2*r-j]==3:
									if self.LL[x+1][j-1]&2!=2:
										H1=1
										break		
									if self.LL[x+1][j]&1!=1:
										H1=1
										break
								if self.LL[rr-x][2*r-j]==7:
									if self.LL[x+1][j]&1!=1:
										H1=1
										break		
									if self.LL[x][j-1]&4!=4:
										H1=1
										break
									if self.LL[x+1][j-1]&2!=2:
										H1=1
										break
								if self.LL[rr-x][2*r-j]==11:
									if self.LL[x+1][j]&1!=1:
										H1=1
										break		
									if self.LL[x-1][j-1]&8!=8:
										H1=1
										break
									if self.LL[x+1][j-1]&2!=2:
										H1=1
										break
								if self.LL[rr-x][2*r-j]==15:
									if self.LL[x-1][j-1]&8!=8:
										H1=1
										break		
									if self.LL[x][j-1]&4!=4:
										H1=1
										break
									if self.LL[x+1][j]&1!=1:
										H1=1
										break
									if self.LL[x+1][j-1]&2!=2:
										H1=1
										break
							if H1==1:
								break		
					else:
						r=int(2*(m+n))
						for x in range(self.LL_length_length):
							for j in range(m+1):
								if self.LL[x][j]==0:
									if self.LL[rr-x+1][r-j]&1==1:
										H1=1
										break
								if self.LL[x][j]==4:
									if self.LL[rr-x][r-j-1]&4!=4:
										H1=1
										break
								if self.LL[x][j]==8:
									if self.LL[rr-x-1][r-j-1]&8!=8:
										H1=1
										break 		
								if self.LL[x][j]==12:
									if self.LL[rr-x][r-j-1]&4!=4:
										H1=1
										break	
									if self.LL[rr-x-1][r-j-1]&8!=8:
										H1=1
										break
								if self.LL[x][j]==1:
									if self.LL[rr-x+1][r-j]&1!=1:
										H1=1
										break
								if self.LL[x][j]==5:
									if self.LL[rr-x+1][r-j]&1!=1:
										H1=1
										break	
									if self.LL[rr-x][r-j-1]&4!=4:
										H1=1
										break	
								if self.LL[x][j]==9:
									if self.LL[rr-x+1][r-j]&1!=1:
										H1=1
										break	
									if self.LL[rr-x-1][r-j-1]&8!=8:
										H1=1
										break	
								if self.LL[x][j]==13:
									if self.LL[rr-x+1][r-j]&1!=1:
										H1=1
										break	
									if self.LL[rr-x-1][r-j-1]&8!=8:
										H1=1
										break
									if self.LL[rr-x][r-j-1]&4!=4:
										H1=1
										break
								if self.LL[x][j]==2:
									if self.LL[rr-x+1][r-j-1]&2!=2:
										H1=1
										break
								if self.LL[x][j]==6:
									if self.LL[rr-x+1][r-j-1]&2!=2:
										H1=1
										break		
									if self.LL[rr-x][r-j-1]&4!=4:
										H1=1
										break
								if self.LL[x][j]==10:
									if self.LL[rr-x+1][r-j-1]&2!=2:
										H1=1
										break		
									if self.LL[rr-x-1][r-j-1]&8!=8:
										H1=1
										break		
								if self.LL[x][j]==14:
									if self.LL[rr-x-1][r-j-1]&8!=8:
										H1=1
										break		
									if self.LL[rr-x+1][r-j-1]&2!=2:
										H1=1
										break		
									if self.LL[rr-x][r-j-1]&4!=4:
										H1=1
										break
								if self.LL[x][j]==3:
									if self.LL[rr-x+1][r-j-1]&2!=2:
										H1=1
										break		
									if self.LL[rr-x+1][r-j]&1!=1:
										H1=1
										break
								if self.LL[x][j]==7:
									if self.LL[rr-x+1][r-j]&1!=1:
										H1=1
										break		
									if self.LL[rr-x][r-j-1]&4!=4:
										H1=1
										break
									if self.LL[rr-x+1][r-j-1]&2!=2:
										H1=1
										break
								if self.LL[x][j]==11:
									if self.LL[rr-x+1][r-j]&1!=1:
										H1=1
										break		
									if self.LL[rr-x-1][r-j-1]&8!=8:
										H1=1
										break
									if self.LL[rr-x+1][r-j-1]&2!=2:
										H1=1
										break
								if self.LL[x][j]==15:
									if self.LL[rr-x-1][r-j-1]&8!=8:
										H1=1
										break		
									if self.LL[rr-x][r-j-1]&4!=4:
										H1=1
										break
									if self.LL[rr-x+1][r-j]&1!=1:
										H1=1
										break
									if self.LL[rr-x+1][r-j-1]&2!=2:
										H1=1
										break
							if H1==1:
								break
						for x in range(self.LL_length_length):
							for j in range(1,m+1):
								if self.LL[rr-x][r-j]==0:
									if self.LL[x+1][j]&1==1:
										H1=1
										break
								if self.LL[rr-x][r-j]==4:
									if self.LL[x][j-1]&4!=4:
										H1=1
										break
								if self.LL[rr-x][r-j]==8:
									if self.LL[x-1][j-1]&8!=8:
										H1=1
										break 		
								if self.LL[rr-x][r-j]==12:
									if self.LL[x][j-1]&4!=4:
										H1=1
										break	
									if self.LL[x-1][j-1]&8!=8:
										H1=1
										break
								if self.LL[rr-x][r-j]==1:
									if self.LL[x+1][j]&1!=1:
										H1=1
										break
								if self.LL[rr-x][r-j]==5:
									if self.LL[x+1][j]&1!=1:
										H1=1
										break	
									if self.LL[x][j-1]&4!=4:
										H1=1
										break	
								if self.LL[rr-x][r-j]==9:
									if self.LL[x+1][j]&1!=1:
										H1=1
										break	
									if self.LL[x-1][j-1]&8!=8:
										H1=1
										break	
								if self.LL[rr-x][r-j]==13:
									if self.LL[x+1][j]&1!=1:
										H1=1
										break	
									if self.LL[x-1][j-1]&8!=8:
										H1=1
										break
									if self.LL[x][j-1]&4!=4:
										H1=1
										break
								if self.LL[rr-x][r-j]==2:
									if self.LL[x+1][j-1]&2!=2:
										H1=1
										break
								if self.LL[rr-x][r-j]==6:
									if self.LL[x+1][j-1]&2!=2:
										H1=1
										break		
									if self.LL[x][j-1]&4!=4:
										H1=1
										break
								if self.LL[rr-x][r-j]==10:
									if self.LL[x+1][j-1]&2!=2:
										H1=1
										break		
									if self.LL[x-1][j-1]&8!=8:
										H1=1
										break		
								if self.LL[rr-x][r-j]==14:
									if self.LL[x-1][j-1]&8!=8:
										H1=1
										break		
									if self.LL[x+1][j-1]&2!=2:
										H1=1
										break		
									if self.LL[x][j-1]&4!=4:
										H1=1
										break
								if self.LL[rr-x][r-j]==3:
									if self.LL[x+1][j-1]&2!=2:
										H1=1
										break		
									if self.LL[x+1][j]&1!=1:
										H1=1
										break
								if self.LL[rr-x][r-j]==7:
									if self.LL[x+1][j]&1!=1:
										H1=1
										break		
									if self.LL[x][j-1]&4!=4:
										H1=1
										break
									if self.LL[x+1][j-1]&2!=2:
										H1=1
										break
								if self.LL[rr-x][r-j]==11:
									if self.LL[x+1][j]&1!=1:
										H1=1
										break		
									if self.LL[x-1][j-1]&8!=8:
										H1=1
										break
									if self.LL[x+1][j-1]&2!=2:
										H1=1
										break
								if self.LL[rr-x][r-j]==15:
									if self.LL[x-1][j-1]&8!=8:
										H1=1
										break		
									if self.LL[x][j-1]&4!=4:
										H1=1
										break
									if self.LL[x+1][j]&1!=1:
										H1=1
										break
									if self.LL[x+1][j-1]&2!=2:
										H1=1
										break
							if H1==1:
								break
					if H1==0:
						break
					i+=0.5
			if H1==0:
				R=True
				
		#print(H,GH,V,R)
		if H==False and GH==False and V==False and R==False:
			print(f'Pattern is a frieze of period {self.T} that is invariant under translation only.')
		if H==False and GH==False and V==True and R==False:	
			print(f'Pattern is a frieze of period {self.T} that is invariant under translation')
			print('        and vertical reflection only.')
		if H==True and GH==False and V==False and R==False:	
			print(f'Pattern is a frieze of period {self.T} that is invariant under translation')
			print('        and horizontal reflection only.')
		if H==False and GH==True and V==False and R==False:	
			print(f'Pattern is a frieze of period {self.T} that is invariant under translation')
			print('        and glided horizontal reflection only.')
		if H==False and GH==False and V==False and R==True:	
			print(f'Pattern is a frieze of period {self.T} that is invariant under translation')
			print('        and rotation only.')
		if H==False and GH==True and V==True and R==True:	
			print(f'Pattern is a frieze of period {self.T} that is invariant under translation,')
			print('        glided horizontal and vertical reflections, and rotation only.')
		if H==True and GH==False and V==True and R==True:	
			print(f'Pattern is a frieze of period {self.T} that is invariant under translation,')
			print('        horizontal and vertical reflections, and rotation only.')
		
		
		
	def display(self):
		H1=[]
		for i in str(self.filename):
			if i!='.':
				H1.append(i)
			else:
				break
		H2=''.join(H1)
		with open(f'{H2}.tex','w') as f:
			context=r'''\documentclass[10pt]{article}
\usepackage{tikz}
\usepackage[margin=0cm]{geometry}
\pagestyle{empty}

\begin{document}

\vspace*{\fill}
\begin{center}
\begin{tikzpicture}[x=0.2cm, y=-0.2cm, thick, purple]
% North to South lines
'''
			f.write(context)
			H4=[]
			for i in range(self.LL_length):
				for j in range(len(self.LL)):
					H44=[]
					H3=self.LL[j][i]
					if bin(H3&1).replace('0b','')=='1':
						H44.append(i)
						H44.append(j-1)
						H4.append(H44)
			H444=[]
			H41=[]
			if H4!=[]:
				for i in range(len(H4)-1):
					if H4[i][0]==H4[i+1][0]:
						H444.append((H4[i][0],H4[i][1]))
						H444.append((H4[i+1][0],H4[i+1][1]))
					else:
						if H444==[]:
							if i==len(H4)-2:
								H444.append((H4[i][0],H4[i][1]))
								H41.append(H444)
								H444=[]
								H444.append((H4[i+1][0],H4[i+1][1]))
							else:
								H444.append((H4[i][0],H4[i][1]))
								H41.append(H444)
								H444=[]
						else:
							H4444=sorted(list(set(H444)))
							H41.append(H4444)
							H444=[]
				H4444=sorted(list(set(H444)))			
				H41.append(H4444)
				for i in range(len(H41)):
					H5=H41[i][0][1]
					H6=H41[i][0][1]+1
					j=1
					while j<len(H41[i]):
						if H41[i][j][1]!=H6:
							f.write('    \draw ')
							f.write(f'({H41[i][0][0]},{H5})')
							f.write(' -- ')
							f.write(f'({H41[i][0][0]},{H6});\n')
							H5=H41[i][j][1]
							H6=H41[i][j][1]+1
						else:
							H6+=1
						j+=1
					f.write('    \draw ')
					f.write(f'({H41[i][0][0]},{H5})')
					f.write(' -- ')
					f.write(f'({H41[i][0][0]},{H6});\n')
			f.write('% North-West to South-East lines\n')
			H7=[]
			H8=[]
			for _ in range(self.LL_length_length):
				for _ in range(self.LL_length):
					H8.append('0')
				H7.append(H8)
				H8=[]
			i=0
			while i<len(self.LL):
				j=0
				while j<self.LL_length:
					if H7[i][j]=='0' and bin(self.LL[i][j]&8).replace('0b','')=='1000':
						H5=j+1
						H6=i+1
						while bin(self.LL[H6][H5]&8).replace('0b','')=='1000':
							H7[H6][H5]='1'
							H5+=1
							H6+=1
						f.write('    \draw ')
						f.write(f'({j},{i})')
						f.write(' -- ')
						f.write(f'({H5},{H6});\n')
					j+=1
				i+=1
			f.write('% West to East lines\n')
			H4=[]
			for i in range(len(self.LL)):
				for j in range(self.LL_length):
					H44=[]
					H3=self.LL[i][j]
					if bin(H3&4).replace('0b','')=='100':
						H44.append(i)
						H44.append(j)
						H4.append(H44)
			H444=[]
			H41=[]
			for i in range(len(H4)-1):
				if H4[i][0]==H4[i+1][0]:
					H444.append((H4[i][0],H4[i][1]))
					H444.append((H4[i+1][0],H4[i+1][1]))
				else:
					if H444==[]:
						if i==len(H4)-2:
							H444.append((H4[i][0],H4[i][1]))
							H41.append(H444)
							H444=[]
							H444.append((H4[i+1][0],H4[i+1][1]))
						else:
							H444.append((H4[i][0],H4[i][1]))
							H41.append(H444)
							H444=[]
					else:
						H4444=sorted(list(set(H444)))
						H41.append(H4444)
						H444=[]
			H4444=sorted(list(set(H444)))			
			H41.append(H4444)
			for i in range(len(H41)):
				H5=H6=H41[i][0][1]
				j=1
				while j<len(H41[i]):
					if H41[i][j][1]!=H6+1:
						f.write('    \draw ')
						f.write(f'({H5},{H41[i][0][0]})')
						f.write(' -- ')
						f.write(f'({H6+1},{H41[i][0][0]});\n')
						H5=H6=H41[i][j][1]
					else:
						H6+=1
					j+=1
				f.write('    \draw ')
				f.write(f'({H5},{H41[i][0][0]})')
				f.write(' -- ')
				f.write(f'({H6+1},{H41[i][0][0]});\n')
			f.write('% South-West to North-East lines\n')
			H7=[]
			H8=[]
			H11=defaultdict(list)
			H12=[]
			for _ in range(self.LL_length_length):
				for _ in range(self.LL_length):
					H8.append('0')
				H7.append(H8)
				H8=[]
			i=len(self.LL)-1
			while i>-1:
				j=0
				while j<self.LL_length:
					if H7[i][j]=='0' and bin(self.LL[i][j]&2).replace('0b','')=='10':
						H5=j+1
						H6=i-1
						while bin(self.LL[H6][H5]&2).replace('0b','')=='10':
							H7[H6][H5]='1'
							H5+=1
							H6-=1
						H12.append(j)
						H12.append(H5)
						H12.append(H6)
						H11[i].append(H12)
						H12=[]
					j+=1
				i-=1
			H13=dict(sorted(H11.items(),key=operator.itemgetter(0)))
			for i in list(H13.keys()):
				for j in range(len(H13[i])):
					f.write('    \draw ')
					f.write(f'({H13[i][j][0]},{i})')
					f.write(' -- ')
					f.write(f'({H13[i][j][1]},{H13[i][j][2]});\n')
			context=r'''\end{tikzpicture}
\end{center}
\vspace*{\fill}

\end{document}
'''
			f.write(context)
