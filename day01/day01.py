#!/usr/bin/python
def inverse_captcha(n):
    data = open('input.txt').read().strip()
    total = 0
    for i in range(len(data)):
        num = int(data[i])
        next_index = (i + n) % len(data)
        if num == int(data[next_index]):
            total += num
    print(total)


inverse_captcha(1)
inverse_captcha(len(data) // 2)
