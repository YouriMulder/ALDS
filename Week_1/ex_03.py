# Name : Youri Mulder
# Studentnumber : 1716390
# Class : V2C
# Teacher : Frits Dannenberg

# Testing done:
# Compared to https://primes.utm.edu/lists/small/10000.txt
# Used different maxNumbers and compared those against the site.
#
# Used different maxNumber parameter types like: str, list, float and int to check the assert.

"""
Function to generate a list of prime numbers up to a given number.
This is done using the sieve of Eratosthenes algorithm.

Parameters
----------
maxNumber : int
	The highest value you possibly want in the generated prime list. 

Returns
-------
list
	A list containing all the prime numbers up to the parameter maxNumber.
"""
def createPrimeList(maxNumber):
	assert type(maxNumber) is int, "Requires an integer: " + type(maxNumber)

	listSize = maxNumber + 1 
	numbers = range(listSize)
	marked = [True] * listSize
	marked[0] = False
	marked[1] = False
	
	
	lowestNewNumber = 2
	while lowestNewNumber < len(numbers):
		if marked[lowestNewNumber]:
			for i in range(lowestNewNumber * 2, maxNumber + 1, lowestNewNumber):
				marked[i] = False

		lowestNewNumber += 1

	return [numbers[i] for i in range(len(numbers)) if marked[i]]

print(createPrimeList(1000))