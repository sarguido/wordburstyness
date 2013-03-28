#!/usr/bin/python

# A script to retrieve poetry text and separate it by technological development.

import time, re
from bs4 import BeautifulSoup
from selenium import webdriver

# Create the files for our words.

photography = open('photography.txt', 'w')
cinema = open('cinema.txt', 'w')
television = open('television.txt', 'w')
internet = open('internet.txt', 'w')

# Open list of tech words
# Is the list is finalized?
tech_words = open('text_words.txt', 'rU')

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

		# At this point, we can write to the file based on
		# either the subject of the poem or by the year. If we're
		# writng based on year, then what are the cutoff dates?

		break

	break


