# -*- coding: utf-8 -*-


class KV:
    """Key Value
    simulator of address: value
    """
    def __init__(self, k, v):
        self.k = k
        self.v = v


class X:
    """B Tree Node
    """

    def __init__(self, n, keys, children, is_leaf):
        """
        Arguments:
            n {int} -- the number of keys
            keys {KV[]} -- key (key-value) list
            children {X[]} -- child node list
            is_leaf {bool} -- whether this node is leaf
        """
        self.n = n
        self.keys = keys
        self.c = children
        self.is_leaf = is_leaf

    def stringify(self):
        return 'n:{}, keys:{}, c:{}, is_leaf:{}'.format(
            self.n,
            [kv.v for kv in self.keys],
            [[kv.v for kv in c.keys] for c in self.c],
            self.is_leaf
        )

    def __str__(self):
        return self.stringify()


class BTree:
    """Chapter 18: B Tree
    """
    def __init__(self, t):
        """
        Arguments:
            t {int} -- the minimum number of children an internal (non-root) node can have.
        """
        self.t = t
        self.count_disk_read = 0
        self.count_disk_write = 0
        x = X(0, [], [], True)
        self.disk_write(x)
        self.root = x

    def disk_read(self, x):
        self.count_disk_read += 1

    def disk_write(self, x):
        self.count_disk_write += 1

    def search(self, k):
        self.count_disk_read = 0
        self.count_disk_write = 0
        return self._search(self.root, k)

    def _search(self, x, k):
        """
        CPU time O(t * log{t}(n))
        disk access O(log{t}(n))

        Arguments:
            x {X} -- node
            k {int} -- key

        Returns:
            {KV | None}
        """
        i = 1
        while i <= x.n and k > x.keys[i - 1].k:
            i = i + 1
        if i <= x.n and k == x.keys[i - 1].k:
            return x.keys[i - 1]
        elif x.is_leaf:
            return None
        else:
            self.disk_read(x.c[i - 1])
            return self._search(x.c[i - 1], k)

    def split_child(self, x, i):
        """
        CPU time Θ(t)
        disk access O(1)
        """
        z = X(0, [], [], True)
        y = x.c[i]
        z.is_leaf = y.is_leaf
        z.n = self.t - 1

        # Move keys from y to z
        for j in range(1, self.t):
            z.keys.append(y.keys[j + self.t - 1])
        for j in range(1, self.t):
            y.keys.pop()

        y.n = self.t - 1

        # Copy children from y to z
        if not y.is_leaf:
            for j in range(0, self.t):
                z.c.append(y.c[j + self.t])
            for j in range(0, self.t):
                y.c.pop()

        # Slide x children to make space for z
        x.c.append(x.c[-1])
        for j in range(x.n, i, -1):
            x.c[j] = x.c[j - 1]

        # Add z to x children
        x.c[i + 1] = z

        # Slide x keys to make space for new key from y
        if len(x.keys) > 0:
            x.keys.append(x.keys[-1])
        for j in range(x.n - 1, i - 1, -1):
            x.keys[j] = x.keys[j - 1]
        x.n = x.n + 1

        # Move split key from y to x
        if len(x.keys) > 0:
            x.keys[i] = y.keys[self.t - 1]
        else:
            x.keys.append(y.keys[self.t - 1])
        y.keys.pop(self.t - 1)

        self.disk_write(x)
        self.disk_write(y)
        self.disk_write(z)

    def insert(self, kv):
        """insert
        Arguments:
            kv {KV}
        """
        self.count_disk_read = 0
        self.count_disk_write = 0

        r = self.root
        if r.n == 2 * self.t - 1:
            s = X(0, [], [r], False)
            self.root = s
            self.split_child(s, 0)
            self.insert_nonfull(s, kv)
        else:
            self.insert_nonfull(r, kv)

    def insert_nonfull(self, x, kv):
        """insert nonfull
        Arguments:
            x {X}
            kv {KV}
        """
        i = x.n
        if x.is_leaf:
            x.keys.append(x.keys[-1])
            while i >= 1 and kv.k < x.keys[i - 1].k:
                x.keys[i - 1] = x.keys[i - 2]
                i = i - 1
            x.keys[i] = kv
            x.n = x.n + 1
            self.disk_write(x)
        else:
            while i >= 1 and kv.k < x.keys[i - 1].k:
                i = i - 1
            i = i + 1
            self.disk_read(x.c[i - 1])

            if x.c[i - 1].n == 2 * self.t - 1:
                self.split_child(x, i - 1)
                if kv.k > x.keys[i - 1].k:
                    i = i + 1

            self.insert_nonfull(x.c[i - 1], kv)


if __name__ == '__main__':
    print('x')
