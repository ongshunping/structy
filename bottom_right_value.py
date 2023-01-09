class Node:
	def __init__(self, val):
		self.val = val 
		self.left = None
		self.right = None

def test_bottom_right_value():
	# test_00:
	a = Node(3)
	b = Node(11)
	c = Node(10)
	d = Node(4)
	e = Node(-2)
	f = Node(1)

	a.left = b
	a.right = c
	b.left = d
	b.right = e
	c.right = f

	#       3
	#    /    \
	#   11     10
	#  / \      \
	# 4   -2     1

	assert bottom_right_value(a) == 1

	# test_01:
	a = Node(-1)
	b = Node(-6)
	c = Node(-5)
	d = Node(-3)
	e = Node(-4)
	f = Node(-13)
	g = Node(-2)
	h = Node(6)

	a.left = b
	a.right = c
	b.left = d
	b.right = e
	c.right = f
	e.left = g
	e.right = h

	#        -1
	#      /   \
	#    -6    -5
	#   /  \     \
	# -3   -4   -13
	#     / \       
	#    -2  6

	assert bottom_right_value(a) == 6

	# test_02:
	a = Node(-1)
	b = Node(-6)
	c = Node(-5)
	d = Node(-3)
	e = Node(-4)
	f = Node(-13)
	g = Node(-2)
	h = Node(6)
	i = Node(7)

	a.left = b
	a.right = c
	b.left = d
	b.right = e
	c.right = f
	e.left = g
	e.right = h
	f.left = i

	#        -1
	#      /   \
	#    -6    -5
	#   /  \     \
	# -3   -4   -13
	#     / \    /   
	#    -2  6  7 

	assert bottom_right_value(a) == 7

	# test_03:
	a = Node('a')
	b = Node('b')
	c = Node('c')
	d = Node('d')
	e = Node('e')
	f = Node('f')

	a.left = b
	a.right = c
	b.right = d
	d.left = e
	e.right = f

	#      a
	#    /   \ 
	#   b     c
	#    \
	#     d
	#    /
	#   e
	#  /
	# f
	          
	assert bottom_right_value(a) == 'f'

	# test_04:
	a = Node(42)
	assert bottom_right_value(a) == 42

from collections import deque 

def bottom_right_value(root):
	queue = deque([root])

	while queue:
		current = queue.pop()
		if current.left:
			queue.appendleft(current.left)
		if current.right:
			queue.appendleft(current.right)

	return current.val

test_bottom_right_value()


# Complexity
# n = number of nodes
# Time: O(n)
# Space: O(n)