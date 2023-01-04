from collections import deque 

class Node:
	def __init__(self, val):
		self.val = val 
		self.left = None
		self.right = None

def test_breadth_first_values():
	# test_00:
	a = Node('a')
	b = Node('b')
	c = Node('c')
	d = Node('d')
	e = Node('e')
	f = Node('f')

	a.left = b
	a.right = c
	b.left = d
	b.right = e
	c.right = f

	#      a
	#    /   \
	#   b     c
	#  / \     \
	# d   e     f

	assert breadth_first_values(a) == ['a', 'b', 'c', 'd', 'e', 'f'] 

	# test_01: 
	a = Node('a')
	b = Node('b')
	c = Node('c')
	d = Node('d')
	e = Node('e')
	f = Node('f')
	g = Node('g')
	h = Node('h')

	a.left = b
	a.right = c
	b.left = d
	b.right = e
	c.right = f
	e.left = g
	f.right = h

	#      a
	#    /   \
	#   b     c
	#  / \     \
	# d   e     f
	#    /       \
	#   g         h

	assert breadth_first_values(a) == ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

	# test_02:
	a = Node('a')
	assert breadth_first_values(a) == ['a']

	# test_03: 
	a = Node('a')
	b = Node('b')
	c = Node('c')
	d = Node('d')
	e = Node('e')
	x = Node('x')

	a.right = b
	b.left = c
	c.left = x
	c.right = d
	d.right = e

	#      a
	#       \
	#        b
	#       /
	#      c
	#    /  \
	#   x    d
	#         \
	#          e

	assert breadth_first_values(a) == ['a', 'b', 'c', 'x', 'd', 'e']

	# test_04: 
	assert breadth_first_values(None) == [] 

# Iterative 
def breadth_first_values(root):
	if root is None:
		return [] 

	queue = deque([root])
	values = [] 
	while queue:
		current = queue.popleft()
		values.append(current.val)
		if current.left:
			queue.append(current.left)
		if current.right:
			queue.append(current.right)

	return values

test_breadth_first_values()

# Complexity 
# n = number of nodes 
# Time: O(n)
# Space: O(n) 