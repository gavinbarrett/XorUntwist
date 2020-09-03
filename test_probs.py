
# Test emission probabilities
with open('emit.hmm', 'r') as fi:
	data = fi.readlines()
	lines = [x.split(' ') for x in data]
	probs = 0.0
	sts = set().union([x[1] for x in lines])
	
	for s in sts:
		prob = 0.0
		for l in lines:
			if l[1] == s:
				prob += float(l[3])
		print(f'P(E{s}: {prob})')

with open('trans.hmm', 'r') as fi:
	data = fi.readlines()
	lines = [x.split(' ') for x in data]
	probs = 0.0
	sts = set().union([x[1] for x in lines])
	
	for s in sts:
		prob = 0.0
		for l in lines:
			if l[1] == s:
				prob += float(l[3])
		print(f'P(T{s}: {prob})')


