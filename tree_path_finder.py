class Node:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

def test_path_finder():
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

	assert path_finder(a, 'e') == [ 'a', 'b', 'e' ]

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

	assert path_finder(a, 'p') == None

	# test_02:
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

	assert path_finder(a, "c") == ['a', 'c']

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

	assert path_finder(a, "h") == ['a', 'c', 'f', 'h']

	# test_04:
	x = Node("x")
	assert path_finder(x, "x") == ['x']

	# test_05:
	assert path_finder(None, "x") == None

def path_finder(root, target):
	paths = _path_finder(root, target)
	if paths is None:
		return None
	else:
		return paths[::-1]

def _path_finder(root, target):
	if root is None:
		return None 
	if root.val == target:
		return [root.val]

	paths = _path_finder(root.left, target) or _path_finder(root.right, target)
	if paths is not None:
		paths.append(root.val)

	return paths

test_path_finder()


# Complexity 
# n = number of nodes 
# Time: O(n)
# Space: O(n)