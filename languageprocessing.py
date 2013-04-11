#!/usr/bin/python
# -*- coding: utf-8 -*-

import nltk, re
from nltk.corpus import stopwords
from mrjob.job import MRJob

# Removing stopwords, stemming, etc for a better word analysis

f = open('2010_before.txt', 'rU')
f1 = open('2010_before_nltk.txt', 'w')

unfiltered_list = []
filtered_list = []

for word in f:
	if len(word.split()):
		words = word.split()
		for w in words:
			w = w.strip("\xc2\xa0")
			w = w.strip("\t,.!?“\n:;\"”’-$()— ")
			w = w.lower()
			if re.search(r"\t*", w):
				tabs = re.compile(r"\t*")
				w = re.sub(tabs, '', w)
			if w == '' or w == ' ':
				continue
			else:
				unfiltered_list.append(w)
	else:
		word = word.strip("\xc2\xa0")
		word = word.strip("\t,.!?“\n:;\"”’-$()— ")
		word = word.lower()
		if re.search(r"\t*", word):
			tabs = re.compile(r"\t*")
			word = re.sub(tabs, '', word)
		if word == '' or word == ' ':
			continue
		else:
			unfiltered_list.append(word)

for un in unfiltered_list:
	if un in stopwords.words('english'):
		continue
	else:
		filtered_list.append(un)

for fil in filtered_list:
	f1.write(fil + "\n")

