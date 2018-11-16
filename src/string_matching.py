# -*- coding: utf-8 -*-

from typing import List


def exact_match(T: List, P: List) -> bool:
    """
    T and P are lists of characters.
    The length of them are the same.
    """
    n = len(T)
    m = len(P)
    if n != m:
        raise Exception('The lengths of T and P are different')
    for i in range(0, n):
        if T[i] != P[i]:
            return False
    return True


def naive_string_matcher(T: List, P: List) -> List[int]:
    """
    32.1 Navive String Matcher
    returns a list of matching shifts

    preprocessing: 0
    matching:      O((n - m + 1) * m)
    """
    shifts = []
    n = len(T)
    m = len(P)
    for s in range(0, n - m + 1):
        if exact_match(P, T[s:s + m]):
            shifts.append(s)
    return shifts


if __name__ == '__main__':
    print('x')
