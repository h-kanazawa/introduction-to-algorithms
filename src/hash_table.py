# -*- coding: utf-8 -*-

from typing import Tuple, List
from copy import deepcopy


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


def gen_lenear_probing(m: int, f):
    """
    f: auxiliary hash function
    """
    def h(k: int, i: int):
        return (f(k) + i) % m
    return h


def gen_quadratic_probing(m: int, f, c1, c2):
    """
    f: auxiliary hash function
    if m is 2^n, c1 = c2 = 1/2 is good
    """
    def h(k: int, i: int):
        return (f(k) + c1 * i + c2 * i * i) % m
    return h


class X:
    def __init__(self, k, v):
        self.key = k
        self.value = v

    def stringify(self):
        return '(k: {}, v: {})'.format(self.key, self.value)

    def __str__(self):
        return self.stringify()

    def __eq__(self, other):
        return type(self) == type(other) and self.key == other.key and self.value == other.value


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


class ClosedAddressingHashTable:
    """cloased addressing hash table implemented with array, not dict.
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

    def delete(self, key):
        """
        """
        original = deepcopy(self.T[self.hash(key)])
        self.T[self.hash(key)] = list(filter(lambda z: z.key != key, original))

    def __str__(self):
        return '\n'.join(
            [', '.join([kv.stringify() for kv in kvs]) for kvs in self.T]
        )


class OpenAddressingHashTable:
    """open addressing hash table implemented with array, not dict.

    hash: (key, int) => int
    hash should return an int in range(0, m)
    """
    DELETED = 'DELETED'

    def __init__(self, m: int, hash):
        self.T = [None for i in range(m)]
        self.m = m
        self.hash = hash

    def insert(self, x: X):
        for i in range(0, self.m):
            j = self.hash(x.key, i)
            if self.T[j] is None or self.T[j] == OpenAddressingHashTable.DELETED:
                self.T[j] = x
                break
        else:
            raise Exception('overflow')

    def search(self, key):
        for i in range(0, self.m):
            j = self.hash(key, i)
            if self.T[j] is None:
                break
            if self.T[j] == OpenAddressingHashTable.DELETED:
                continue
            if self.T[j].key == key:
                return self.T[j]
        return None

    def delete(self, key):
        for i in range(0, self.m):
            j = self.hash(key, i)
            if self.T[j] is None:
                break
            if self.T[j] == OpenAddressingHashTable.DELETED:
                continue
            if self.T[j].key == key:
                self.T[j] = OpenAddressingHashTable.DELETED
                break

    def stringify(self):
        st = []
        for kv in self.T:
            if kv is None:
                st.append('')
            elif kv == OpenAddressingHashTable.DELETED:
                st.append('DELETED')
            else:
                st.append(kv.stringify())
        return '\n'.join(st)

    def __str__(self):
        return self.stringify()


if __name__ == '__main__':
    None
