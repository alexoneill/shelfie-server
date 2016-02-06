# hackAmazon.py
# We don't want to register, so let's hack a BS4 API!!

from bs4 import BeautifulSoup
import urllib
# url = 'http://www.amazon.com/s/ref=nb_sb_noss_1?url=search-alias%3Dstripbooks&field-keywords=asimov'
# r = urllib.urlopen(url).read()
# soup = BeautifulSoup(r)

# for e in soup.find_all(class_="a-link-normal s-access-detail-page  a-text-normal"):
# 	print e["title"]

# def amazonResults(isbn):
# 	# isbn = '9780545670319'
# 	url = 'http://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Dstripbooks&field-keywords='+str(isbn)+'&rh=n%3A283155%2Ck%3A'+str(isbn)
# 	r = urllib.urlopen(url).read()
# 	soup = BeautifulSoup(r)
# 	return soup

def recommendations(isbn):
	# isbn = '9780545670319'
	reco = []
	url = 'http://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Dstripbooks&field-keywords='+str(isbn)+'&rh=n%3A283155%2Ck%3A'+str(isbn)
	r = urllib.urlopen(url).read()
	soup = BeautifulSoup(r, "html.parser")
	res = soup.find(class_="a-size-medium a-color-null s-inline s-access-title a-text-normal")
	if res == None:
		return [[isbn,None,None],None]
	# print '*****',res
	itemTitle = res.contents
	link = res.parent["href"]

	r = urllib.urlopen(link).read()
	soup = BeautifulSoup(r, "html.parser")
	for res in soup.find_all(class_="a-carousel-card a-float-left"):
		rfa = res.find_all('a')
		title_raw = rfa[0].find_all('div')[-1].contents[0]
		title = ' '.join(''.join(title_raw.split('\n')).split())
		author = rfa[1].contents[0]
		# rating = rfa[2].contents[1].span.contents[0]
		reclink = 'www.amazon.com%s'%rfa[0]['href']
		reco += [[title,author,reclink]]
	return [[isbn,itemTitle,link],reco]

# (b,r) = recommendations('9781451666328')
# print b
# print ''
# for e in r:
# 	print e
# 	print ''
