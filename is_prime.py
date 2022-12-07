# Write a function is_prime, that takes in a number as an argument. 
# The function should return a boolean indicating if the given number is prime.
# You can assume that the input number is a positive integer.


def test_is_prime():
	assert is_prime(2) == True 
	assert is_prime(3) == True 
	assert is_prime(4) == False 
	assert is_prime(5) == True 
	assert is_prime(6) == False 
	assert is_prime(7) == True 
	assert is_prime(8) == False 
	assert is_prime(25) == False 
	assert is_prime(31) == True 
	assert is_prime(2017) == True 
	assert is_prime(2048) == False 
	assert is_prime(1) == False 
	assert is_prime(713) == False 

from math import sqrt, floor

def is_prime(n):
	if n < 2:
		return False 
	for i in range(2, floor(sqrt(n)) + 1):
		if n % i == 0:
			return False 
	return True 

test_is_prime()


# Time complexity: O(sqrt(n))
# Space complexity: O(1) 