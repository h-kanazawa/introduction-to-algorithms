# -*- coding: utf-8 -*-

from functools import reduce

from src.euclid import recursive_extended_euclid


def chinese_remainder_theorem_pair(b1, b2, m1, m2) -> int:
    """Chinese remainder theorem
    """
    d, x, y = recursive_extended_euclid(m1, m2)
    if d != 1:
        raise Exception('m1 and m2 is not relatively prime')
    ans = b1 + m1 * x * (b2 - b1)
    if ans < 0:
        ans += m1 * m2
    return ans


def chinese_remainder_theorem(n, a) -> int:
    """Chinese remainder theorem
    ref: https://rosettacode.org/wiki/Chinese_remainder_theorem#Python
    """
    sum = 0
    prod = reduce(lambda k1, k2: k1 * k2, n)

    for n_i, a_i in zip(n, a):
        p = prod / n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod


def mul_inv(a, b):
    if b == 1:
        raise Exception('All n must not be 1')

    b0 = b
    _y, _x = 0, 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        _y, _x = _x - q * _y, _y

    if _x < 0:
        _x += b0
    return _x


if __name__ == '__main__':
    print('x')
