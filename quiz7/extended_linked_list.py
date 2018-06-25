# Written by **** for COMP9021

from linked_list_adt import *

class ExtendedLinkedList(LinkedList):
	def __init__(self, L = None):
		super().__init__(L)

	def rearrange(self):
		if len(self)<3:
			return
		node=self.head
		H1=node.next_node.value
		H3=self.head
		while node.next_node.next_node:
			if H1>node.next_node.next_node.value:
				H1=node.next_node.next_node.value
				self.head=node
			node=node.next_node
		node.next_node.next_node=H3
		H4=self.head.next_node
		self.head.next_node=None
		self.head=H4
		H5=self.head
		even_node=self.head
		odd_node=self.head.next_node
		H6=self.head.next_node
		begin_even=even_node
		while True:
			if even_node.next_node and even_node.next_node.next_node:
				even_node.next_node=even_node.next_node.next_node
				even_node=even_node.next_node
			else:
				break
			if odd_node.next_node and odd_node.next_node.next_node:
				odd_node.next_node=odd_node.next_node.next_node
				odd_node=odd_node.next_node
			else:
				break
		self.head=H6
		odd_node.next_node=begin_even
		even_node.next_node=None
		while self.head.next_node!=H5:
			even_node=self.head
			odd_node=self.head.next_node
			begin_odd=odd_node
			while True:
				if even_node.next_node and even_node.next_node.next_node:
					even_node.next_node=even_node.next_node.next_node
					even_node=even_node.next_node
				else:
					break
				if odd_node.next_node and odd_node.next_node.next_node:
					odd_node.next_node=odd_node.next_node.next_node
					odd_node=odd_node.next_node
				else:
					break
			even_node.next_node=begin_odd
			odd_node.next_node=None
        # Replace pass above with your code
    
    
    
