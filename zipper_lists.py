# Write a function, zipper_lists, that takes in the head of two linked lists
# as arguments. The function should zipper the two lists together into 
# single linked list by alternating nodes. If one of the linked lists is 
# longer than the other, the resulting list should terminate with the 
# remaining nodes. The function should return the head of the zippered 
# linked list.
# Do this in-place, by mutating the original Nodes. 
# You may assume that both input lists are non-empty.


from linked_list_values import linked_list_values

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def test_zipper_lists():
    # test_00:
    a = Node("a")
    b = Node("b")
    c = Node("c")
    a.next = b
    b.next = c

    x = Node("x")
    y = Node("y")
    z = Node("z")
    x.next = y
    y.next = z

    assert linked_list_values(zipper_lists(a, x)) == ['a', 'x', 'b', 'y', 'c', 'z']

    # test_01: 
    d = Node("d")
    e = Node("e")
    f = Node("f")
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f

    x = Node("x")
    y = Node("y")
    z = Node("z")
    x.next = y
    y.next = z

    assert linked_list_values(zipper_lists(a, x)) == ['a', 'x', 'b', 'y', 'c', 'z', 'd', 'e', 'f']

    #test_02: 
    s = Node("s")
    t = Node("t")
    s.next = t

    one = Node(1)
    two = Node(2)
    three = Node(3)
    four = Node(4)
    one.next = two
    two.next = three
    three.next = four

    assert linked_list_values(zipper_lists(s, one)) == ['s', 1, 't', 2, 3, 4]

    #test_03: 
    w = Node("w")
    assert linked_list_values(zipper_lists(w, one)) == ['w', 1, 't', 2, 3, 4]

# Iterative 
def zipper_lists(head_1, head_2):
    tail = head_1 
    current_1 = head_1.next
    current_2 = head_2 
    count = 0 

    while current_1 is not None and current_2 is not None:
        if count % 2 == 0:
            tail.next = current_2
            current_2 = current_2.next 
        else:
            tail.next = current_1 
            current_1 = current_1.next 
        tail = tail.next
        count += 1 

    if current_1 is not None:
        tail.next = current_1
    if current_2 is not None:
        tail.next = current_2 

    return head_1

# Recursive 
# def zipper_lists(head_1, head_2):
#     if head_1 is None and head_2 is None:
#         return None 
#     if head_1 is None:
#         return head_2
#     if head_2 is None:
#         return head_1

#     next_1 = head_1.next
#     next_2 = head_2.next

#     head_1.next = head_2
#     head_2.next = zipper_lists(next_1, next_2)

#     return head_1 

test_zipper_lists()


# Iterative Complexity 
# n = length of list 1 
# m = lengoth of list 2 
# Time: O(min(n, m))
# Space: O(1) 

# Recursive Complexity 
# n = length of list 1 
# m = length of list 2 
# Time: O(min(n, m))
# Space: O(min(n, m))
