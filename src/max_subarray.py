# -*- coding: utf-8 -*-

from typing import List
from math import floor


def find_max_subarray(A: List[float], low: int, high: int) -> List[float]:
    if high == low:
        return (low, high, A[low])
    else:
        mid = floor((low + high) / 2)
        (left_low, left_high, left_sum) = find_max_subarray(A, low, mid)
        (right_low, right_high, right_sum) = find_max_subarray(A, mid + 1, high)
        (cross_low, cross_high, cross_sum) = find_max_crossing_subarray(A, low, mid, high)

        # Compare maxses of left subarray, right subarray, and cross subarray
        if left_sum >= right_sum and left_sum >= cross_sum:
            return (left_low, left_high, left_sum)
        if right_sum >= left_sum and right_sum >= cross_sum:
            return (right_low, right_high, right_sum)
        return (cross_low, cross_high, cross_sum)


def find_max_crossing_subarray(A: List[float], low: int, mid: int, high: int):
    # Find max left
    left_sum = float('-inf')
    _sum = 0
    for i in range(mid, low - 1, -1):
        _sum = _sum + A[i]
        if _sum > left_sum:
            left_sum = _sum
            max_left = i

    # Find max right
    right_sum = float('-inf')
    _sum = 0
    for j in range(mid + 1, high + 1):
        _sum = _sum + A[j]
        if _sum > right_sum:
            right_sum = _sum
            max_right = j

    return (max_left, max_right, left_sum + right_sum)


if __name__ == '__main__':
    A = [5, 1, 4, 2, 3, 1.4, 7.9, 0, -10, -83, 9, 1, 10, -3.3]
    print(find_max_subarray(A, 0, len(A) - 1))
