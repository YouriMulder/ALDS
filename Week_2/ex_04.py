def myBin(n):
	assert type(n) == int, "Requires an integer" + str(type(n))
	assert n >= 0, "Requires n to be positive" + n
	if n <= 0:
		return ''

	return myBin(int(n / 2)) + str(n % 2)
	
print(myBin(127))