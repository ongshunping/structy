# Write a function, anagrams, that takes in two strings as a arguments. 
# The function should return a boolean indicating whether or not 
# the strings are anagrams. Anagrams are strings that contain
# the same characters, but in any order. 

# from collections import Counter 

def test_anagrams():
	assert anagrams('restful', 'fluster') == True 
	assert anagrams('cats', 'tocs') == False
	assert anagrams('monkeyswrite', 'newyorktimes') == True
	assert anagrams('paper', 'reapa') == False
	assert anagrams('elbow', 'below') == True
	assert anagrams('tax', 'taxi') == False
	assert anagrams('taxi', 'tax') == False
	assert anagrams('night', 'thing') == True
	assert anagrams('abbc', 'aabc') == False
	assert anagrams('po', 'popp') == False
	assert anagrams('pp', 'oo') == False

# def anagrams(s1, s2):
# 	return Counter(s1) == Counter(s2)

def anagrams(s1, s2):
	return char_count(s1) == char_count(s2)

def char_count(s):
	count = {}
	for char in s:
		if char not in count:
			count[char] = 0
		count[char] += 1
	return count

test_anagrams()


# Complexity 
# Let n = string1 length 
# Let m = string2 length 
# Time : O(n+m) 
# Space: ~O(n+m)
# Linear 