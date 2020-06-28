from math import log
from nltk import trigrams
from nltk.corpus import reuters
from collections import defaultdict

class SmoothTrigram:
	# Kat's backoff trigram with Laplace smoothing
	def __init__(self, sentences):
		self.model = defaultdict(lambda: defaultdict(lambda: 0))
		self.joint_model = defaultdict(lambda: defaultdict(lambda: 0))
		# train the model on the inputs
		self.train(sentences)

		# self.score()

	def train(self, sentences):
		# for each sentence
		for sentence in sentences:#reuters.sents():
			# split the sentence into trigrams
			for w1,w2,w3 in trigrams(sentence, pad_right=True, pad_left=True):
				# increment trigram occurrence
				self.model[(w1,w2)][w3] += 1
	
	def joint_prob(self, model2, sentences, sentences2):
		# loop through training data 
		# get probability of every event
		# - models may contain different entries
		# add entry into joint model and set prob to model1_prob * model2_prob
		# we should take both models and add them together, then turn into a set to remove any
		# duplicates. Then we can loop through all of these trigrams and multiply their probs

		#for pr1, pr2 in zip(sentences, sentences):
		#	self.joint_model[] = min()
		pass

	def see_keys(self):
		for i in self.model:
			print(i, end='  ')
			for j in i:
				print(self.model[i][j])

	def score(self):
		# for each n gram
		for gram in self.model:
			# total the number of occurrences
			tots = float(sum(self.model[gram].values()))
			# for each tri
			for w3 in self.model[gram]:
				# compute the probabilities
				if self.model[gram][w3] == 0:
					# return smoothed value
					self.model[gram][w3] = 1/tots
				else:
					# return real statistical value
					self.model[gram][w3] /= tots
	
	def score_joint(self):
		# for each n gram
		for gram in self.joint_model:
			# total the number of occurrences
			tots = float(sum(self.joint_model[gram].values()))
			# for each tri
			for w3 in self.joint_model[gram]:
				# compute the probabilities
				if self.joint_model[gram][w3] == 0:
					# return smoothed value
					self.joint_model[gram][w3] = 1/tots
				else:
					# return real statistical value
					self.joint_model[gram][w3] /= tots
