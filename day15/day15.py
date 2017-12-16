with open('input.txt', 'r') as f:
    a_start = f.readline().split(' ')[-1]
    b_start = f.readline().split(' ')[-1]


def a_generator(m=1):
    num = int(a_start)
    while True:
        num = num * 16807 % 2147483647
        if num % m == 0:
            yield num


def b_generator(m=1):
    num = int(b_start)
    while True:
        num = num * 48271 % 2147483647
        if num % m == 0:
            yield num


a = a_generator()
b = b_generator()
matches = 0
for _ in range(40000000):
    a_val = next(a)
    b_val = next(b)
    if a_val & 0xFFFF == b_val & 0xFFFF:
        matches += 1
print(matches)

a = a_generator(4)
b = b_generator(8)
matches = 0
for _ in range(5000000):
    a_val = next(a)
    b_val = next(b)
    if a_val & 0xFFFF == b_val & 0xFFFF:
        matches += 1
print(matches)
