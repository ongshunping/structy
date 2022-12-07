# Write a function uncompress, that takes in a string as an argument. 
# The input string will be formatted into multiple groups according to the 
# following pattern: <number><char> for example, '2c' or '3a'. 
# The function should return an uncompressed version of the string where 
# each 'char' of a group is repeated 'number' times consecutively. 


def test_uncompress():
	assert uncompress("2c3a1t") == "ccaaat"
	assert uncompress("4s2b") == "ssssbb"
	assert uncompress("2p1o5p") == "ppoppppp"
	assert uncompress("3n12e2z") == "nnneeeeeeeeeeeezz"
	assert uncompress("127y") == "yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy"

def uncompress(s):
	result = []
	i = 0
	for j in range(len(s)):
		if s[j].isalpha():
			number = int(s[i:j])
			result.append(s[j] * number)
			i = j + 1 
	return ''.join(result)

test_uncompress()


# Imagine 1000p1000q and 1a1b1c1d1e. Input sizes are both 10 
# but the output size is 2000 for 1000p1000q and 5 for 1a1b1c1d1e. 
# Let n = number of groups and m = max number for any groups. 
# Time complexity: O(nm) 
# Space complexity: O(nm)