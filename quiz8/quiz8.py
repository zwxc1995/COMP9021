# Randomly fills a grid of size 10 x 10 with 0s and 1s,
# in an estimated proportion of 1/2 for each,
# and computes the longest leftmost path that starts
# from the top left corner -- a path consisting of
# horizontally or vertically adjacent 1s --,
# visiting every point on the path once only.
#
# Written by *** and Eric Martin for COMP9021


import sys
from random import seed, randrange

from queue_adt import *
import copy 

def display_grid():
    for i in range(len(grid)):
        print('   ', ' '.join(str(grid[i][j]) for j in range(len(grid[0]))))

def leftmost_longest_path_from_top_left_corner():
	if grid[0][0]==0:
		return
	H1=Queue()
	H1.enqueue(([(0,0)],'E'))
	while H1.is_empty()==0:
		H2,H3=H1.dequeue()
		H4=H2[len(H2)-1]
		if H3=='E':
			for i in ('S','E','N'):
				if i=='S':
					H5=(H4[0],H4[1]-1)
				elif i=='E':
					H5=(H4[0]+1,H4[1])
				elif i=='N':
					H5=(H4[0],H4[1]+1)
				if not -1<H5[0]<10 or not -1<H5[1]<10 or H5 in H2 or grid[H5[0]][H5[1]]==0:
					continue
				H6=copy.deepcopy(H2)
				H6+=[H5]
				H1.enqueue((H6,i))
		if H3=='S':
			for i in ('W','S','E'):
				if i=='W':
					H5=(H4[0]-1,H4[1])
				elif i=='S':
					H5=(H4[0],H4[1]-1)
				elif i=='E':
					H5=(H4[0]+1,H4[1])
				if not -1<H5[0]<10 or not -1<H5[1]<10 or H5 in H2 or grid[H5[0]][H5[1]]==0:
					continue
				H6=copy.deepcopy(H2)
				H6+=[H5]
				H1.enqueue((H6,i))				
		if H3=='N':
			for i in ('E','N','W'):
				if i=='E':
					H5=(H4[0]+1,H4[1])
				elif i=='N':
					H5=(H4[0],H4[1]+1)
				elif i=='W':
					H5=(H4[0]-1,H4[1])
				if not -1<H5[0]<10 or not -1<H5[1]<10 or H5 in H2 or grid[H5[0]][H5[1]]==0:
					continue
				H6=copy.deepcopy(H2)
				H6+=[H5]
				H1.enqueue((H6,i))
		if H3=='W':
			for i in ('N','W','S'):
				if i=='N':
					H5=(H4[0],H4[1]+1)
				elif i=='W':
					H5=(H4[0]-1,H4[1])
				elif i=='S':
					H5=(H4[0],H4[1]-1)
				if not -1<H5[0]<10 or not -1<H5[1]<10 or H5 in H2 or grid[H5[0]][H5[1]]==0:
					continue
				H6=copy.deepcopy(H2)
				H6+=[H5]
				H1.enqueue((H6,i))
	path=H2
	return path	
    # Replace pass above with your code


provided_input = input('Enter one integer: ')
try:
    for_seed = int(provided_input)
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
seed(for_seed)
grid = [[randrange(2) for _ in range(10)] for _ in range(10)]
print('Here is the grid that has been generated:')
display_grid()
path = leftmost_longest_path_from_top_left_corner()
if not path:
    print('There is no path from the top left corner.')
else:
    print(f'The leftmost longest path from the top left corner is: {path}')
           
