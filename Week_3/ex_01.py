# Studentnumber : 1716390
# Class : V2C

"""
Function to check whether the given position i is possible.
This should be a positions where the queen can't be attacked by others.

Parameters
----------
a : list (Didn't choose the name myself. Was given in the reader)
    The current board for the queensproblem solution

i : integer (Didn't choose the name myself. Was given in the reader)
    The column you want to place the new queen at.

Returns
-------
boolean
    Boolean containing True when the position is possible.
    If not possible the boolean contains False.
"""
def check(a,i):  # ga na of i aan a toegevoegd kan worden
    n = len(a)
    return not (i in a or # niet in dezelfde kolom 
                i+n in [a[j]+j for j in range(n)] or # niet op dezelfde diagonaal 
                i-n in [a[j]-j for j in range(n)]) # niet op dezelfde diagonaal

"""
Function to print the board containing the queens to the screen.

Parameters
----------
a : list (Didn't choose the name myself. Was given in the reader)
    The position of the queens on the board.

Returns
-------
None
"""
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

"""
Function to find all the solutions for a queensproblem with a given amount of queens.

Parameters
----------
N : list (Didn't choose the name myself. Was given in the reader)
    The amount of queens you want on your board 
    without being able to take each other. 

Returns
-------
boolean
    Boolean containing True when the solutions where found.
    If not found the boolean contains False.
"""
def rsearch(N):
    global a
    for i in range(N): # cols (0, 1)
        if check(a,i):
            a.append(i)
            if len(a) == N:
                if a not in solutions:
                    solutions.append(a)
                    a = []
                    rsearch(N)
                    return True
            else:
                if rsearch(N):
                    return True
            if len(a) > 0:
                del a[-1] # verwijder laatste element
    
    return False

a = [] # a geeft voor iedere rij de kolompositie aan
solutions = []

print(rsearch(8))
for solution in solutions:
    print(solution)
    printQueens(solution)
print(len(solutions))


#===========================================================
"""
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
"""

