# -*- coding: utf-8 -*-

from typing import List


def recursive_activity_selector(s: List[int], f: List[int], k: int, n: int):
    """
    16.1 P349

    Args:
        s (List[int]): list of activity starting time
        f (List[int]): list of activity finishing time
        k int: kth activity
        n int: number of activities
    Returns:
        List[int]: set of activities
    """
    m = k + 1
    while m <= n and s[m] < f[k]:
        m = m + 1
    if m <= n:
        return [m] + recursive_activity_selector(s, f, m, n)
    else:
        return []


def greedy_activity_selector(s: List[int], f: List[int]):
    """
    16.1 P350

    Args:
        s (List[int]): list of activity starting time
        f (List[int]): list of activity finishing time
    Returns:
        List[int]: set of activities
    """
    n = len(s)
    A = [1]
    k = 1
    for m in range(2, n):
        if s[m] >= f[k]:
            A = A + [m]
            k = m
    return A


if __name__ == '__main__':
    s = [0, 1, 3, 0, 5, 3, 5, 6, 8, 8, 2, 12]
    f = [0, 4, 5, 6, 7, 9, 9, 10, 11, 12, 14, 16]
    ans = greedy_activity_selector(s, f)
    print(ans)
