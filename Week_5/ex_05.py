#5a
def isEulerGraph(G):
	for node in G:
		if not len(G[node]) % 2 == 0:
			return False
	return True

#5b
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


def getBridges(G):
	bridges = []
	for u in vertices(G):
		G[u] = sorted(G[u])
		for v in G[u]:
			
			G[u].remove(v)
			
			clear(G) 
			BFS(G, u)
			
			if v.distance is INFINITY:
				if (u,v) not in bridges:
					bridges.append((u, v))
				
			G[u].append(v)
			G[u] = sorted(G[u])

	return bridges

def addToCircuitIfValid(G, node, neighbour, circuit, bridges):
	if (node, neighbour) not in bridges or neighbour == G[node][-1]:
		print(node, neighbour, G[node][-1])
		circuit.append(neighbour)
		return True
	return False

def getEulerCircuit(G, s):
	circuit = list()

	added = False
	currentNode = s
	circuit.append(currentNode)
	
	allEdges = edges(G)
	while allEdges:
		bridges = getBridges(G)
		for neighbour in G[currentNode]:
			print(currentNode, G[currentNode])
			if addToCircuitIfValid(G, currentNode, neighbour, circuit, bridges):
				G[currentNode].remove(neighbour)
				G[neighbour].remove(currentNode)
				added = True
				break

		if not added:
			return added

		currentNode = circuit[-1]
		allEdges = edges(G)
		#print(circuit)
	
	return circuit
		


# 5a
v = [Vertex(i) for i in range(8)]

G = {	v[0]: [v[1], v[2]],
		v[1]: [v[0], v[3]],
		v[2]: [v[0], v[3]],
		v[3]: [v[1], v[2], v[4], v[6]],
		v[4]: [v[3], v[5], v[6], v[7]],
		v[5]: [v[4], v[6]],
		v[6]: [v[3], v[4], v[5], v[7]],
		v[7]: [v[6], v[4]]
}
print("is Euler graph ", isEulerGraph(G))

G = {	v[0]: [v[1], v[2]],
		v[1]: [v[0], v[3],v[4]],
		v[2]: [v[0], v[3]],
		v[3]: [v[1], v[2], v[4], v[6]],
		v[4]: [v[3], v[5], v[6], v[7]],
		v[5]: [v[4], v[6]],
		v[6]: [v[3], v[4], v[5], v[7]],
		v[7]: [v[6], v[4]]
}
print("is not Euler graph ", isEulerGraph(G))

#5b
G = {	v[0]: [v[1], v[2]],
		v[1]: [v[0], v[3]],
		v[2]: [v[0], v[3]],
		v[3]: [v[1], v[2], v[4], v[6]],
		v[4]: [v[3], v[5], v[6], v[7]],
		v[5]: [v[4], v[6]],
		v[6]: [v[3], v[4], v[5], v[7]],
		v[7]: [v[6], v[4]]
}
print("is Euler graph ", getEulerCircuit(G, v[0]))


