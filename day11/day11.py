data = open('input.txt').read().strip().split(',')
location = [0, 0]
furthest = 0
distance = 0
for step in data:
    if step == 'n':
        location[1] += 1
    elif step == 's':
        location[1] -= 1
    elif step == 'ne':
        location[0] += 1
    elif step == 'sw':
        location[0] -= 1
    elif step == 'nw':
        location[0] -= 1
        location[1] += 1
    elif step == 'se':
        location[0] += 1
        location[1] -= 1
    distance = max([abs(location[0]), abs(location[1]),
                    abs(location[0] + location[1])])
    if distance >= furthest:
        furthest = distance
print(distance)
print(furthest)
