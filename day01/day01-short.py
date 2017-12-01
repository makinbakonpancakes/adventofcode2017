#!/usr/bin/python
def inverse_captcha(data, n):
    print(sum(int(a) for a, b in zip(data, data[n:] + data[:n]) if a == b))


data = open('input.txt').read().strip()
inverse_captcha(data, 1)
inverse_captcha(data, len(data) // 2)
