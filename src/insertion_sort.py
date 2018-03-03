# -*- coding: utf-8 -*-

from typing import List


def sort(arr: List[int]) -> List[int]:
    """insertion sort
    """
    for j in range(1, len(arr)):
        key = arr[j]
        i = j - 1
        while i >= 0 and arr[i] > key:
            arr[i + 1] = arr[i]
            i = i - 1
        arr[i + 1] = key

    return arr


def desc_sort(arr: List[int]) -> List[int]:
    """2.1-2
    """
    for j in range(1, len(arr)):
        key = arr[j]
        i = j - 1
        while i >= 0 and arr[i] < key:
            arr[i + 1] = arr[i]
            i = i - 1
        arr[i + 1] = key

    return arr


if __name__ == '__main__':
    print(sort([5, 1, 4, 2, 3]))
