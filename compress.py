# Write a function, compress that takes in a string as an argument.
# The function should return a compressed version of the string 
# where consecutive occurences of the same characters are
# compressed into the number of occurences followed by the character.
# Single character occurences should not be changed. 
# You can assume that the input only contains alphabetic characters.


def test_compress():
	assert compress('ccaaatsss') == '2c3at3s'
	assert compress('ssssbbz') == '4s2bz'
	assert compress('ppoppppp') == '2po5p'
	assert compress('nnneeeeeeeeeeeezz') =='3n12e2z'
	assert compress('yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy') == '127y'

def compress(s):
	def add_character(lst, char, count):
		if count == 1:
			lst.append(char)
		else:
			lst.append(str(count))
			lst.append(char)

	result = []
	i = 0
	s += ' '
	for j in range(len(s)):
		if s[j] != s[i]:
			count = j - i 
			add_character(result, s[i], count)
			i = j

	return ''.join(result)

test_compress()


# Complexity 
# n = string length 
# Time: O(n) from loop 
# Space: O(n) from short consecutive streak 