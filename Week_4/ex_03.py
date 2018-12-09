import math 

def BInReader(n, k):
	return (math.factorial(n)//math.factorial(k)//math.factorial(n-k))


def B(n, k):
	if n == k or k == 0:
		return 1
	
	if k > n:
		return 0

	row = [1]
	for i in range(n):
		temp = [0] + row
		row = row + [0]

		for elementIndex in range(len(row)):
			row[elementIndex] += temp[elementIndex]

		if len(row) > k:
			row = row[0:k + 1]

	return row[k]	

print(B(4, 4))
print(B(4, 0))
print(B(6, 3))
print(B(6, 2))
print(B(6, 7))
print(B(100, 50))
print(BInReader(100, 50))

print(BInReader(100, 50) == B(100, 50))





