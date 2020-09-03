#!/usr/bin/env python
import unittest
from collections import defaultdict

tots = defaultdict(lambda: 0.0)

class ProbabilityTester(unittest.TestCase):
	def test_probs(self):
		for key in tots.keys():
			self.assertEqual(round(tots[key], 7), 1.0)

def probability_test():
	lines = open('../dataset/probabilities', 'r')
	keys = [line.split() for line in lines.readlines()]
	for key in keys:
		tots[str([key[0] + ' ' + key[1]])] += float(key[3])

if __name__ == "__main__":
	probability_test()
	unittest.main()
