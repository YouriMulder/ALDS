def NumberOFwaysToSpentMoney(cents):
	m = [1,2,5,10,20,50,100,200,500,1000,2000,5000,10000]
	
	if cents > m[-1]:
		return None

	A = [[1] * (cents + 1)]
	for i in range(1, len(m)):
		A.append([1] * (cents + 1))
		for j in range( len(A[i]) ):
			if j >= m[i]: 
				A[i][j] = A[i-1][j] + A[i][j-m[i]]
			else:
				A[i][j] = A[i-1][j]
		
		if m[i + 1] > cents:
			break

	lastTest = A[len(A) - 1]
	return lastTest[len(lastTest) - 1]



print(NumberOFwaysToSpentMoney(7))
print(NumberOFwaysToSpentMoney(8))
print(NumberOFwaysToSpentMoney(9))
print(NumberOFwaysToSpentMoney(10))
print(NumberOFwaysToSpentMoney(11))
print(NumberOFwaysToSpentMoney(100))
print(NumberOFwaysToSpentMoney(10001))
