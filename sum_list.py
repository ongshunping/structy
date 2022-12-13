# Write a function, sum_list, that takes in the head of a linked list 
# containing numbers as an argument. The function should return the 
# total sum of all values in the linked list.


class Node:
	def __init__(self, val):
		self.val = val
		self.next = None

def test_sum_list():
	# test_00:
	a = Node(2)
	b = Node(8)
	c = Node(3)
	d = Node(-1)
	e = Node(7)
	a.next = b
	b.next = c
	c.next = d
	d.next = e
	assert sum_list(a) == 19 

	# test_01: 
	x = Node(38)
	y = Node(4)
	x.next = y
	assert sum_list(x) == 42

	# test_02: 
	z = Node(100)
	assert sum_list(z) == 100

	# test_03:
	assert sum_list(None) == 0

# Iterative
def sum_list(head):
	total = 0 
	current = head
	while current is not None:
		total += current.val
		current = current.next
	return total

# Recursive
# def sum_list(head):
# 	if head is None:
# 		return 0
# 	return head.val + sum_list(head.next)

test_sum_list()


# Iterative Complexity 
# n = number of nodes
# Time: O(n)
# Space: O(1)

# Recursive Complexity
# n = number of node
# Time: O(n)
# Space: O(n) 