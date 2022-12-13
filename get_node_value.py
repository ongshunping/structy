# Write a function, get_node_value, that takes in the head of a linked list 
# and an index. The function should return the value of the linked list at 
# the specified index.
# If there is no node at the given index, then return None.


class Node:
	def __init__(self, val):
		self.val = val
		self.next = None

def test_get_node_value():
	# test_00:
	a = Node("a")
	b = Node("b")
	c = Node("c")
	d = Node("d")
	a.next = b
	b.next = c
	c.next = d
	assert get_node_value(a, 2) == 'c'

	# test_01:
	assert get_node_value(a, 3) == 'd'

	# test_02: 
	assert get_node_value(a, 7) == None

	# test_03:
	node1 = Node("banana")
	node2 = Node("mango")
	node1.next = node2
	assert get_node_value(node1, 0) == 'banana'

	# test_04: 
	assert get_node_value(node1, 1) == 'mango'

# Iterative
# def get_node_value(head, index):
# 	count = 0
# 	current = head 
# 	while current is not None:
# 		if count == index:
# 			return current.val
# 		count += 1
# 		current = current.next
# 	return None 

# Recursive
def get_node_value(head, index):
	if head is None:
		return None 
	if index == 0:
		return head.val
	return get_node_value(head.next, index - 1)
	
test_get_node_value()


# Iterative Complexity 
# n = number of nodes 
# Time: O(n)
# Space: O(1) 

# Recursive Complexity 
# n = number of nodes 
# Time: O(n)
# Space: O(n)