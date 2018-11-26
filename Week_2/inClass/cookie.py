# Studentnumber : 1716390
# Class : V2C

def cookies(k, A):
	counter = 0
	while len(A) > 1 and (min(A) < k):
		a = min(A)
		A.pop(A.index(a))
		b = min(A)
		A.pop(A.index(b))


		newCookie = a + (2 * b)
		A[A.index(a)] = newCookie

		a = min(A)
		counter += 1

	if len(A) > 0 and min(A) >= k:
		return counter
	else:
		return -1



#k = 1000
#A = list(range(10 ** 6))

#A = [1,2,3,9,10,12,3]

#k = 1000
#A = [1000, -1, -1, -1 , -1 , -1 ,- 10]

k = 12
A = [6,7,9,21,3,4,5,7,10,11,13,2,2,2,2,2,2]


result = cookies(k, A)
print(result)

# waarde hoger dan of gelijk aan k