# Write a function, longest_streak, that takes in the head of a linked list 
# as an argument. The function should return the length of the longest 
# consecutive streak of the same value within the list. 


class Node:
    def __init__(self, val):
        self.val = val 
        self.next = None 

def test_longest_streak():
    # test_00:
    a = Node(5)
    b = Node(5)
    c = Node(7) 
    d = Node(7) 
    e = Node(7) 
    f = Node(6) 
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f 
    assert longest_streak(a) == 3 

    # test_01:
    a = Node(3)
    b = Node(3) 
    c = Node(3)
    d = Node(3) 
    e = Node(9) 
    f = Node(9) 
    a.next = b
    b.next = c 
    c.next = d 
    d.next = e 
    e.next = f 
    assert longest_streak(a) == 4 

    # test_02:
    a = Node(9)
    b = Node(9) 
    c = Node(1) 
    d = Node(9) 
    e = Node(9) 
    f = Node(9)
    a.next = b 
    b.next = c 
    c.next = d
    d.next = e 
    e.next = f 
    assert longest_streak(a) == 3 

    # test_03: 
    a = Node(5)
    b = Node(5) 
    a.next = b 
    assert longest_streak(a) == 2 

    # test_04:
    a = Node(4) 
    assert longest_streak(a) == 1

    # test_05: 
    assert longest_streak(None) == 0

# Iterative 
def longest_streak(head):
    current = head
    max_streak = 0 
    current_streak = 0 
    prev_val = None 

    while current is not None:
        if prev_val == current.val:
            current_streak += 1 
        else:
            current_streak = 1 
            prev_val = current.val

        if max_streak < current_streak:
            max_streak = current_streak 

        current = current.next 

    return max_streak 

test_longest_streak()


# Iterative Complexity 
# n = number of nodes 
# Time: O(n) 
# Space: O(1) 
