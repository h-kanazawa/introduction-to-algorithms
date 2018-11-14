# -*- coding: utf-8 -*-


def recursive_euclid(a: int, b: int) -> int:
    if b == 0:
        return a
    return recursive_euclid(b, a % b)


def euclid(a: int, b: int) -> int:
    """greatest common devisor

    """
    while b > 0:
        a, b = b, a % b
    return a


def recursive_extended_euclid(a: int, b: int) -> (int, int, int):
    if b == 0:
        return (a, 1, 0)
    _d, _x, _y = recursive_extended_euclid(b, a % b)
    d, x, y = _d, _y, (_x - (a // b) * _y)
    return d, x, y


if __name__ == '__main__':
    print('x')
