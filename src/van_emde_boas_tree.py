# -*- coding: utf-8 -*-

from math import floor, fmod


def high(u):
    def f(x):
        return int(floor(x / floor(u ** 0.5)))
    return f


def low(u):
    def f(x):
        return int(fmod(x, floor(u ** 0.5)))
    return f


def index(u):
    def f(x, y):
        return int(x * floor(u ** 0.5) + y)
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

    def __str__(self):
        self.get_as_list()

    def get_as_list(self):
        a = []
        curr = self.min
        while curr is not None:
            a.append(curr)
            curr = self.successor(curr)
        return a

    def member(self, x):
        if x == self.min or x == self.max:
            return True
        elif self.u == 2:
            return False
        else:
            return self.cluster[self.high(x)].member(self.low(x))

    def successor(self, x):
        """O(loglog(u))
        """
        if self.u == 2:
            if x == 0 and self.max == 1:
                return 1
            else:
                return None
        elif self.min is not None and x < self.min:
            return self.min
        else:
            # max value of cluster having x
            max_low = self.cluster[self.high(x)].max
            if max_low is not None and self.low(x) < max_low:
                offset = self.cluster[self.high(x)].successor(self.low(x))
                return self.index(self.high(x), offset)
            else:
                succ_cluster = self.summary.successor(self.high(x))
                if succ_cluster is None:
                    return None
                else:
                    print(succ_cluster)
                    offset = self.cluster[succ_cluster].min
                    return self.index(succ_cluster, offset)

    def predecessor(self, x):
        """O(loglog(u))
        """
        if self.u == 2:
            if x == 1 and self.min == 0:
                return 0
            else:
                return None
        elif self.max is not None and x > self.max:
            return self.max
        else:
            min_low = self.cluster[self.high(x)].min
            if min_low is not None and self.low(x) > min_low:
                offset = self.cluster[self.high(x)].predecessor(self.low(x))
                return self.index(self.high(x), offset)
            else:
                pred_cluster = self.summary.predecessor(self.high(x))
                if pred_cluster is None:
                    if self.min is not None and x > self.min:
                        return self.min
                    else:
                        return None
                else:
                    offset = self.cluster[pred_cluster].max
                    return self.index(pred_cluster, offset)

    def insert_to_empty(self, x):
        self.min = x
        self.max = x

    def insert(self, x):
        if self.min is None:
            self.insert_to_empty(x)
        else:
            if x < self.min:
                tmp = self.min
                self.min = x
                x = tmp

            if self.u > 2:
                if self.cluster[self.high(x)].min is None:
                    self.summary.insert(self.high(x))
                    self.cluster[self.high(x)].insert_to_empty(self.low(x))
                else:
                    self.cluster[self.high(x)].insert(self.low(x))

            if x > self.max:
                self.max = x

    def delete(self, x):
        if self.min == self.max:
            self.min = None
            self.max = None
        elif self.u == 2:
            if x == 0:
                self.min = 1
            else:
                self.min = 0
            self.max = self.min
        else:
            if x == self.min:
                first_cluster = self.summary.min
                x = self.index(first_cluster, self.cluster[first_cluster].min)
                self.min = x
            self.cluster[self.high(x)].delete(self.low(x))

            if self.cluster[self.high(x)].min is None:
                self.summary.delete(self.high(x))

                if x == self.max:
                    summary_max = self.summary.max
                    if summary_max is None:
                        self.max = self.min
                    else:
                        self.max = self.index(summary_max, self.cluster[summary_max].max)
            elif x == self.max:
                self.max = self.index(self.high(x), self.cluster[self.high(x)].max)


if __name__ == '__main__':
    print('x')
