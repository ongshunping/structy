# Write a function, create_linked_list, that takes in a list of values as an 
# argument. The function should create a linked list containing each item of 
# the list as the values of the nodes. The function should return the head 
# of the linked list. 


from linked_list_values import linked_list_values 

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None 

def test_create_linked_list():
    # test_00:
    assert linked_list_values(create_linked_list(["h", "e", "y"])) == ['h', 'e', 'y'] 

    # test_01:
    assert linked_list_values(create_linked_list([1, 7, 1, 8])) == [1, 7, 1, 8]

    # test_02: 
    assert linked_list_values(create_linked_list(["a"])) == ['a']

    # test_03:
    assert linked_list_values(create_linked_list([])) == [] 

def create_linked_list(values):
    dummy_head = Node(None)
    tail = dummy_head 
    for value in values:
        tail.next = Node(value)  
        tail = tail.next 
    return dummy_head.next

test_create_linked_list() 


# Complexity 
# n = number of nodes 
# Time: O(n)
# Space: O(n) 
