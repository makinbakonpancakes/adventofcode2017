#!/usr/bin/python
def main(incrementor):
    data = open('input.txt').read().strip()
    total = 0
    for i in range(len(data)):
        num = int(data[i])
        next_index = int(incrementor(i, len(data))) % len(data)
        if num == int(data[next_index]):
            total += num
    print(total)


main(lambda x, y: x + 1)
main(lambda x, y: x + y / 2)
