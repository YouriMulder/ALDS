class myqueue(list):
	def __init__(self,a=[]):
		list.__init__(self,a)

	def dequeue(self):
		return self.pop(0)

	def enqueue(self,x):
		self.append(x)
		
class Vertex:
	def __init__(self, data):
		self.data = data
	
	def __repr__(self):         # voor afdrukken
		return str(self.data)
	
	def __lt__(self, other):    # voor sorteren
		return self.data < other.data

import math
INFINITY = math.inf # float("inf")

def vertices(G):
	return sorted(G)

def edges(G):
	return [(u,v) for u in vertices(G) for v in G[u]]

def BFS(G,s):
	V = vertices(G)
	s.predecessor = None
	s.distance = 0
	for v in V:
		if v != s:
			v.distance = INFINITY  # v krijgt het attribuut 'distance'
	q = myqueue()
	q.enqueue(s) 
	while q:
		u = q.dequeue() 
		for v in G[u]:
			if v.distance == INFINITY: # v is nog niet bezocht
				v.distance = u.distance + 1
				v.predecessor = u  # v krijgt het attribuut 'predecessor'
				q.enqueue(v)

def clear(G): 
    for v in vertices(G):
        k = [e for e in vars(v) if e != 'data']
        for e in k:
            delattr(v,e)


def path_BFS(G,u,v):
	BFS(G,u)
	a = []
	if hasattr(v,'predecessor'):
		current = v
		while current:
			a.append(current)
			current = current.predecessor
		a.reverse()
	return a	

def reverseGraph(G):
	for vertex in edges(G):
		G[vertex[0]].remove(vertex[1])
		G[vertex[1]].append(vertex[0])

def isStronglyConnected(G, isReversed = False):
	V = vertices(G)
	s = V[0]
	
	BFS(G,s)
	for node in G:
		if node.distance is INFINITY:
			return False
	
	if not isReversed:
		reverseGraph(G)
		return True and isStronglyConnected(G, True)
	else:
		return True


v = [Vertex(i) for i in range(3)]
G = {   
	v[0]: [v[1]],
	v[1]: [v[2]],
	v[2]: [v[0]]
}
print("Strong connected: ", isStronglyConnected(G))

G = {
	v[0]: [v[2]],
	v[1]: [v[0]],
	v[2]: [v[1]]
}
print("Strong connected reversed: ", isStronglyConnected(G))

G = {
	v[0]: [v[1]],
	v[1]: [],
	v[2]: [v[0],v[1]]
}
print("Not strong connected: ", isStronglyConnected(G))

v = [Vertex(i) for i in range(5)]
G = {
	v[0]: [v[1]],
	v[1]: [v[2]],
	v[2]: [v[3], v[4]],
	v[3]: [v[0]],
	v[4]: [v[2]],
}
print("Custom strong connected: ", isStronglyConnected(G))

v = [Vertex(i) for i in range(7)]
G = {
	v[0]: [v[2]],
	v[1]: [v[0]],
	v[2]: [v[1],v[3]],
	v[3]: [v[2]],
	v[4]: [v[3],v[5]],
	v[5]: [v[4],v[6]],
	v[6]: []
}
print("Custom not strong connected: ", isStronglyConnected(G))




