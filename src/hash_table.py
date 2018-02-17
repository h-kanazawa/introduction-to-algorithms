# -*- coding: utf-8 -*-

from typing import Tuple, List
from copy import deepcopy


class X:
    def __init__(self, k, v):
        self.key = k
        self.value = v


class DirectAddressTable:
    """direct-address table implemented with array, not dict
    key should be in range(m)
    """
    def __init__(self, m: int):
        self.T = [None for i in range(m)]
        self.m = m

    def search(self, k: int):
        """worst-case time O(1)
        """
        return self.T[k]

    def insert(self, x: X):
        """worst-case time O(1)
        """
        self.T[x.key] = x

    def delete(self, x: X):
        """worst-case time O(1)
        """
        self.T[x.key] = None


class HashTable:
    """hash table implemented with array, not dict.
    Each chain of a HashTable is Array, but Linked List is used in the textbook.
    """
    def __init__(self, m: int, hash):
        self.T = [[] for i in range(m)]
        self.m = m
        self.hash = hash

    def search(self, key):
        """
        average time if self.m is O(n)
        average time when key exists in the table: Θ(1 + m/n)
        average time when key does not exist in the table: Θ(1 + m/n)
        """
        filtered = list(filter(lambda z: z.key == key, self.T[self.hash(key)]))
        if len(filtered) < 1:
            return None
        return filtered[0]

    def insert(self, x: X):
        """worst-case time: O(1)
        it assumes that the element x.key is not already present in the table
        """
        self.T[self.hash(x.key)].append(x)

    def delete(self, x: X):
        """
        """
        original = deepcopy(self.T[self.hash(x.key)])
        self.T[self.hash(x.key)] = list(filter(lambda z: z.key != x.key, original))

    def __str__(self):
        return '\n'.join(
            [', '.join(
                ['(k: {}, v: {})'.format(kv.key, kv.value) for kv in kvs]
            ) for kvs in self.T]
        )


def gen_division_hash(m: int):
    def h(k: int):
        return k % m
    return h


def gen_multiplication_hash(m: int):
    # 0 < A < 1
    # A should be "s / 2^ω" (0 < s < 2^ω)
    # Knuth suggests the (5^0.5 - 2) / 2 is reasonable.
    A = 2654435769.0 / (2 ^ 32)

    def h(k: int):
        return int((k * A % 1) * m)
    return h


if __name__ == '__main__':
    print('x')
