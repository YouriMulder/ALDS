import sys
from random import randint

#Genereer honderd keer een lijst van 23 random gehele getallen tussen de 1 en de 365.
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