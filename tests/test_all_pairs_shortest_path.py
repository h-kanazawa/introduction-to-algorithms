# -*- coding: utf-8 -*-

import numpy as np

from src.all_pairs_shortest_path import *


INF = float('inf')


def gen_graph():
    return np.array([
        [0, 1, INF, INF],
        [INF, 0, 2, 7],
        [5, INF, 0, 3],
        [INF, INF, INF, 0]
    ])


def test_build_shortest_path():
    Π = np.array([
        [None, 0, 1, 2],
        [2, None, 1, 2],
        [2, 0, None, 2],
        [None, None, None, None]
    ])
    assert build_shortest_path(Π, 0, 0) == [0]
    assert build_shortest_path(Π, 0, 1) == [0, 1]
    assert build_shortest_path(Π, 0, 2) == [0, 1, 2]
    assert build_shortest_path(Π, 0, 3) == [0, 1, 2, 3]

    assert build_shortest_path(Π, 1, 0) == [1, 2, 0]
    assert build_shortest_path(Π, 1, 1) == [1]
    assert build_shortest_path(Π, 1, 2) == [1, 2]
    assert build_shortest_path(Π, 1, 3) == [1, 2, 3]

    assert build_shortest_path(Π, 2, 0) == [2, 0]
    assert build_shortest_path(Π, 2, 1) == [2, 0, 1]
    assert build_shortest_path(Π, 2, 2) == [2]
    assert build_shortest_path(Π, 2, 3) == [2, 3]


    assert build_shortest_path(Π, 3, 0) is None
    assert build_shortest_path(Π, 3, 1) is None
    assert build_shortest_path(Π, 3, 2) is None
    assert build_shortest_path(Π, 3, 3) == [3]


def test_slow_all_pairs_shortest_paths():
    W = gen_graph()
    Lm = slow_all_pairs_shortest_paths(W)
    assert Lm.tolist() == [[0, 1, 3, 6], [7, 0, 2, 5], [5, 6, 0, 3], [INF, INF, INF, 0]]


def test_faster_all_pairs_shortest_paths():
    W = gen_graph()
    Lm = faster_all_pairs_shortest_paths(W)
    assert Lm.tolist() == [[0, 1, 3, 6], [7, 0, 2, 5], [5, 6, 0, 3], [INF, INF, INF, 0]]
