from datetime import datetime
from requests import get
import os

start_time = datetime.now()
print 'Started at ' + str(start_time)

num_files_found = 0
num_files_downloaded = 0

with open('data_urls.txt', 'rU') as in_file:

	for link in in_file.readlines():

		path = link.split('/',)

		file_name = path[len(path) - 1]

		if os.path.isfile('data/' + file_name):

			print '   found file: {}...'.format(file_name)

			num_files_found += 1

		else:

			print '   downloading: {} ({})...'.format(file_name, datetime.now() - start_time)

			response = get(link, stream=True)

			with open('data/' + file_name, 'wb') as f:
				for chunk in response.iter_content(chunk_size=1024):
					if chunk: # filter out keep-alive new chunks
						f.write(chunk)
						f.flush()

			num_files_downloaded += 1

# maybe how long it took to print statement
print "Finished. Found {0} files, downloaded {1} (see data/ directory).".format(num_files_found, num_files_downloaded)