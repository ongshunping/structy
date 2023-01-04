class Node:
	def __init__(self, val):
		self.val = val 
		self.left = None
		self.right = None

def test_tree_includes():
	# test_00:
	a = Node("a")
	b = Node("b")
	c = Node("c")
	d = Node("d")
	e = Node("e")
	f = Node("f")

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

	assert tree_includes(a, "e") == True

	# test_01: 
	a = Node("a")
	b = Node("b")
	c = Node("c")
	d = Node("d")
	e = Node("e")
	f = Node("f")

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

	assert tree_includes(a, "a") == True

	# test_02: 
	a = Node("a")
	b = Node("b")
	c = Node("c")
	d = Node("d")
	e = Node("e")
	f = Node("f")

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

	assert tree_includes(a, "n") == False

	# test_03: 
	a = Node("a")
	b = Node("b")
	c = Node("c")
	d = Node("d")
	e = Node("e")
	f = Node("f")
	g = Node("g")
	h = Node("h")

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

	assert tree_includes(a, "f") == True

	# test_04:
	a = Node("a")
	b = Node("b")
	c = Node("c")
	d = Node("d")
	e = Node("e")
	f = Node("f")
	g = Node("g")
	h = Node("h")

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

	assert tree_includes(a, "p") == False

	# test_05: 
	assert tree_includes(None, "b") == False

# Recursive 
def tree_includes(root, target):
	if root is None:
		return False

	if root.val == target:
		return True 

	return tree_includes(root.left, target) or tree_includes(root.right, target)

test_tree_includes()

# Iterative 
from collections import deque

def tree_includes(root, target):
	if root is None:
		return False 

	queue = deque([root])
	while queue:
		current = queue.popleft()
		if current.val == target:
			return True 

		if current.left:
			queue.append(current.left)
		if current.right:
			queue.append(current.right)

	return False 

test_tree_includes()


# Complexity 
# n = number of nodes
# Time: O(n)
# Space: O(n)