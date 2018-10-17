# -*- coding: utf-8 -*-

from math import floor, fmod


def high(u):
    def f(x):
        return floor(x / floor(u ** 0.5))
    return f


def low(u):
    def f(x):
        return fmod(x, floor(u ** 0.5))
    return f


def index(u):
    def f(x, y):
        return x * floor(u ** 0.5) + y
    return f


class VanEmdeBoas:

    def __init__(self, u):
        """van Emde Boas Tree

        Arguments:
            u {int} -- 2 ^ k (k is an integer)
        """
        self.u = u
        self.min = None
        self.max = None

        self.high = high(u)
        self.low = low(u)
        self.index = index(u)

        if u == 2:
            self.summary = None
            self.cluster = None
            return

        # ⊥√u
        fu = floor(u ** 0.5)
        self.summary = VanEmdeBoas(fu)
        self.cluster = [VanEmdeBoas(fu) for i in range(0, fu)]

    def member(self, x):
        if x == self.min or x == self.max:
            return True
        elif self.u == 2:
            return False
        else:
            return self.cluster[self.high(x)].member(self.low(x))


if __name__ == '__main__':
    print('x')
