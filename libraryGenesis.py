"""This code takes as input the name of any book,
searches it in library genesis,
fetches you the first 'n' download links.

this code can be customised to search for a specific author, series, publisher, year, ISBN, language and more.
for this, change the 'link' variable and make suitable changes in the following code.
"""

# library genesis: https://libgen.rs/index.php (to find soft copy of any book)

import requests # to open a link
from bs4 import BeautifulSoup # to get the html code of the link

query = input('Enter book name: ') or 'harry potter' # name of the book you want to search
link = f'https://libgen.rs/search.php?req={query}&open=0&res=25&view=simple&phrase=1&column=title' # query to be sent to the web
num = 10 # first 'n' results
names = [] # names of the books found are stored here
mirrors = [] # download links of the books are stored here

reqs = requests.get(link) # open the link
soup = BeautifulSoup(reqs.text, 'html.parser') # get the source code

for mirror in soup.find_all('a'): # finds every <a> tag
	temp = mirror.get('href') # gets the ' href = "" ' attribute of the <a> tag
	if 'library.lol' in temp: # other links are available too, i just choose this one. i.e, the link will be something like this: 'https://library.lol/.....'
		mirrors.append(temp) # append the link to the list
		if len(mirrors) == num: # exit the loop on reaching the limit
			break

for link in mirrors: # for each link in the mirrors list
	reqs = requests.get(link) # open it in the web
	soup = BeautifulSoup(reqs.text, 'html.parser') # and get its source code
	for temp in soup.find_all('h1'): # find the <h1> tag as the name of the book is stored here
		names.append(temp.text) # append the name to names
		break # just in case there are more than 1 <h1> tag

download_link = dict(zip(names, mirrors)) # zip names to their links

# displaying the obtained data
print()
for book in download_link:
	print(f'book: {book}')
	print(f'link: {download_link[book]}')
	print()

# you can now open the link and click on the "GET" link at the top
# the file starts downloading automatically