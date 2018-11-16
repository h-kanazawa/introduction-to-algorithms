# -*- coding: utf-8 -*-

from src.finite_automaton_matcher import *


def test_finite_automaton_matcher():
    # 32.3-1
    P = list('aabab')
    T = list('aaababaabaababaab')
    Σ = set(P + T)
    m = len(P)
    δ, _ = compute_transition_function(P, Σ)

    assert finite_automaton_matcher(T, δ, m) == [1, 9]

def test_compute_transition_function():
    # 32.7
    P = list('ababaca')
    Σ = { 'a', 'b', 'c' }
    δ, _ = compute_transition_function(P, Σ)
    assert δ(0, 'a') == 1
    assert δ(0, 'b') == 0
    assert δ(0, 'c') == 0

    assert δ(1, 'a') == 1
    assert δ(1, 'b') == 2
    assert δ(1, 'c') == 0

    assert δ(2, 'a') == 3
    assert δ(2, 'b') == 0
    assert δ(2, 'c') == 0

    assert δ(3, 'a') == 1
    assert δ(3, 'b') == 4
    assert δ(3, 'c') == 0

    assert δ(4, 'a') == 5
    assert δ(4, 'b') == 0
    assert δ(4, 'c') == 0

    assert δ(5, 'a') == 1
    assert δ(5, 'b') == 4
    assert δ(5, 'c') == 6

    assert δ(6, 'a') == 7
    assert δ(6, 'b') == 0
    assert δ(6, 'c') == 0

    assert δ(7, 'a') == 1
    assert δ(7, 'b') == 2
    assert δ(7, 'c') == 0



def test_is_suffix():
    x = list('bcd')
    y = list('abcd')
    assert is_suffix(x, y) == True

    x = list('abcd')
    y = list('abcd')
    assert is_suffix(x, y) == True

    x = list('bcd')
    y = list('abacd')
    assert is_suffix(x, y) == False
