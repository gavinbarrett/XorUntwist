#!/usr/bin/env python
from math import ceil

def test_train_split(lines, ratio, size):
	threshold = ceil(ratio*size)
	return lines[:threshold], lines[threshold:]

def mix_sentences(lines, size, blksz=20):
	print('Chunking blocks..')
	blocks = [lines[i:i+blksz] for i in range(0, size, blksz)]
	print('Zipping blocks..')
	return list(zip(*blocks))

def xor_streams(plaintext, keystreams):
	by = [x^y for x,y in zip(''.join(plaintext), ''.join(keystreams))]
	#return print(by)

def print_out(plain_train, plain_test, keystream, ciphertext):
	with open('dat.plain.train') as train, open('dat.plain.test') as test, open('dat.key', 'w') as k, open('dat.cipher', 'w') as c:
		train.write(plain_train)
		test.write(plain_test)
		k.write(keystream)
		c.write(ciphertext)


with open('./dat.tag', 'r') as fi:
	
	# select level to split
	split_level = 6
	print('Reading lines..')
	lines = fi.readlines()
	print('Gathering size..')
	size = len(lines)
	
	# FIXME: change function to add randomness to the function
	mixed = mix_sentences(lines, size)

	# seperate key from plaintext
	plaintext = mixed[:size//2]
	keystream =  mixed[size//2:]
	# FIXME: fix encryption function
	# create cipher file
	cipher = xor_streams(plaintext, keystream)

	#train_set, test_set = test_train_split(lines, 0.8, size)
