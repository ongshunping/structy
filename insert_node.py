# Write a function, insert_node, that takes in the head of a linked list, a 
# value, and an index. The function should insert a new node with the value 
# into the list at the specified index. Consider the head of the linked list 
# as index 0. The function should return the head of the resulting linked 
# list. Do this in-place. 
# You may assume that the input list is non-empty and the index is not greater
# than the length of the input list. 


from linked_list_values import linked_list_values

class Node:
    def __init__(self, val):
        self.val = val 
        self.next = None 

def test_insert_node():
    # test_00: 
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")
    a.next = b
    b.next = c
    c.next = d
    assert linked_list_values(insert_node(a, 'x', 2)) == ['a', 'b', 'x', 'c', 'd'] 

    # test_01:
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")
    a.next = b
    b.next = c
    c.next = d
    assert linked_list_values(insert_node(a, 'v', 3)) == ['a', 'b', 'c', 'v', 'd']

    # test_02:
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")
    a.next = b
    b.next = c
    c.next = d
    assert linked_list_values(insert_node(a, 'm', 4)) == ['a', 'b', 'c', 'd', 'm']

    # test_03: 
    a = Node("a")
    b = Node("b")
    a.next = b
    assert linked_list_values(insert_node(a, 'z', 0)) == ['z', 'a', 'b']

# Iterative 
def insert_node(head, value, index):
    new_node = Node(value)
    if index == 0:
        new_node.next = head  
        return new_node 

    current = head 
    count = 0
    while current is not None:
        if count == index - 1:
            next = current.next 
            current.next = new_node
            new_node.next = next 
        current = current.next
        count += 1
    return head

test_insert_node()

# Recursive 
def insert_node(head, value, index, count = 0):
    if index == 0:
        new_head = Node(value)
        new_head.next = head 
        return new_head 

    if head is None:
        return None 

    if count == index - 1:
        temp = head.next 
        head.next = Node(value)
        head.next.next = temp 
        return 

    insert_node(head.next, value, index, count + 1)
    return head

test_insert_node()


# Iterative Complexity 
# n = number of nodes 
# Time: O(n) 
# Space: O(1) 

# Recursive Complexity 
# n = number of nodes 
# Time: O(n) 
# Space: O(n) 
