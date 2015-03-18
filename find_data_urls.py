from datetime import datetime, timedelta
from sys import argv
from urlparse import urlparse
from requests import get
from bs4 import BeautifulSoup

start_time = datetime.now()
print 'Started at ' + str(start_time)

try:
	url = argv[1]
except IndexError:
	url = raw_input("Enter url:")

domain = urlparse(url).scheme + "://" +urlparse(url).netloc

response = get(url)

soup = BeautifulSoup(response.content)

url_count = 0

with open('data_urls.txt', 'a') as in_file:

	for link in soup.find_all('a'):

		if link['href'][-4:] == '.csv':

			if domain in link['href']:

				in_file.write(link['href'] + '\n')

			else: 

				in_file.write(domain + link['href'] + '\n')

			url_count += 1

# maybe how long it took to print statement
print "Found {0} data urls (see data_urls.txt)".format(url_count)