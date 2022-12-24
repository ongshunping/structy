# Write a function, is_univalue_list, that takes in the head of a linked_list
# as an argument. The function should return a boolean indicating whether or 
# not the linked list contains exactly one unique value. You may assume that 
# the input list is non-empty. 


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def test_is_univalue_list():
    # test_00: 
    a = Node(7)
    b = Node(7)
    c = Node(7) 
    a.next = b
    b.next = c 

    assert is_univalue_list(a) == True 

    # test_01:
    a = Node(7)
    b = Node(7)
    c = Node(4)
    a.next = b
    b.next = c 
    assert is_univalue_list(a) == False 

    # test_02: 
    u = Node(2)
    v = Node(2)
    w = Node(2)
    x = Node(2)
    y = Node(2)
    u.next = v
    v.next = w 
    w.next = x 
    x.next = y 
    assert is_univalue_list(u) == True 

    # test_03: 
    u = Node(2) 
    v = Node(2) 
    w = Node(3)
    x = Node(3) 
    y = Node(2)
    u.next = v
    v.next = w
    w.next = x
    x.next = y 
    assert is_univalue_list(u) == False 

    # test_04: 
    z = Node('z')
    assert is_univalue_list(z) == True 

# Iterative 
def is_univalue_list(head):
    current = head
    while current is not None:
        if current.val != head.val:
            return False 
        current = current.next
    return True 

# Recursive  
def is_univalue_list(head, prev_val = None):
    if head is None:
        return True 
    if prev_val is not None and head.val != prev_val:
        return False 
    return is_univalue_list(head.next, head.val)

test_is_univalue_list()


# Iterative Complexity 
# n = number of nodes 
# Time: O(n)
# Space: O(1) 

# Recursive Complexity 
# n = number of nodes 
# Time: O(n)
# Space: O(n)
