#!/usr/bin/env python3

import sys

def main(args):
	minuend_filename, subtrahend_filename = args

	with open(subtrahend_filename) as sub_f:
		lines_to_remove = set(iter(sub_f))

	with open(minuend_filename) as min_f:
		sys.stdout.writelines(
			line
				for line in min_f
				if line not in lines_to_remove
		)

if __name__ == "__main__":
	main(sys.argv[1:])
