# Studentnumber : 1716390
# Class : V2C

"""
Function to get the maximum value of a 
list full of integers or/and floats.

Parameters
----------
n : integer (Didn't choose the name myself. Was given in the reader)
	The integer you want to get the binary representation of.

Returns
-------
String:
	This string contains the binary representation of n.
"""
def myBin(n):
	assert type(n) == int, "Requires an integer" + str(type(n))
	assert n >= 0, "Requires n to be positive" + n
	if n <= 0:
		return ''

	return myBin(int(n / 2)) + str(n % 2)
	
print(myBin(127))
print(myBin(1))
print(myBin(2))
print(myBin(16))
print(myBin(32))
print(myBin(101))