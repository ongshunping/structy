# Write a function greet that takes in a string argument s and 
# returns the string "hey s". 


def test_greet():
	assert greet('alvin') == 'hey alvin'
	assert greet('jason') == 'hey jason'
	assert greet('how now brown cow') == 'hey how now brown cow'

def greet(s):
	return f'hey {s}'

test_greet()