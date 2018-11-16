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


def rabin_karp(T: List, P: List, q: int) -> List[int]:
    """
    32.2 Rabin-Karp
    Σ = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

    Arguments:
        T {List[int]} -- text
        P {List[int]} -- pattern
        d {int} -- size of character set
        q {int} -- a prime number

    Returns:
        List[int] -- list of matching shift
    """
    # fixed d
    d = 10

    shifts = []
    fs = 0
    n = len(T)
    m = len(P)
    h = d ** (m - 1) % q
    p = 0
    t = [0 for i in range(0, n - m + 1)]

    # preprocessing
    for i in range(0, m):
        p = (d * p + P[i]) % q
        t[0] = (d * t[0] + T[i]) % q

    # matching
    for s in range(0, n - m + 1):
        if p == t[s]:
            if exact_match(P, T[s:s + m]):
                shifts.append(s)
            else:
                # false positive
                fs += 1
        if s < n - m:
            t[s + 1] = (d * (t[s] - T[s] * h) + T[s + m]) % q

    return (shifts, fs)

if __name__ == '__main__':
    print('x')
