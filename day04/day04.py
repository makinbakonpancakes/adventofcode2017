from itertools import permutations


data = [line.split() for line in open('input.txt').readlines()]
print(len(data) - sum(True for phrase in data if len(phrase) != len(set(phrase))))
print(len(data) - sum([any([True for pair in permutations(phrase, 2)
                            if sorted(pair[0]) == sorted(pair[1])]) for phrase in data]))
