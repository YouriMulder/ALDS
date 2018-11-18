import sys

"""
Function to convert numbers in a string to an list of integer.
123 th1s is an 3xampl3 456 = [123, 1, 3, 3, 456].

Parameters
----------
s : str
	A string containing numbers you want to convert to a list of integers.

Returns
-------
list
	A list containing integers which are in parameter string s.
"""
def getNumbers(s):
	assert type(s) is str, "Requires a string: " + str(type(s))
	print(str(type(s)))
	numbers = []
	number = 0
	for element in s:
		if element >= '0' and element <= '9':
			number = (number * 10) + int(element)
		elif number:
			numbers.append(number)
			number = 0

	return numbers


try:
	print(getNumbers("een123zin45 6met-632meerdere+7777getallen"))
	print(getNumbers("een123zin45" + 'dit is een test 123' + "c++17_uint8_t"))
	print(getNumbers(10))
	print(getNumbers(10.1))
	print(getNumbers(["ea", 10, 1.0]))
except Exception as e:
	print('Error on line {}'.format(sys.exc_info()[-1].tb_lineno))
	print(e)
