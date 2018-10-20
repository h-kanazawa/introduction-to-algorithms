# -*- coding: utf-8 -*-


class X:
    def __init__(self, v):
        self.v = v
        self.next = None
        self.set = None

    def find_set(self):
        if self.set is None:
            raise Exception('This element does not belong to any Set')
        return self.set.head

    def __str__(self):
        s = self.set.head.v if self.set is not None else 'None'
        return '(v:{}, set:{})'.format(self.v, s)


class Set:
    def __init__(self, x):
        """make_set"""
        x.set = self
        self.head = x
        self.tail = x
        self.w = 1

    def to_list(self):
        a = []
        o = self.head
        while o is not None:
            a.append(o)
            o = o.next
        return a

    def __str__(self):
        a = [o.__str__() for o in self.to_list()]
        return '{' + ', '.join(a) + '} w: ' + str(self.w)

    def to_v_list(self):
        return [o.v for o in self.to_list()]


def union(x, y):
    y_set = y.set
    x.set.tail.next = y.set.head
    x.set.tail = y.set.tail
    x.set.w = x.set.w + y.set.w
    o = y.set.head
    while o.next is not None:
        o.set = x.set
        o = o.next
    o.set = x.set
    return x.set, y_set


def weighted_union(x, y):
    if x.set.w < y.set.w:
        return union(y, x)
    else:
        return union(x, y)


if __name__ == '__main__':
    pass
