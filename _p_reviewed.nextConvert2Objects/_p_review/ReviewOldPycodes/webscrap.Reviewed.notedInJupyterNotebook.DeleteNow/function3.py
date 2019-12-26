#web scraping function
#function3.py

from webscrapfunc import *

#url = 'http://example.webscraping.com/view-%d'%page

def id_iter_crawl(url):
	import itertools
	max_errors = 5
	num_errors = 0
	for page in itertools.count(1):
		html = download(url)
		if html is None:
			#received an error 
			num_errors+=1
			if num_errors == max_error:
				break
		else:
			#success - can scrape the result
			#...
			num_errors = 0
