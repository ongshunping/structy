# Write a function, pair_product, that takes in a list and a 
# target product as arguments. The function should return a
# tuple containing a pair of indices whose elements multiply
# to the given target. The indices returned must be uniqued.
# There is guaranteed to be one such pair whose product is the target.


def test_pair_product():
	assert pair_product([3, 2, 5, 4, 1], 8) == (1, 3)
	assert pair_product([3, 2, 5, 4, 1], 10) == (1, 2)
	assert pair_product([4, 7, 9, 2, 5, 1], 5) == (4, 5)
	assert pair_product([4, 7, 9, 2, 5, 1], 35) == (1, 4)
	assert pair_product([3, 2, 5, 4, 1], 10) == (1, 2)
	assert pair_product([4, 6, 8, 2], 16) == (2, 3)

def pair_product(numbers, target_product):
	previous_nums = {}
	for index, num in enumerate(numbers):
		complement = target_product / num
		if complement in previous_nums:
			return (previous_nums[complement], index)
		previous_nums[num] = index

test_pair_product()


# Complexity 
# n = array length 
# Time: O(n) 
# Space: O(n) 