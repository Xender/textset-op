#!/usr/bin/env python3

import sys

def build_line_sets(filenames):
	line_sets = []

	for filename in filenames:
		with open(filename) as f:
			current_lineset = set()
			line_sets.append( current_lineset )

			for line in f:
				current_lineset.add(line)

	return line_sets

def update_set_with_op(operation, target_set, *sets):
	if operation == '*':
		raise NotImplementedError(
		"Cartesian product not implemented.\n"
		"If you wanted intersection, use one of:\n"
		" `intersect', `and', `&'")
	try:
		op = {
			'|':         target_set.update,
			'+':         target_set.update,
			'or':        target_set.update,
			'union':     target_set.update,

			'&':         target_set.intersection_update,
			'and':       target_set.intersection_update,
			'intersect': target_set.intersection_update,

			'-':         target_set.difference_update,
			'diff':      target_set.difference_update,

			'^':         target_set.symmetric_difference_update,
			'xor':       target_set.symmetric_difference_update,
			'sym_diff':  target_set.symmetric_difference_update,
		}[operation]
	except KeyError:
		raise ValueError("Uknown or invalid operation: %r", (operation,))

	op(*sets)

def main(args):
	op, *filenames = args

	line_sets = build_line_sets(filenames)
	update_set_with_op(op, *line_sets)

	for line in line_sets[0]:
		sys.stdout.write(line)

if __name__ == "__main__":
	main(sys.argv[1:])
