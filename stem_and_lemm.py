#!/usr/bin/python
# -*- coding: utf-8 -*-

import nltk, re
from nltk.stem.wordnet import WordNetLemmatizer

# Lemmatizing and stemming, just to see what happens.

f1 = open('nltk/1970_before_nltk.txt', 'rU')
f2 = open('nltk/lemmstem_1970_before.txt', 'w')

lemm = WordNetLemmatizer()
stemmer = nltk.PorterStemmer()

words = []

for word in f1:
	word = word.strip()

	word = lemm.lemmatize(word)
	word = stemmer.stem(word)
	f2.write(word + "\n")