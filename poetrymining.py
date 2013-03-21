#!/usr/bin/python

# A script to retrieve poetry text and separate it by technological development.

import urllib2
from bs4 import BeautifulSoup

# Create the files for our words.

photography = open('photography.txt', 'w')
cinema = open('cinema.txt', 'w')
television = open('television.txt', 'w')
internet = open('internet.txt', 'w')

# Open list of tech words
# Is the list is finalized?
tech_words = open('text_words.txt', 'rU')

# Unary search
# Iterate through each of the query words

for word in tech_words:
	url = 'http://www.poetryfoundation.org/search/poems#qs=' + word
	search = urllib2.urlopen(url).read()

	soup = BeautifulSoup(search)

	# Getting dynamically created elements is slightly problematic
	# Going to try Selenium WebDriver for this--have used it in PHP

	# Code below is not correct. Only for conceptual purposes
	results = soup.find(id='search-results')
	poems = results.find_all('href')

	for link.get_text() in poems:

		# Open the link of the poem
		l = 'http://www.poetryfoundation.org/' + link
		poem = urllib2.urlopen(l).read()

		# Grab the poem text and the pub date

		# Based on the pub date, output the poem's text to one of the files

		# Lather, rinse, repeat



