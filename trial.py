from SmoothTrigram import SmoothTrigram
from JointTrigram import JointTrigramProb
from string import ascii_uppercase, ascii_lowercase
from collections import defaultdict

def initial_probs(sents):
	alphabet = ascii_lowercase + ascii_uppercase
	# create a dictionary for character frequencies
	freqs = defaultdict(lambda: 0.0)
	# strip out the first character of each sentence
	init_chars = list(zip(*sents))[0]
	# compute the frequency of each character as the initial character
	for c in alphabet:
		freqs[c] = init_chars.count(c)/len(init_chars)
	return freqs

s1 = "This model is going to take over my life"
s2 = "Fish tacos make a great snack"
s3 = "This is my favorite tune"
s4 = "Machine learning is pretty cool"
s5 = "Cannot wait to eat some breakfast later"
s6 = "Today is going to be a good day"
s7 = "Go Biden"

#sents1 = [s1.split(),s2.split(),s3.split(),s4.split(),s5.split(),s6.split()]
#sents2 = [s1.split(),s2.split(),s3.split(),s4.split(),s5.split(),s7.split()]

sents1 = [list(s1),list(s2),list(s3),list(s4),list(s5),list(s6)]
sents2 = [list(s1),list(s2),list(s3),list(s4),list(s5),list(s7)]
# create two language models
st1 = SmoothTrigram(sents1)
st2 = SmoothTrigram(sents2)

# take the joint probability
#st1.joint_prob(st2)
#print(dict(st.model['over', 'my']))
#st1.joint_prob(st2)

print(initial_probs(sents1))
