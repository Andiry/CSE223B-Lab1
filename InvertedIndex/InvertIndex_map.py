#!/usr/bin/python

import re
import sys
import os

def get_filename():
	filename = os.environ['map_input_file']
	parts = filename.split('/')
	length = len(parts)
	filename = parts[length - 1]
	return filename

def process_word(word):
	word = word.lower()
	length = len(word)
	p = re.compile('[a-z0-9\'-]')
	word1 = []
	for i in range(0, length):
		if p.match(word[i]):
			word1.append(word[i])
	return ''.join(word1)

def main():
	for line in sys.stdin:
		words = line.strip().split()
		for word in words:
			filename = get_filename()
			word = process_word(word)
			if word:
				print '%s\t%s' % (filename, word)

main()
 
