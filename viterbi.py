#!/usr/bin/env python3
from re import match
from math import log
from sys import argv, exit
from binascii import unhexlify
from collections import defaultdict

OOV = 'OOV'
INIT = 'INIT'
FINAL = 'FINAL'

def build_emission(EMIT_HMM, B, states, vocab):
	# emit.hmm file fields
	# Emit state emit probability

	# build emission matrix
	with open(EMIT_HMM) as f:
		for line in f:
			# split emission data into four fields
			emit = line.split(' ')
			# get state character
			st = unhexlify(emit[1])
			# get emission byte
			em = unhexlify(emit[2])
			# get emission probability
			prob = float(emit[3])
			# save emission probability
			B[st][em] = log(prob)
			states[st] = 1
			vocab[em] = 1

def build_transition(TRANS_HMM, A, states):
	# trans.hmm file fields
	# Trans state1 state2 probability
	
	# build transition matrix
	with open(TRANS_HMM) as f:
		for line in f:
			tran = line.split()
			# get the first state
			st1 = unhexlify(tran[1])
			# get the second state
			st2 = unhexlify(tran[2])
			# get the probability
			prob = float(tran[3])
			# save transition probability
			A[st1][st2] = log(prob)
			states[st1] = 1
			states[st2] = 1

def backtrace(CIPH, states, vocab, A, B):
	'''
	print(states)
	print(vocab)
	print(A)
	print(B)
	'''
	k1 = ''
	tags = ''
	with open(CIPH) as f:
		for line in f:
			line = line.strip()
			line = line.split()
			size = len(line)
			line = [''] + line
			V = defaultdict(lambda: defaultdict(lambda: None))
			Backtrace = defaultdict(lambda: defaultdict(lambda: None))
			V[0][INIT] = 0.0
			for i in range(1, size+1):
				if vocab[line[i]] == 0.0:
					line[i] = OOV
				for k1 in (states.keys()):
					for k2 in (states.keys()):
						if (A[k2][k1] != 0.0 and B[k1][line[i]] != 0.0 and V[i-1][k2] != None):
							v = V[i-1][k2] + A[k2][k1] + B[k1][line[i]]
							if V[i][k1] == None or v > V[i][k1]:
								V[i][k1] = v
								Backtrace[i][k1] = k2
			foundgoal = 0
			for k2 in (states.keys()):
				if A[k2][FINAL] != 0.0 and V[size][k2] is not None:
					v = V[size][k2] + A[k2][FINAL]
					if not foundgoal or v > goal:
						goal = v
						foundgoal = 1
						k1 = k2
			if foundgoal:
				tags = []
				for j in range(size, 0, -1):
					tags = [k1] + tags
					k1 = Backtrace[j][k1]
		return tags

if len(argv) < 4:
	print('Usage: ./viterbi.py <trans.hmm> <emit.hmm> <data.cipher.test>')
	exit()

TRANS_HMM = argv[1]
EMIT_HMM = argv[2]
CIPH = argv[3]

vocab = defaultdict(lambda: 0)
total = 0
states = defaultdict(lambda: 0)

A = defaultdict(lambda: defaultdict(lambda: 0.0))
B = defaultdict(lambda: defaultdict(lambda: 0.0))

# build emission matrix
build_emission(EMIT_HMM, B, states, vocab)

# build transmission matrix
build_transition(TRANS_HMM, A, states)

# backtrace through the HMM to find the sequence
seq = backtrace(CIPH, states, vocab, A, B)

print(f'Sequence: {seq}')
