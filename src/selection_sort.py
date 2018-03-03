# -*- coding: utf-8 -*-

from typing import List


def sort(arr: List[int]) -> List[int]:
    """2.2-2
    selection sort
    """
    m = len(arr)
    for j in range(0, m - 1):

        # Fine minimum value in arr[j] ~ arr[m]
        key = j
        for i in range(j + 1, m):
            if arr[i] < arr[key]:
                key = i

        # Change minimum value and arr[j]
        t = arr[j]
        arr[j] = arr[key]
        arr[key] = t

    return arr


if __name__ == '__main__':
    print(sort([5, 1, 4, 2, 3]))
