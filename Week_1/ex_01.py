# Name : Youri Mulder
# Studentnumber : 1716390
# Class : V2C
# Teacher : Frits Dannenberg

# Testing done:
# Checked if the printed value is what I expected.
# Used different a parameter types like: str, list, float and int to check the asserts.


import sys

"""
Function to get the maximum value of a 
list full of integers or/and floats.

Parameters
----------
a : list
	A list containing floats or integers 
	you want to get the highest value of.

Returns
-------
int/float
	The highest value in the parameter a.
"""
def myMax(a):
	assert hasattr(a, '__len__'), "Requires a len method: " + str(type(a))
	assert len(a) != 0, "List a is empty, length: " + str(len(a))
	max = a[0]
	for element in a:
		assert type(element) is int or type(element) is float, "Element is not int or float: " + str(type(element))
		if element > max: max = element
	return max

try:
	print(myMax([10,101]))
	print(myMax([1.1, 1.5, 100.1, 10]))
	#print(myMax([10, 10.1, "foo", "bar"]))
	#print(myMax(int(10)))
	#print(myMax(float(1.1)))
except Exception as e:
	print('Error on line {}'.format(sys.exc_info()[-1].tb_lineno))
	print(e)