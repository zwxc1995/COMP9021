# Written by *** for COMP9021


from binary_tree_adt import *
from math import log

class PriorityQueue(BinaryTree):
	def __init__(self):
		super().__init__()

	def insert(self, value):
		if self.value is None:
			self.value=value
			self.left_node=PriorityQueue()
			self.right_node=PriorityQueue()
			return
		H9=self.size()+1
		H4=log(H9,2)//1
		H1=H2=2**H4
		H3=[]
		H3.append(self)
		while H4>1:
			H2=H2/2
			if self.size()+1>=H1+H2:
				H1=H1+H2
				self=self.right_node
			else:
				self=self.left_node
			H3.append(self)
			H4-=1
		if H9==H1+1:
			self.right_node=BinaryTree(value)
			for _ in range(len(H3)):
				H6=H3.pop()
				if self.right_node.value<H6.value:
					self.right_node.value,H6.value=H6.value,self.right_node.value
		if H9==H1:
			self.left_node=BinaryTree(value)
			for _ in range(len(H3)):
				H6=H3.pop()
				if self.left_node.value<H6.value:
					self.left_node.value,H6.value=H6.value,self.left_node.value

        # Replace pass above with your code
