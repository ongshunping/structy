# Write a function, linked_list_values, that takes in the head 
# of a linked list as an argument. The function should return 
# a list containing all values of the nodes in the linked list.


def test_linked_list_values():
	## test_00:
	a = Node("a")
	b = Node("b")
	c = Node("c")
	d = Node("d")

	a.next = b
	b.next = c
	c.next = d
	assert linked_list_values(a) == ['a', 'b', 'c', 'd']

	## test_01:
	x = Node("x")
	y = Node("y")

	x.next = y
	assert linked_list_values(x) == ['x', 'y']

	## test_02: 
	q = Node("q")
	assert linked_list_values(q) == ['q']

	## test_03: 
	assert linked_list_values(None) == []

class Node:
	def __init__(self, val):
		self.val = val
		self.next = None 

# Iterative
# def linked_list_values(head):
# 	values = []
# 	current = head
# 	while current is not None:
# 		values.append(current.val)
# 		current = current.next
# 	return values

# Recursive
def linked_list_values(head):
	values = []
	fill_values(head, values)
	return values

def fill_values(head, values):
	current = head
	if current is None:
		return
	values.append(current.val)
	fill_values(current.next, values)

test_linked_list_values()


# Complexity
# n = number of node 
# Time: O(n)
# Space: O(n)