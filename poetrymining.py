#!/usr/bin/python

# A script to retrieve poetry text and separate it by technological development.

import time, re
from bs4 import BeautifulSoup
from selenium import webdriver

# Create the files for our words.

f1 = open('1900.txt', 'w')
f2 = open('1910.txt', 'w')
f3 = open('1920.txt', 'w')
f4 = open('1930.txt', 'w')
f5 = open('1940.txt', 'w')
f6 = open('1950.txt', 'w')
f7 = open('1960.txt', 'w')
f8 = open('1970.txt', 'w')
f9 = open('1980.txt', 'w')
f10 = open('1990.txt', 'w')
f11 = open('2000.txt', 'w')
f12 = open('2010.txt', 'w')

# Open list of tech words
# Is the list is finalized?
tech_words = open('text_words.txt', 'rU')

# tech_words = ['cinema', 'theater']
# Initialize Selenium for dynamic scraping purposes
driver = webdriver.Firefox()

# Unary search
# Iterate through each of the query words

for word in tech_words:
	url = 'http://www.poetryfoundation.org/search/poems#qs=' + word
	driver.get(url)
	time.sleep(3)

	html = driver.page_source
	soup = BeautifulSoup(html)
	results = soup.find('div', id='search-results')
	links = results.find_all('a', 'title')

	for l in links:
		link = l.get('href')
		poem_url = 'http://www.poetryfoundation.org' + link
		driver.get(poem_url)
		
		poem_html = driver.page_source
		soup = BeautifulSoup(poem_html)
		poem = soup.find('div', 'poem')
		poem_text = poem.find_all('div')

		word_list = []

		for line in poem_text:
			line = line.get_text()
			line = line.split(' ')
			for li in line:
				word_list.append(li)
		
		credits = soup.find('div', 'credit')
		date = re.search(r'([0-9]{4})', str(credits))
		pub_year = date.group(0)

		# separated by decade
		if pub_year >= '1900' or pub_year <= '1909':
			for word in word_list:
				f1.write('word' + "\n")
		elif pub_year >= '1910' or pub_year <= '1919':
			for word in word_list:
				f2.write('word' + "\n")
		elif pub_year >= '1920' or pub_year <= '1929':
			for word in word_list:
				f3.write('word' + "\n")
		elif pub_year >= '1930' or pub_year <= '1939':
			for word in word_list:
				f4.write('word' + "\n")
		elif pub_year >= '1940' or pub_year <= '1949':
			for word in word_list:
				f5.write('word' + "\n")
		elif pub_year >= '1950' or pub_year <= '1959':
			for word in word_list:
				f6.write('word' + "\n")
		elif pub_year >= '1960' or pub_year <= '1969':
			for word in word_list:
				f7.write('word' + "\n")
		elif pub_year >= '1970' or pub_year <= '1979':
			for word in word_list:
				f8.write('word' + "\n")
		elif pub_year >= '1980' or pub_year <= '1989':
			for word in word_list:
				f9.write('word' + "\n")
		elif pub_year >= '1990' or pub_year <= '1999':
			for word in word_list:
				f10.write('word' + "\n")
		elif pub_year >= '2000' or pub_year <= '2009':
			for word in word_list:
				f11.write('word' + "\n")
		elif pub_year >= '2010' or pub_year <= '2019':
			for word in word_list:
				f12.write('word' + "\n")
		else:
			continue


