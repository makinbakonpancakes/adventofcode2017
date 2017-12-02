#!/usr/bin/python
from itertools import permutations


rows = [[int(y) for y in x.split()] for x in open('input.txt').readlines()]
print(sum(max(row) - min(row) for row in rows))
print(sum(a//b for row in rows for a, b in permutations(row, 2) if a % b == 0))
