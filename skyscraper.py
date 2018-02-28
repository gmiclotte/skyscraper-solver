#!/usr/bin/python3.6
import itertools
from operator import mul
from functools import reduce
import sys

def satisfies_r(row, r):
	return satisfies_l(list(reversed(row)), r)

def satisfies_l(row, l):
	if len(set(row)) < len(list(row)):
		return False
	if l == 0:
		return True
	seen = 0
	curr_max = 0
	for entry in row:
		if entry > curr_max:
			curr_max = entry
			seen += 1
	return l == seen

def possible_rows(s, l, r):
	p = []
	for row in itertools.permutations(range(1, s + 1)):
		if satisfies_l(row, l) and satisfies_r(row, r):
			p.append(row)
	return p

def solve(s, l, r, t, b):
	rows = []
	for i in range(s):
		rows.append(possible_rows(s, l[i], r[i]))
	sol_count = 0
	total = reduce(mul, [len(row) for row in rows], 1)
	for solution in itertools.product(*rows):
		sol_count += 1
		print(sol_count, total)
		count = 0
		for i in range(s):
			c = [row[i] for row in solution]
			if not (satisfies_l(c, t[i]) and satisfies_r(c, b[i])):
				break
			count += 1
		if count == s:
			return solution
	return ["no solution found"]

def main(argv):
	s = int(argv[1])
	l = r = t = b = []
	for arg in argv[2:]:
		if arg[0] == 'c':
			temp = [int(i) for i in arg[1:]]
			t = temp[0:s]
			r = temp[s:2*s]
			b = list(reversed(temp[2*s:3*s]))
			l = list(reversed(temp[3*s:]))
		if arg[0] == 'l':
			l = [int(i) for i in arg[1:]]
		if arg[0] == 'r':
			r = [int(i) for i in arg[1:]]
		if arg[0] == 't':
			t = [int(i) for i in arg[1:]]
		if arg[0] == 'b':
			b = [int(i) for i in arg[1:]]
	print(l,r,t,b)
	for row in solve(s, l, r, t, b):
		print(row)


if __name__ == '__main__':
	main(sys.argv)
