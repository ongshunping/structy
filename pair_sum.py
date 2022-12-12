# Write a function, pair_sum, that takes in a list and a target sum
# as arguements. The function should return a tuple containing 
# a pair of indices whose elements sum to the given target. The
# indices return must be unique. 
# There is guaranteed to be one such pair that sums to the target.


def test_pair_sum():
	assert pair_sum([3, 2, 5, 4, 1], 8) == (0, 2)
	assert pair_sum([4, 7, 9, 2, 5, 1], 5) == (0, 5)
	assert pair_sum([4, 7, 9, 2, 5, 1], 3) == (3, 5)
	assert pair_sum([1, 6, 7, 2], 13) == (1, 2)
	assert pair_sum([9, 9], 18) == (0, 1)
	assert pair_sum([6, 4, 2, 8 ], 12) == (1, 3)

def pair_sum(numbers, target_sum):
	previous = {}
	for index, num in enumerate(numbers):
		complement = target_sum - num
		if complement in previous:
			return (previous[complement], index)
		previous[num] = index

test_pair_sum()


# Complexity
# n = array length 
# Time: O(n) 
# Space: O(n) 