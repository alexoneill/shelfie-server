import pprint
# import sys
from apiclient.discovery import build
import httplib2
import hackAmazon as ha

import sys
import json

api_key = 'AIzaSyBhtLjbQ5F3XoqEElobXVsNhpPf3nkR3WU'
try:
	service = build('books', 'v1', developerKey=api_key)
except Exception, e:
	# print 'Could not connect, exiting...'
	print e
	exit()

# request = service.volumes().list(source='public', q='asimov', maxResults=3)
# response = request.execute()
# pprint.pprint(response)

#Returns list of top n<=3 queries for title/author info
#[Title,Author,ISBN10,ISBN13,rating]
#Later: incorporate bonus data (e.g.book dimensions) for lolz
#	bvi['pageCount']
def topNQueries(q,N=1):
	if N<1:
		n = 1
	if N>5:
		n = 5
	result = []
	request = service.volumes().list(source='public', q=q, maxResults=3)
	response = request.execute()
	# print 'Found %d books:' % len(response['items'])
	for book in response.get('items', []):
		bvi = book['volumeInfo']
		# print bvi['industryIdentifiers']
		rating = None
		buyLink = None
		bvi = book['volumeInfo']
		if 'averageRating' in bvi:
			rating = '%.1f'%bvi['averageRating']
		
	  	ISBN10,ISBN13 = None,None
	  	if 'industryIdentifiers' in bvi:
		  	for e in bvi['industryIdentifiers']:
		  		if '10' in e['type']:
		  			ISBN10 = e['identifier']
		  		if '13' in e['type']:
		  			ISBN13 = e['identifier']
	  	
	  	title = bvi['title']
	  	author = None
	  	if 'authors' in bvi:
	  		author = bvi['authors'][0] #main author
	  	result += [[title,author,ISBN10,ISBN13,rating]]
  	return result

def suggest(q):
	ml = []
	for result in topNQueries(q):
		# print result
		# print '='*50
		# print result
		# print 'If you like \"%s\" by %s, you should read:'%(result[0],result[1])
		reco = ha.recommendations(result[3])
		if reco[1] == None:
			continue

		l = list()
		for bk in reco[1]:
			d = dict([('book', bk[0]), ('author', bk[1]), ('link', bk[2])])
			l += [d]

		ml += [l]

	print json.dumps(ml)

for item in sys.argv[1:]:
  suggest(item)
