# Randomly generates a grid with 0s and 1s, whose dimension is controlled by user input,
# as well as the density of 1s in the grid, and finds out, for a given direction being
# one of N, E, S or W (for North, East, South or West) and for a given size greater than 1,
# the number of triangles pointing in that direction, and of that size.
#
# Triangles pointing North:
# - of size 2:
#   1
# 1 1 1
# - of size 3:
#     1
#   1 1 1
# 1 1 1 1 1
#
# Triangles pointing East:
# - of size 2:
# 1
# 1 1
# 1
# - of size 3:
# 1
# 1 1
# 1 1 1 
# 1 1
# 1
#
# Triangles pointing South:
# - of size 2:
# 1 1 1
#   1
# - of size 3:
# 1 1 1 1 1
#   1 1 1
#     1
#
# Triangles pointing West:
# - of size 2:
#   1
# 1 1
#   1
# - of size 3:
#     1
#   1 1
# 1 1 1 
#   1 1
#     1
#
# The output lists, for every direction and for every size, the number of triangles
# pointing in that direction and of that size, provided there is at least one such triangle.
# For a given direction, the possble sizes are listed from largest to smallest.
#
# We do not count triangles that are truncations of larger triangles, that is, obtained
# from the latter by ignoring at least one layer, starting from the base.
#
# Written by *** and Eric Martin for COMP9021


from random import seed, randint
import sys
from collections import defaultdict
import copy


def display_grid():
    for i in range(len(grid)):
        print('   ', ' '.join(str(int(grid[i][j] != 0)) for j in range(len(grid))))

def triangles_in_grid():
    List1=[]
    for j in range (0,len(grid)):
        for i in range(0,len(grid)):
            H3 =1
            H2 = min(i+1,len(grid)-i,len(grid)-j)
            while H2>=2:
                H3=1
                H5=0
                for y in range(j,j+H2):
                    for x in range(i-H5,i+H5+1):
                        if grid[y][x] == 0:
                            H3=0
                            break
                    if H3==0:
                        H2-=1
                        break
                    else:
                        H5+=1
                if H3!=0:
                    List1.append(H2)
                    break
    List4=defaultdict(list)
    List2=set(List1)
    List3=sorted(List2,reverse=True)
    i=0
    for x in range(0,len(List3)):
        i=0
        for y in range(0,len(List1)):
            if List1[y] == List3[x]:
                i+=1
        List4['N'].append((List3[x],i))
    gridH1=copy.deepcopy(grid)
    gridH1.reverse()
    gridH2=[[jj[ii] for jj in gridH1] for ii in range(len(gridH1[0]))]
    List1=[]
    for j in range (0,len(gridH2)):
        for i in range(0,len(gridH2)):
            H3 =1
            H2 = min(i+1,len(gridH2)-i,len(gridH2)-j)
            while H2>=2:
                H3=1
                H5=0
                for y in range(j,j+H2):
                    for x in range(i-H5,i+H5+1):
                        if gridH2[y][x] == 0:
                            H3=0
                            break
                    if H3==0:
                        H2-=1
                        break
                    else:
                        H5+=1
                if H3!=0:
                    List1.append(H2)
                    break
    List2=set(List1)
    List3=sorted(List2,reverse=True)
    i=0
    for x in range(0,len(List3)):
        i=0
        for y in range(0,len(List1)):
            if List1[y] == List3[x]:
                i+=1
        List4['W'].append((List3[x],i))
    gridH3=copy.deepcopy(gridH2)
    gridH3.reverse()
    gridH4=[[jj[ii] for jj in gridH3] for ii in range(len(gridH3[0]))]
    List1=[]
    for j in range (0,len(gridH4)):
        for i in range(0,len(gridH4)):
            H3 =1
            H2 = min(i+1,len(gridH4)-i,len(gridH4)-j)
            while H2>=2:
                H3=1
                H5=0
                for y in range(j,j+H2):
                    for x in range(i-H5,i+H5+1):
                        if gridH4[y][x] == 0:
                            H3=0
                            break
                    if H3==0:
                        H2-=1
                        break
                    else:
                        H5+=1
                if H3!=0:
                    List1.append(H2)
                    break
    List2=set(List1)
    List3=sorted(List2,reverse=True)
    i=0
    for x in range(0,len(List3)):
        i=0
        for y in range(0,len(List1)):
            if List1[y] == List3[x]:
                i+=1
        List4['S'].append((List3[x],i))
    gridH5=copy.deepcopy(gridH4)
    gridH5.reverse()
    gridH6=[[jj[ii] for jj in gridH5] for ii in range(len(gridH5[0]))]
    List1=[]
    for j in range (0,len(gridH6)):
        for i in range(0,len(gridH6)):
            H3 =1
            H2 = min(i+1,len(gridH6)-i,len(gridH6)-j)
            while H2>=2:
                H3=1
                H5=0
                for y in range(j,j+H2):
                    for x in range(i-H5,i+H5+1):
                        if gridH6[y][x] == 0:
                            H3=0
                            break
                    if H3==0:
                        H2-=1
                        break
                    else:
                        H5+=1
                if H3!=0:
                    List1.append(H2)
                    break
    List2=set(List1)
    List3=sorted(List2,reverse=True)
    i=0
    for x in range(0,len(List3)):
        i=0
        for y in range(0,len(List1)):
            if List1[y] == List3[x]:
                i+=1
        List4['E'].append((List3[x],i))
    return List4


    # Replace return {} above with your code

# Possibly define other functions

try:
    arg_for_seed, density, dim = input('Enter three nonnegative integers: ').split()
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    arg_for_seed, density, dim = int(arg_for_seed), int(density), int(dim)
    if arg_for_seed < 0 or density < 0 or dim < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
seed(arg_for_seed)
grid = [[randint(0, density) for _ in range(dim)] for _ in range(dim)]
print('Here is the grid that has been generated:')
display_grid()
# A dictionary whose keys are amongst 'N', 'E', 'S' and 'W',
# and whose values are pairs of the form (size, number_of_triangles_of_that_size),
# ordered from largest to smallest size.
triangles = triangles_in_grid()
for direction in sorted(triangles, key = lambda x: 'NESW'.index(x)):
    print(f'\nFor triangles pointing {direction}, we have:')
    for size, nb_of_triangles in triangles[direction]:
        triangle_or_triangles = 'triangle' if nb_of_triangles == 1 else 'triangles'
        print(f'     {nb_of_triangles} {triangle_or_triangles} of size {size}')
