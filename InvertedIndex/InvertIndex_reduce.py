#!/usr/bin/python

import re
import sys

def main():
	output = {}
	for line in sys.stdin:
		(filename, key) = line.strip().split('\t')
		if key not in output:
			output[key] = []
			output[key].append(filename)
		elif filename not in output[key]:
			output[key].append(filename)

	for key, count in output.items():
		count = ' '.join(count)
		count = '(' + count + ')'
		print "\t".join([key, count])

main()
