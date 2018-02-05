# -*- coding: utf-8 -*-

from typing import List


# 2.2-2 selection sort
def sort(arr: List[int]) -> List[int]:
    m = len(arr)
    for j in range(0, m - 1):

        # arr[j] ~ arr[m] の中の最小値を見つける
        key = j
        for i in range(j + 1, m):
            if arr[i] < arr[key]:
                key = i

        # 最小値とarr[j]を交換する
        t = arr[j]
        arr[j] = arr[key]
        arr[key] = t

    return arr


if __name__ == '__main__':
    print(sort([5, 1, 4, 2, 3]))
