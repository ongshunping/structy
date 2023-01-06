class Node:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

def test_max_path_sum():
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

	assert max_path_sum(a) == 18

	# test_01:
	a = Node(5)
	b = Node(11)
	c = Node(54)
	d = Node(20)
	e = Node(15)
	f = Node(1)
	g = Node(3)

	a.left = b
	a.right = c
	b.left = d
	b.right = e
	e.left = f
	e.right = g

	#        5
	#     /    \
	#    11    54
	#  /   \      
	# 20   15
	#      / \
	#     1  3

	assert max_path_sum(a) == 59

	# test_02:
	a = Node(-1)
	b = Node(-6)
	c = Node(-5)
	d = Node(-3)
	e = Node(0)
	f = Node(-13)
	g = Node(-1)
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
	# -3   0    -13
	#     /       \
	#    -1       -2

	assert max_path_sum(a) == -8

	# test_03:
	a = Node(42)
	assert max_path_sum(a) == 42

# Recursive 
def max_path_sum(root):
	if root is None:
		return float("-inf")

	if root.left is None and root.right is None:
		return root.val

	left_max_path_sum = max_path_sum(root.left)
	right_max_path_sum = max_path_sum(root.right)

	return root.val + max(left_max_path_sum, right_max_path_sum)

test_max_path_sum()


# Complexity 
# n = number of nodes 
# Time: O(n)
# Space: O(n)