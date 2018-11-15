# -*- coding: utf-8 -*-


def to_binary(n):
    return [int(s) for s in list(bin(n).replace('0b', ''))]


def modular_exponentiation(a, b, n):
    """
    (a ^ b) mod n
    page 795
    """
    c = 0
    d = 1

    bs = to_binary(b)
    size = len(bs)
    for i in range(0, size):
        c = 2 * c
        d = (d * d) % n
        if bs[i] == 1:
            c = c + 1
            d = (d * a) % n
        print('{} {} {} {}'.format(i, bs[i], c, d))
    return d


if __name__ == '__main__':
    print('x')
