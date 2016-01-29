from bs4 import BeautifulSoup
import urllib2
import sys
#grabs the website url
url = sys.argv[1]
# print temp
def findPDF(temp):
	y = []
	request = urllib2.Request(temp)
	# print request
	# request.add_header('User-agent', 'Mozilla 5.10')
	try:
		response = urllib2.urlopen(request)
	except urllib2.URLError, e: #HTTPError, e:
		print e.reason
	except ValueError:
		return y
	
	x = []
	s = BeautifulSoup(response.read())
	response.close()
	for links in s.find_all('a'):
		x.append(links.get('href'))
	
	#while loop runs through the list of links
	#grabs any of type pdf
	i = 0
	while i < len(x):
		t = x[i]
		# print t
		if t == "/":
			break
		a = len(t)
		b = a - 5
		a = a - 4 
		try:
			req = urllib2.Request(t)
			r = urllib2.urlopen(req)
			if r.geturl() == url:
				i = i + 1
				t = x[i]
				# print t
				req = urllib2.Request(t)
				r = urllib2.urlopen(req)
		except urllib2.URLError, e: 
			print e.reason
		except urllib2.HTTPError, e:
			print e.reason
		except ValueError:
			pass
		# if "http:" in t:
		if "/" in t:
			if t == url:
				return y
			if t == temp:
				return y
			# if r.getcode() > 200:
				# print r.getcode()
				# print t
			if "pdf" in r.geturl():
				# r = urllib2.urlopen(t)
				# print r.getcode()
				c = t + '   Size: ', len(r.read())
				y.append(c)
			elif "pdf" in t:
				# r = urllib2.urlopen(t)
				# print r.getcode()
				c = t + '   Size: ', len(r.read())
				y.append(c)
			elif t[b:] == ".html":
				pass
			else :
				# print t
				y = y + findPDF(t)
		else:
			break
		i = i + 1
	return y

z = findPDF(url)
for d in z:
	print d
		
