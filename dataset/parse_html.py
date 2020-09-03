#!/usr/bin/env python3
from os import listdir, path, remove
from bs4 import BeautifulSoup

# target blog directory
files = listdir('./blogs/')
# target the data file
data = './dat.tag'
# set a limit for data files extracted
limit = 1000

# remove data file if it exists
if (path.exists(data) and path.isfile(data)):
	remove(data)

of = open(data, 'w+')

# iterate through blog files
for idx, _file in enumerate(files):
	
	print(f'Reading file: {idx+1}...')
	with open(f'./blogs/{_file}', 'rb')as fi:
		
		# read the file data
		blogdata = fi.read()
		# parse the html
		soup = BeautifulSoup(blogdata, 'html.parser')
		# find all post tags
		posts = soup.findAll('post')
		# extract the text content from each post
		texts = [post.get_text().lstrip().rstrip() for post in posts]
		# split the posts into seperate sentences
		split_texts = [text.split('  ') for text in texts]
		# filter out empty strings and newlines
		filtered = list(filter(lambda x: x != '' and x != '\n', split_texts))
		# iterate through all sentences
		for sentences in filtered:
			for j, sentence in enumerate(sentences):
				# write the tagged sentence out to the dat file
				of.write(f'<s>{sentence}</s>\n')
	#if idx == limit:
	#	break
of.close()
