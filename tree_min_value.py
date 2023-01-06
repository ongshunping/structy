class Node:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

def test_tree_min_value():
	# test_00:
	a = Node(3)
	b = Node(11)
	c = Node(4)
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
	#   11     4
	#  / \      \
	# 4   -2     1

	assert tree_min_value(a) == -2

	# test_01:
	a = Node(5)
	b = Node(11)
	c = Node(3)
	d = Node(4)
	e = Node(14)
	f = Node(12)

	a.left = b
	a.right = c
	b.left = d
	b.right = e
	c.right = f

	#       5
	#    /    \
	#   11     3
	#  / \      \
	# 4   14     12

	assert tree_min_value(a) == 3

	# test_02:
	a = Node(-1)
	b = Node(-6)
	c = Node(-5)
	d = Node(-3)
	e = Node(-4)
	f = Node(-13)
	g = Node(-2)
	h = Node(-2)

	a.left = b
	a.right = c
	b.left = d
	b.right = e
	c.right = f
	e.left = g
	f.right = h

	#        -1
	#      /   \
	#    -6    -5
	#   /  \     \
	# -3   -4   -13
	#     /       \
	#    -2       -2

	assert tree_min_value(a) == -13

	# test_03:
	a = Node(42)
	assert tree_min_value(a) == 42

# Recursive 
def tree_min_value(root):
	if root is None:
		return float("inf")
	return min(root.val, tree_min_value(root.left), tree_min_value(root.right))

test_tree_min_value()

# Iterative 
from collections import deque 

def tree_min_value(root):
	queue = deque([root])
	min_value = float("inf")

	while queue:
		current = queue.popleft()
		if current.val < min_value:
			min_value = current.val
		if current.left:
			queue.append(current.left)
		if current.right:
			queue.append(current.right)

	return min_value

test_tree_min_value()

# Complexity 
# n = number of nodes 
# Time: O(n)
# Space: O(n)