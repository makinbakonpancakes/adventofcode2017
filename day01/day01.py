#!/usr/bin/python
def inverse_captcha(incrementor):
    data = open('input.txt').read().strip()
    total = 0
    for i in range(len(data)):
        num = int(data[i])
        next_index = int(incrementor(i, len(data))) % len(data)
        if num == int(data[next_index]):
            total += num
    print(total)


inverse_captcha(lambda x, y: x + 1)
inverse_captcha(lambda x, y: x + y / 2)
