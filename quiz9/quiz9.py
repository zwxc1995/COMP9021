# Randomly generates a binary search tree whose number of nodes
# is determined by user input, with labels ranging between 0 and 999,999,
# displays it, and outputs the maximum difference between consecutive leaves.
#
# Written by *** and Eric Martin for COMP9021

import sys
from random import seed, randrange
from binary_tree_adt import *

# Possibly define some functions
class EmptyQueueError(Exception):
	def __init__(self, message):
		self.message = message


class Queue:
	min_capacity = 10

	def __init__(self, capacity = min_capacity):
		self.min_capacity = capacity
		self._data = [None] * capacity
		self._length = 0
		self._front = 0
        
	def __len__(self):
		return self._length

	def is_empty(self):
		return self._length == 0
	
	def enqueue(self, datum):
		if self._length == len(self._data):
			self._resize(2 * len(self._data))
		self._data[(self._front + self._length) % len(self._data)] = datum
		self._length += 1

	def dequeue(self):
		if self.is_empty():
			raise EmptyQueueError('Cannot dequeue from empty queue')
		datum_at_front = self._data[self._front]
		self._data[self._front] = None
		self._front = (self._front + 1) % len(self._data)        
		self._length -= 1
		self._shrink_if_needed()
		return datum_at_front
	
	def _shrink_if_needed(self):
		if self.min_capacity // 2 <= self._length <= len(self._data) // 4:
			self._resize(len(self._data) // 2)
	
def find_consecutive_leaves(tree):
	if tree is None:
		return 
	H1=Queue()
	H1.enqueue(tree)
	H2=[]
	while not H1.is_empty():
		H3=H1.dequeue()
		if H3.left_node.value is None and H3.right_node.value is None:
			H2.append(H3.value)
		elif H3.left_node.value is not None:
				H1.enqueue(H3.left_node)
		if H3.right_node.value is not None:
				H1.enqueue(H3.right_node)
	return H2	
	
def max_diff_in_consecutive_leaves(tree):
	H4=find_consecutive_leaves(tree)
	H4.sort()
	H5=[]
	for i in range(0,len(H4)-1):
		H6=H4[i+1]-H4[i]
		H5.append(H6)
	if H5!=[]:
		H7=max(H5)
	else:
		H7=0
	return H7
    # Replace pass above with your code


provided_input = input('Enter two integers, the second one being positive: ')
try:
    arg_for_seed, nb_of_nodes = provided_input.split()
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    arg_for_seed, nb_of_nodes = int(arg_for_seed), int(nb_of_nodes)
    if nb_of_nodes < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
seed(arg_for_seed)
tree = BinaryTree()
for _ in range(nb_of_nodes):
    datum = randrange(1000000)
    tree.insert_in_bst(datum)
	
print('Here is the tree that has been generated:')
tree.print_binary_tree()
print('The maximum difference between consecutive leaves is: ', end = '')
print(max_diff_in_consecutive_leaves(tree))
           
