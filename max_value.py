# Write a function max_value, that takes in list of numbers as an argument. 
# The function should return the largest number in the list. 
# Solve this without using any built-in list methods. 
# You can assume that the list is non-empty.


def test_max_value():
	assert max_value([4, 7, 2, 8, 10, 9]) == 10 
	assert max_value([10, 5, 40, 40.3]) == 40.3 
	assert max_value([-5, -2, -1, -11]) == -1 
	assert max_value([42]) == 42 
	assert max_value([1000, 8]) == 1000
	assert max_value([1000, 8, 9000]) == 9000 
	assert max_value([2, 5, 1, 1, 4]) == 5

def max_value(nums):
	maximum = float("-inf")
	for num in nums:
		if maximum < num:
			maximum = num
	return maximum

test_max_value()


# If n = array length (number of elements in the nums list), the time 
# complexity is O(n) and the space complexity is O(1). 