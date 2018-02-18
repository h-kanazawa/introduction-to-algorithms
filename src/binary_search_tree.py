# -*- coding: utf-8 -*-


class X:
    def __init__(self, key, value, left, right, parent):
        self.k = key
        self.v = value
        self.l = left
        self.r = right
        self.p = parent

    def stringify(self):
        return 'k:{}, v:{}, l:{}, r:{}, has_p:{}'.format(
            self.k, self.v, self.l, self.r, self.p is not None)

    def __str__(self):
        return self.stringify()


class BinarySearchTree:

    def __init__(self):
        self.root = None

    def __eq__(self, other):
        return type(self) == type(other) and self.k == other.k

    def inorder_tree_walk(self, x):
        if x is None:
            return
        self.inorder_tree_walk(x.l)
        print(x)
        self.inorder_tree_walk(x.r)

    def search(self, x, key):
        if x is None or x.k == key:
            return x
        if key < x.k:
            return self.search(x.l, key)
        if x.k < key:
            return self.search(x.r, key)

    def iterative_tree_search(self, x, key):
        while x is not None and key != x.k:
            if key < x.k:
                x = x.l
            else:
                x = x.r
        return x

    def minimum(self, x):
        if x is None:
            return None
        while x.l is not None:
            x = x.l
        return x

    def successor(self, x):
        if x is None:
            return None
        if x.r is not None:
            return self.minimum(x.r)

        y = x.p
        while y is not None and x == y.r:
            x = y
            y = y.p
        return y


if __name__ == '__main__':
    root = X(1, '10', None, None, None)
    bst = BinarySearchTree()
    bst.root = root
    bst.inorder_tree_walk(root)
    print('---')
    print(bst.search(root, 1))
    print(bst.search(root, 2))
    print(bst.iterative_tree_search(root, 1))
    print(bst.iterative_tree_search(root, 2))
    print(bst.minimum(root))
