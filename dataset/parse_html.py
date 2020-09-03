from os import listdir
from bs4 import BeautifulSoup

files = listdir('./blogs/')
i = 0
for fi in files:
	
	fi = open(f'./blogs/{fi}', 'rb')
	
	blogdata = fi.read()

	soup = BeautifulSoup(blogdata, 'html.parser')

	fi.close()

	ls = soup.findAll('post')
	less = [l.get_text().lstrip().rstrip() for l in ls]
	print(less)
	i += 1
	if (i == 5):
		break
