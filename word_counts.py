#!/usr/bin/python

# To run ex: python word_counts.py 1970_after.txt > word_counts_1970.txt

from mrjob.job import MRJob
import re

word = re.compile(r"\b[\w']+\b")

class PoetryWordCount(MRJob):

	def mapper(self, _, line):
		for word in word.findall(line):
			yield word.lower(), 1

	def combiner(self, word, counts):
		yield word, sum(counts)

	def reducer(self, word, counts):
		yield word, sum(counts)


if __name__ == '__main__':
	PoetryWordCount.run()