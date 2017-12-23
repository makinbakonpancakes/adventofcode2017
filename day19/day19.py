data = open('input.txt').readlines()
location = complex(data[0].index('|'), 0)
direction = -1j
path = ""


def left():
    global direction
    direction *= 1j


def right():
    global direction
    direction *= -1j


def road(location):
    return data[int(location.imag) * -1][int(location.real)]


steps = 0
while road(location) != ' ':
    steps += 1
    location += direction
    if road(location) == '+':
        left_path = road(location + direction * 1j)
        left() if left_path != ' ' else right()
    if road(location).isalpha():
        path += road(location)
        location += direction
        steps += 1
print(path)
print(steps)
