# Write a function, intersection, that takes in two lists, a and b, 
# as arguments. The function should return a new list containing 
# elements that are in both of the two lists. 
# You may assume that each input list does not contain duplicate elements.


def test_intersection():
	assert intersection([4,2,1,6], [3,6,9,2,10]) == [2,6]
	assert intersection([2,4,6], [4,2]) == [2,4]
	assert intersection([4,2,1], [1,2,4,6]) == [1,2,4]
	assert intersection([0,1,2], [10,11]) == []
	a = [ i for i in range(0, 50000) ]
	b = [ i for i in range(0, 50000) ]
	assert intersection(a, b) == [ i for i in range(0, 50000) ]

def intersection(a, b):
	a = set(a)
	return [ num for num in b if num in a ]


# Complexity 
# n = length of array a 
# m = length of array b 
# Time: O(n+m). n from creating the set and m from iterating 
# Space: O(n) 