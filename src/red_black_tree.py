# -*- coding: utf-8 -*-

B = 'BLACK'
R = 'RED'
NIL = 'NIL'


class X:
    def __init__(self, key, color, left, right, parent):
        self.k = key
        self.c = color
        self.l = left
        self.r = right
        self.p = parent

    def stringify(self):
        return 'k:{}, c: {}, l:{}, r:{}, p:{}'.format(
            self.k, self.c, self.l and self.l.k, self.r and self.r.k, self.p and self.p.k)

    def __str__(self):
        return self.stringify()

    def __eq__(self, other):
        return type(self) == type(other) and self.stringify() == other.stringify()


class RedBlackTree:

    def __init__(self):
        self.nil = X(NIL, B, None, None, None)
        self.root = self.nil

    def left_rotate(self, x):
        """
        y            x
        ├───┐  right ├───┐
        x   c  --->  a   y
        ├─┐    <---      ├─┐
        a b    left      b c
        """
        y = x.r
        x.r = y.l
        if y.l != self.nil:
            y.l.p = x
        y.p = x.p
        if x.p == self.nil:
            self.root = y
        elif x == x.p.l:
            x.p.l = y
        else:
            x.p.r = y
        y.l = x
        x.p = y

    def right_rotate(self, y):
        x = y.l
        y.l = x.r
        if x.r != self.nil:
            x.r.p = y
        x.p = y.p
        if y.p == self.nil:
            self.root = x
        elif y == y.p.r:
            y.p.r = x
        else:
            y.p.l = x
        x.r = y
        y.p = x

    def insert(self, z):
        y = self.nil
        x = self.root
        while x != self.nil:
            y = x
            if z.k == x.k:
                raise Exception('the key of z has existed in the tree')
            elif z.k < x.k:
                x = x.l
            else:
                x = x.r
        # At this point, x is T.nil, and y is the future parent of z
        z.p = y
        if y == self.nil:
            self.root = z
        elif z.key < y.key:
            y.l = z
        else:
            y.r = z
        z.l = self.nil
        z.r = self.nil
        z.c = R
        self.insert_fixup(z)

    def insert_fixup(self, z):
        while z.p.c == R:
            if z.p == z.p.p.l:
                y = z.p.p.r
                if y.c == R:
                    z.p.c = B
                    y.c = B
                    z.p.p.c = R
                    z = z.p.p
                else:
                    if z == z.p.r:
                        z = z.p
                        self.left_rotate(z)
                    z.p.c = B
                    z.p.p.c = R
                    self.right_rotate(z.p.p)
            else:
                # z.p == z.p.p.r
                y = z.p.p.l
                if y.c == R:
                    z.p.c = B
                    y.c = B
                    z.p.p.c = R
                    z = z.p.p
                else:
                    if z == z.p.l:
                        z = z.p
                        self.right_rotate(z)
                    z.p.c = B
                    z.p.p.c = R
                    self.left_rotate(z.p.p)
        self.root.c = B


if __name__ == '__main__':
    print('x')
