from itertools import permutations


data = [x.split() for x in open('input.txt').readlines()]
print(len(data) - sum(1 for x in data if len(x) != len(set(x))))
print(len(data) - sum([any([True for y in permutations(x, 2)
                            if sorted(y[0]) == sorted(y[1])]) for x in data]))
