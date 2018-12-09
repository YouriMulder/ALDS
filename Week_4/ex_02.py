#Als je 64-bits python gebruikt moet je twee verschillende gebroken getallen x en y zoeken
#waarbij geldt: hash(x) % (2**32) == hash(y) % (2**32) . (Anders is teveel rekentijd nodig. Zie
# http://preshing.com/20110504/hash-collision-probabilities/

import random


looping = True
hashed = dict()
listOfDoubles = list()
try: 
	while True:
		randomFloat = random.random()
		
		randomFloatHash = hash(randomFloat) % (2**32)

		if randomFloatHash in hashed.keys():
			print("Collision found")
			listOfDoubles.append([
				[hashed[randomFloatHash], randomFloat]
				,[randomFloatHash, hash(hashed[randomFloatHash]) % (2**32)]
			]) 	
		else:
			hashed[randomFloatHash] = randomFloat
except KeyboardInterrupt:
	for pair in listOfDoubles:
		hashes = pair[0]
		values = pair[1]
		print(hashes, values)

