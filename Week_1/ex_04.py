# Name : Youri Mulder
# Studentnumber : 1716390
# Class : V2C
# Teacher : Frits Dannenberg

# Testing done:
# Placed the function call in a for loop to check if the result is almost the same every time.
# It should not be exactly the same, but it should be close.
#
# Used different amountOfLists and amountOfPeople types like: str, list, float and int to check the asserts.

import sys
from random import randint

"""
Function to approximate the amount of times 
two people have the same birthday in a group.

Parameters
----------
amountOfLists : int
	The amount of lists you want to generate and check for duplicates.

amountOfPeople : int
	The amount of people a list must contain. (The amount of possible different birthdays)

Returns
-------
	A integer containing the amount of time a the list was a double.
"""
def birthdayParadox(amountOfLists, amountOfPeople):
	assert type(amountOfLists) is int, "Requires an integer: " + type(amountOfLists)
	assert type(amountOfPeople) is int, "Requires an integer: " + type(amountOfPeople)
	
	birthdayTest = []
	for i in range(amountOflists):
		innerList = []
		for j in range(amountOfPeople):
			innerList.append(randint(1,365))
		birthdayTest.append(innerList)

	amountOfDuplicates = 0
	for lst in birthdayTest:
		amountOfDuplicates += len(lst) != len(set(lst))

	return amountOfDuplicates

amountOflists = 100
amountOfPeople = 23
totalAmountOfDuplicates = 0

for amountOfTries in range(1, 11):
	totalAmountOfDuplicates += birthdayParadox(amountOflists, amountOfPeople)
	print(amountOfTries, ":", int(totalAmountOfDuplicates / amountOfTries))