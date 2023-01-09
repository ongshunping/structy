class Node:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

def test_how_high():
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

	assert how_high(a) == 2

	# test_01:
	a = Node('a')
	b = Node('b')
	c = Node('c')
	d = Node('d')
	e = Node('e')
	f = Node('f')
	g = Node('g')

	a.left = b
	a.right = c
	b.left = d
	b.right = e
	c.right = f
	e.left = g

	#      a
	#    /   \
	#   b     c
	#  / \     \
	# d   e     f
	#    /
	#   g

	assert how_high(a) == 3

	# test_02:
	a = Node('a')
	c = Node('c')

	a.right = c

	#      a
	#       \
	#        c

	assert how_high(a) == 1

	# test_03:
	a = Node('a')
	assert how_high(a) == 0

	# test_04:
	assert how_high(None) == -1

def how_high(root):
	if root is None:
		return -1 

	return 1 + max(how_high(root.left), how_high(root.right))
	
test_how_high()


# Complexity 
# n = number of nodes
# Time: O(n)
# Space: O(n)