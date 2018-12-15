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

def is_connected(G,s):
	V = vertices(G)
	s.predecessor = None
	s.distance = 0
	for v in V:
		if v != s:
			v.distance = INFINITY  # v krijgt het attribuut 'distance'
	
	q = myqueue()
	q.enqueue(s) 
	
	found = set()

	while q:
		u = q.dequeue() 
		found.add(u)
		for v in G[u]:
			if v.distance == INFINITY: # v is nog niet bezocht
				v.distance = u.distance + 1
				v.predecessor = u  # v krijgt het attribuut 'predecessor'
				q.enqueue(v)
				
	return len(found) == len(G)


v = [Vertex(i) for i in range(8)]
GNotConnected = {
	v[0]:[v[4],v[5]],
	v[1]:[v[4],v[5],v[6]],
	v[2]:[v[4],v[5],v[6]],
	v[3]:[v[7]],
	v[4]:[v[0],v[1],v[2]],
	v[5]:[v[0],v[1],v[2]],
	v[6]:[v[1],v[2]],
	v[7]:[v[3]]
}
print("GNotConnected graph =", is_connected(GNotConnected,v[0]))

v = [Vertex(i) for i in range(6)]
GConnected = {
	v[0]:[v[3],v[4]],
	v[1]:[v[3],v[4],v[5]],
	v[2]:[v[3],v[4],v[5]],
	v[3]:[v[0],v[1],v[2]],
	v[4]:[v[0],v[1],v[2]],
	v[5]:[v[1],v[2]],
}
print("GConnected =", is_connected(GConnected,v[0]))