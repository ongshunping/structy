# Write a function, most_frequent_char, that takes in a string
# as an argument. The function should return the most frequent 
# character of the string. If there are ties, return the character that 
# appears earlier in the string. 
# You can assume that the input string is non-empty.


def test_most_frequent_char():
	assert most_frequent_char('bookeeper') == 'e'
	assert most_frequent_char('david') == 'd'
	assert most_frequent_char('abby') == 'b'
	assert most_frequent_char('mississippi') == 'i'
	assert most_frequent_char('potato') == 'o'
	assert most_frequent_char('eleventennine') == 'e'
	assert most_frequent_char('riverbed') == 'r'

def most_frequent_char(s):
	count = {}
	for char in s:
		if char not in count:
			count[char] = 0
		count[char] += 1

	ans = None 

	for char in s:
		if ans == None or count[char] > count[ans]:
			ans = char 

	return ans 
 
test_most_frequent_char()


# Complexity
# n = string length 
# Time: O(n) 
# Space: O(n)