# -*- coding: utf-8 -*-

from src.hash_table import *


def test_OpenAddressingHashTable():
    m = 4
    f = gen_division_hash(m)
    h = gen_lenear_probing(m, f)
    T = OpenAddressingHashTable(m, h)

    T.insert(X(1, 10))
    T.insert(X(2, 20))
    T.insert(X(5, 30))
    T.delete(2)
    assert T.T[2] == OpenAddressingHashTable.DELETED

    T.insert(X(9, 30))
    assert T.T[0] is None
    assert T.T[1] == X(1, 10)
    assert T.T[2] == X(9, 30)
    assert T.T[3] == X(5, 30)

    assert T.search(1) == X(1, 10)
    assert T.search(2) is None
    assert T.search(5) == X(5, 30)
    assert T.search(9) == X(9, 30)
