# Write a function, linked_list_find, that takes in the head of a linked list 
# and a target value. The function should return a boolean indicating 
# whether or not the linked list contains the target.


class Node:
	def __init__(self, val):
		self.val = val
		self.next = None

def test_linked_list_find():
	# test_00:
	a = Node("a")
	b = Node("b")
	c = Node("c")
	d = Node("d")
	a.next = b
	b.next = c
	c.next = d
	assert linked_list_find(a, "c") == True 

	# test_01:
	assert linked_list_find(a, "d") == True 

	# test_02: 
	assert linked_list_find(a, "q") == False

	# test_03: 
	node1 = Node("jason")
	node2 = Node("leneli")
	node1.next = node2
	assert linked_list_find(node1, "jason") == True

	# test_04: 
	node1 = Node(42)
	assert linked_list_find(node1, 42) == True

	# test_05: 
	assert linked_list_find(node1, 100) == False

# Iterative
# def linked_list_find(head, target):
# 	current = head
# 	while current is not None:
# 		if current.val == target:
# 			return True
# 		current = current.next
# 	return False 

# Recursive 
def linked_list_find(head, target):
	if head is None:
		return False 
	return head.val == target or linked_list_find(head.next, target)

test_linked_list_find()


# Iterative Complexity:
# n = number of nodes
# Time: O(n)
# Space: O(1)

# Recursive Complexity: 
# n = number of nodes 
# Time: O(n) 
# Space: O(n)