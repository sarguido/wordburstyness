#!/usr/bin/python

# A script to retrieve poetry text and separate it by decade.

import time, re
from bs4 import BeautifulSoup
from selenium import webdriver

# Create the files for our words.
# Using the 'before' list here.

f1 = open('1900_before.txt', 'w')
f2 = open('1910_before.txt', 'w')
f3 = open('1920_before.txt', 'w')
f4 = open('1930_before.txt', 'w')
f5 = open('1940_before.txt', 'w')
f6 = open('1950_before.txt', 'w')
f7 = open('1960_before.txt', 'w')
f8 = open('1970_before.txt', 'w')
f9 = open('1980_before.txt', 'w')
f10 = open('1990_before.txt', 'w')
f11 = open('2000_before.txt', 'w')
f12 = open('2010_before.txt', 'w')

# Open list of tech words
tech_words = open('before.txt', 'rU')

# tech_words = ['website', 'cinema', 'theater']
# Initialize Selenium for dynamic scraping purposes
driver = webdriver.Firefox()

# Unary search
# Iterate through each of the query words

for word in tech_words:
	url = 'http://www.poetryfoundation.org/search/poems#qs=' + word
	driver.get(url)
	time.sleep(3)

	x = ''
	while x != 'done':
		html = driver.page_source
		soup = BeautifulSoup(html)

		if soup.find('a', 'next'):

			html = driver.page_source
			soup = BeautifulSoup(html)
			next = soup.find('a', 'next')
			print next
	
			results = soup.find('div', id='search-results')
			links = results.find_all('a', 'title')

			for l in links:
				link = l.get('href')
				poem_url = 'http://www.poetryfoundation.org' + link
				driver.get(poem_url)
				
				poem_html = driver.page_source
				soup = BeautifulSoup(poem_html)

				word_list = []

				name = soup.find(id = 'poem-top')
				title = name.find('h1').get_text()
				word_list.append(title)

				poem = soup.find('div', 'poem')
				poem_text = poem.find_all('div')

				for line in poem_text:
					line = line.get_text()
					line = line.split(' ')
					for li in line:
						word_list.append(li)

				if soup.find('div', 'credit'):
					credits = soup.find('div', 'credit')
					if re.search(r'([0-9]{4})', str(credits)):
						date = re.search(r'([0-9]{4})', str(credits))
						pub_year = int(date.group(0))

						# separated by decade
						if pub_year >= 1900 and pub_year <= 1909:
							for word in word_list:
								word = word.encode('utf-8')
								f1.write(word + "\n")
						elif pub_year >= 1910 and pub_year <= 1919:
							for word in word_list:
								word = word.encode('utf-8')
								f2.write(word + "\n")
						elif pub_year >= 1920 and pub_year <= 1929:
							for word in word_list:
								word = word.encode('utf-8')
								f3.write(word + "\n")
						elif pub_year >= 1930 and pub_year <= 1939:
							for word in word_list:
								word = word.encode('utf-8')
								f4.write(word + "\n")
						elif pub_year >= 1940 and pub_year <= 1949:
							for word in word_list:
								word = word.encode('utf-8')
								f5.write(word + "\n")
						elif pub_year >= 1950 and pub_year <= 1959:
							for word in word_list:
								word = word.encode('utf-8')
								f6.write(word + "\n")
						elif pub_year >= 1960 and pub_year <= 1969:
							for word in word_list:
								word = word.encode('utf-8')
								f7.write(word + "\n")
						elif pub_year >= 1970 and pub_year <= 1979:
							for word in word_list:
								word = word.encode('utf-8')
								f8.write(word + "\n")
						elif pub_year >= 1980 and pub_year <= 1989:
							for word in word_list:
								word = word.encode('utf-8')
								f9.write(word + "\n")
						elif pub_year >= 1990 and pub_year <= 1999:
							for word in word_list:
								word = word.encode('utf-8')
								f10.write(word + "\n")
						elif pub_year >= 2000 and pub_year <= 2009:
							for word in word_list:
								word = word.encode('utf-8')
								f11.write(word + "\n")
						elif pub_year >= 2010 and pub_year <= 2019:
							for word in word_list:
								word = word.encode('utf-8')
								f12.write(word + "\n")
						else:
							continue
					else:
						continue
				else:
					continue

			page = next.get('href')
			form = page.replace('?', '&')
			next_url = url + form

			driver.get(next_url)
			time.sleep(3)
		else:
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
				
				if soup.find('div', 'credit'):
					credits = soup.find('div', 'credit')
					if re.search(r'([0-9]{4})', str(credits)):
						date = re.search(r'([0-9]{4})', str(credits))
						pub_year = date.group(0)

						# separated by decade
						if pub_year >= 1900 and pub_year <= 1909:
							for word in word_list:
								word = word.encode('utf-8')
								f1.write(word + "\n")
						elif pub_year >= 1910 and pub_year <= 1919:
							for word in word_list:
								word = word.encode('utf-8')
								f2.write(word + "\n")
						elif pub_year >= 1920 and pub_year <= 1929:
							for word in word_list:
								word = word.encode('utf-8')
								f3.write(word + "\n")
						elif pub_year >= 1930 and pub_year <= 1939:
							for word in word_list:
								word = word.encode('utf-8')
								f4.write(word + "\n")
						elif pub_year >= 1940 and pub_year <= 1949:
							for word in word_list:
								word = word.encode('utf-8')
								f5.write(word + "\n")
						elif pub_year >= 1950 and pub_year <= 1959:
							for word in word_list:
								word = word.encode('utf-8')
								f6.write(word + "\n")
						elif pub_year >= 1960 and pub_year <= 1969:
							for word in word_list:
								word = word.encode('utf-8')
								f7.write(word + "\n")
						elif pub_year >= 1970 and pub_year <= 1979:
							for word in word_list:
								word = word.encode('utf-8')
								f8.write(word + "\n")
						elif pub_year >= 1980 and pub_year <= 1989:
							for word in word_list:
								word = word.encode('utf-8')
								f9.write(word + "\n")
						elif pub_year >= 1990 and pub_year <= 1999:
							for word in word_list:
								word = word.encode('utf-8')
								f10.write(word + "\n")
						elif pub_year >= 2000 and pub_year <= 2009:
							for word in word_list:
								word = word.encode('utf-8')
								f11.write(word + "\n")
						elif pub_year >= 2010 and pub_year <= 2019:
							for word in word_list:
								word = word.encode('utf-8')
								f12.write(word + "\n")
						else:
							continue
					else:
						continue
				else: 
					continue

			x = 'done'

