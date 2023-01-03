# Write a function, add_lists, that takes in the head of two linked lists, 
# each representing a number. The nodes of the linked lists contain digits as 
# values. The nodes in the input lists are reversed; this means that the least
# significant digit of the number is the head. The function should return the 
# head of a new linked list representing the sum of the input lists. The output
# list should have its digit reversed as well. 


from linked_list_values import linked_list_values

class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def test_add_lists():
	# test_00:
	a1 = Node(1)
	a2 = Node(2)
	a3 = Node(6)
	a1.next = a2
	a2.next = a3
	b1 = Node(4)
	b2 = Node(5)
	b3 = Node(3)
	b1.next = b2
	b2.next = b3
	assert linked_list_values(add_lists(a1, b1)) == [5, 7, 9]

	# test_01:
	a1 = Node(1)
	a2 = Node(4)
	a3 = Node(5)
	a4 = Node(7)
	a1.next = a2
	a2.next = a3
	a3.next = a4
	b1 = Node(2)
	b2 = Node(3)
	b1.next = b2
	assert linked_list_values(add_lists(a1, b1)) == [3, 7, 5, 7]

	# test_02: 
	a1 = Node(9)
	a2 = Node(3)
	a1.next = a2
	b1 = Node(7)
	b2 = Node(4)
	b1.next = b2
	assert linked_list_values(add_lists(a1, b1)) == [6, 8]

	# test_03: 
	a1 = Node(9)
	a2 = Node(8)
	a1.next = a2
	b1 = Node(7)
	b2 = Node(4)
	b1.next = b2
	assert linked_list_values(add_lists(a1, b1)) == [6, 3, 1]

	# test_04: 
	a1 = Node(9)
	a2 = Node(9)
	a3 = Node(9)
	a1.next = a2
	a2.next = a3
	b1 = Node(6)
	assert linked_list_values(add_lists(a1, b1)) == [5, 0, 0, 1]

# Recursive 
def add_lists(head_1, head_2, carry = 0):
	if head_1 is None and head_2 is None and carry == 0:
		return None

	value_1 = 0 if head_1 is None else head_1.val 
	value_2 = 0 if head_2 is None else head_2.val 
	value = value_1 + value_2 + carry
	digit = value % 10 
	result = Node(digit)
	next_carry = value // 10

	next_1 = None if head_1 is None else head_1.next 
	next_2 = None if head_2 is None else head_2.next
	result.next = add_lists(next_1, next_2, next_carry)
	return result

test_add_lists()

# Iterative 
def add_lists(head_1, head_2):
	dummy_head = Node(None)
	tail = dummy_head 
	carry = 0 
	current_1 = head_1 
	current_2 = head_2 

	while current_1 is not None or current_2 is not None or carry == 1:
		val_1 = 0 if current_1 is None else current_1.val
		val_2 = 0 if current_2 is None else current_2.val 
		val = val_1 + val_2 + carry 
		digit = val % 10 
		carry = val // 10 
		tail.next = Node(digit)
		tail = tail.next 

		current_1 = current_1.next if current_1 is not None else current_1
		current_2 = current_2.next if current_2 is not None else current_2

	return dummy_head.next

test_add_lists()


# Complexity 
# n = length of list 1 
# m = length of list 2 
# Time: O(max(n, m))
# Space: O(max(n, m))