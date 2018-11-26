# Studentnumber : 1716390
# Class : V2C

"""
Function to calculate the power of a given digit 
using a base and exponent.

Parameters
----------
a : integer (Didn't choose the name myself. Was given in the reader)
	The base where you want to calculate the power of.

n : integer (Didn't choose the name myself. Was given in the reader)
	The exponent where you want to calculate the power of.

Returns
-------
integer
	This integer contains the power of the given base and exponent.
"""
def machtv3(a, n):
	assert n > 0, "n must be > 1"
	multiplyCounter = 0
	m = 1
	while n > 0:
		if n%2 == 0:
			a *= a
			n /= 2
			multiplyCounter += 1 
		else:
			m *= a
			n -= 1
			multiplyCounter += 1 

	print("amount of multiplies: ", multiplyCounter)
	return m

print("3**5", machtv3(3, 5) == 3**5)
print("5**7", machtv3(5, 7) == 5**7)
print("1**2", machtv3(1, 2) == 1**2)
print("0**2", machtv3(0, 2) == 0**2)
print("111**234", machtv3(111, 234) == 111**234)
print("1234**1234", machtv3(1234, 1234) == 1234**1234)
print("-3**3", machtv3(-3, 3) == -3**3)
#print("2**-2", machtv3(2, -2) == 2**-2) assert

# amount of multiplies with n = 10'000 is 18
print("2**10000", machtv3(2, 10000) == 2**10000)