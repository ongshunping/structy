# Write a function, reverse_list, that takes in the head of a linked list 
# as an argument. The function should reverse the order of the nodes in the 
# linked list in-place and return the new head of the reversed linked list.


from linked_list_values import linked_list_values

class Node:
	def __init__(self, val):
		self.val = val
		self.next = None 

def test_reverse_list():
	# test_00:
	a = Node("a")
	b = Node("b")
	c = Node("c")
	d = Node("d")
	e = Node("e")
	f = Node("f")
	a.next = b
	b.next = c
	c.next = d
	d.next = e
	e.next = f
	assert linked_list_values(reverse_list(a)) == ['f', 'e', 'd', 'c', 'b', 'a']

	# test_01: 
	x = Node("x")
	y = Node("y")
	x.next = y
	assert linked_list_values(reverse_list(x)) == ['y', 'x'] 

	# test_02: 
	p = Node("p")
	assert linked_list_values(reverse_list(p)) == ['p']

# Iterative
#def reverse_list(head):
#    prev = None 
#    current = head 
#    while current is not None:
#        next = current.next 
#        current.next = prev 
#        prev = current 
#        current = next
#    return prev

# Recursive 
def reverse_list(head, prev = None):
    if head is None:
        return prev 
    next = head.next
    head.next = prev 
    return reverse_list(next, head)

test_reverse_list()


# Iterative Complexity 
# n = number of nodes 
# Time: O(n) 
# Space: O(1)

# Recursive Complexity
# n = number of nodes 
# Time: O(n)
# Space: O(n) 
