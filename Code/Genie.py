import mechanize
import cookielib
import html2text
from BeautifulSoup import BeautifulSoup


def browse(username, password):
	
	# Browser
	br = mechanize.Browser()

	# Cookie Jar
	cj = cookielib.LWPCookieJar()
	br.set_cookiejar(cj)

	# Browser options



	#User-Agent
	br.addheaders = [('User-agent', 'Chrome')]

	br.open('http://steamcommunity.com/id/' + username + '/wishlist')

	br.select_form()
