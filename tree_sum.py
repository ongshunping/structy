class Node:
	def __init__(self, val):
		self.val = val 
		self.left = None
		self.right = None

def test_tree_sum():
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

	assert tree_sum(a) == 21 

	# test_01: 
	a = Node(1)
	b = Node(6)
	c = Node(0)
	d = Node(3)
	e = Node(-6)
	f = Node(2)
	g = Node(2)
	h = Node(2)

	a.left = b
	a.right = c
	b.left = d
	b.right = e
	c.right = f
	e.left = g
	f.right = h

	#      1
	#    /   \
	#   6     0
	#  / \     \
	# 3   -6    2
	#    /       \
	#   2         2

	assert tree_sum(a) == 10 

	# test_02: 
	assert tree_sum(None) == 0

# Recursive 
def tree_sum(root):
	if root is None:
		return 0 
	left_sum = tree_sum(root.left)
	right_sum = tree_sum(root.right)
	return root.val + left_sum + right_sum 

test_tree_sum()

# Iterative 
def tree_sum(root):
	if root is None:
		return 0 

	stack = [root] 
	total = 0 
	while stack:
		current = stack.pop()
		total += current.val
		if current.left:
			stack.append(current.left)
		if current.right:
			stack.append(current.right)

	return total

test_tree_sum()

# Complexity 
# n = number of nodes 
# Time: O(n)
# Space: O(n)