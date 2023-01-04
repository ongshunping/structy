class Node:
	def __init__(self, val):
		self.val = val
		self.left = None 
		self.right = None 

def test_depth_first_values():
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

	assert depth_first_values(a) == ['a', 'b', 'd', 'e', 'c', 'f']

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

	assert depth_first_values(a) == ['a', 'b', 'd', 'e', 'g', 'c', 'f']

	# test_02: 
	a = Node('a')
	assert depth_first_values(a) == ['a']

	# test_03: 
	a = Node('a')
	b = Node('b')
	c = Node('c')
	d = Node('d')
	e = Node('e')
	a.right = b;
	b.left = c;
	c.right = d;
	d.right = e;

	#      a
	#       \
	#        b
	#       /
	#      c
	#       \
	#        d
	#         \
	#          e

	assert depth_first_values(a) == ['a', 'b', 'c', 'd', 'e']

	# test_04:
	assert depth_first_values(None) == []

# Recursive 
def depth_first_values(root):
	if root is None:
		return [] 
	left_values = depth_first_values(root.left)
	right_values = depth_first_values(root.right)
	return [root.val, *left_values, *right_values]

test_depth_first_values()

# Iterative 
def depth_first_values(root):
	if root is None:
		return [] 

	stack = [root]
	values = [] 
	while stack:
		current = stack.pop()
		values.append(current.val)
		if current.right is not None:
			stack.append(current.right)
		if current.left is not None:
			stack.append(current.left)

	return values

test_depth_first_values()

# Complexity 
# n = number of nodes 
# Time: O(n)
# Space: O(n)