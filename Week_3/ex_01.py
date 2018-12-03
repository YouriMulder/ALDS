def check(a,i):  # ga na of i aan a toegevoegd kan worden
    n = len(a)
    return not (i in a or # niet in dezelfde kolom 
                i+n in [a[j]+j for j in range(n)] or # niet op dezelfde diagonaal 
                i-n in [a[j]-j for j in range(n)]) # niet op dezelfde diagonaal


def rsearch(N):
    global a
    for i in range(N): # cols (0, 1)
        if check(a,i):
            a.append(i)
            if len(a) == N:
                if a not in b:
                    b.append(a)
                    a = []
            else:
                if rsearch(N):
                    return True
            if len(a) > 0:
                del a[-1] # verwijder laatste element
    return False

a = [] # a geeft voor iedere rij de kolompositie aan
b = []
t = 0

rsearch(8)
print(a)
print(b)

def printQueens(a):
    n = len(a)
    for i in range(n):
        for j in range(n):
            if a[i] == j:
                print("x", end= " ")
            else:
                print("*", end= " ")
        print()
    print()
#===========================================================

from itertools import permutations
counter = 0
n = 8
cols = range(n)
for vec in permutations(cols):
    if n == len(set(vec[i]+i for i in cols)) \
         == len(set(vec[i]-i for i in cols)):
        print (vec )
        counter += 1

print(counter)
