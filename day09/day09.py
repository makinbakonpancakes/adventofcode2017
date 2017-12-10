data = open('input.txt').read().strip()
i = 0
garbage = False
in_groups = 0
score = 0
garbage_count = 0
while i < len(data):
    char = data[i]
    if char == '!':
        i += 1
    elif garbage and char != '>':
        garbage_count += 1
    elif char == '<':
        garbage = True
    elif char == '>':
        garbage = False
    elif char == '{' and not garbage:
        in_groups += 1
    elif char == '}' and not garbage:
        score += in_groups
        in_groups -= 1
    i += 1
print(score)
print(garbage_count)
