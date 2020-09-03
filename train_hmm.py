#!/usr/bin/env python3

from sys import argv
from nltk import trigrams
from binascii import hexlify
from collections import defaultdict

vocab = {}
CHAR_FILE = argv[1]
CIPH_FILE = argv[2]

OOV = 'OOV'
INIT = 'INIT'
FINAL = 'FINAL'

emissions = {}
transitions = {}
emissionsTotal = defaultdict(int)
transitionsTotal = defaultdict(int)

with open(CHAR_FILE) as charFile, open(CIPH_FILE) as ciphFile:
	charString = charFile.read()
	ciphed = ciphFile.read()

	cs = []
	for ciph in ciphed:
		c = ciph.split('\n')[0]
		cs.append(c)
	ciphed = ''.join(cs)

	# iterate through all pairs of trigrams
	for (w1,w2,w3), (w4,w5,w6) in zip(trigrams(charString), trigrams(ciphed)):
		print(w1, w2, w3)
		print(w4, w5, w6)

		tags = [w1, w2, w3]
		tokens = [w4, w5, w6]
		
		pairs = zip(tags, tokens)

		prevtag = INIT
		
		for tag, token in pairs:
			if token not in vocab:
				vocab[token] = 1
				token = OOV
			if tag not in emissions:
				emissions[tag] = defaultdict(int)
			if prevtag not in transitions:
				transitions[prevtag] = defaultdict(int)

			emissions[tag][token] += 1
			emissionsTotal[tag] += 1

			transitions[prevtag][token] += 1
			transitionsTotal[prevtag] += 1
			
			prevtag = tag

		if prevtag not in transitions:
			transitions[prevtag] = defaultdict(int)

		transitions[prevtag][FINAL] += 1
		transitionsTotal[prevtag] += 1

f = open('trans.hmm', 'w')

for prevtag in transitions:
	for tag in transitions[prevtag]:
		f.write("Trans %s %s %s\n" % (hexlify(prevtag.encode()).decode(), hexlify(tag.encode()).decode(), float(transitions[prevtag][tag]) / transitionsTotal[prevtag]))

f.close()

f = open('emit.hmm', 'w')

for tag in emissions:
	for token in emissions[tag]:
		print(f'Tag: {tag}\nToken: {token.encode()}')
		f.write("Emit %s %s %s\n" % (hexlify(tag.encode()).decode(), hexlify(token.encode()).decode(), float(emissions[tag][token]) / emissionsTotal[tag]))

f.close()
