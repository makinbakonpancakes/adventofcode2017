step_size = int(open('input.txt').read().strip())
hurricane = [0]
position = 0
for x in range(2017):
    position = (position + step_size) % len(hurricane) + 1
    hurricane.insert(position, len(hurricane))
print(hurricane[position + 1])

# 0 is always the last item in the list so only keep track when the
# first item changes.
position = 0
for x in range(1, 50000001):
    position = (position + step_size) % x + 1
    if position == 1:
        answer = x
print(answer)
