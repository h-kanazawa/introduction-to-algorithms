# -*- coding: utf-8 -*-

from typing import List

"""
16[1,2,3,4,5,6,7,8,9,10]

1
├──────┐
2      3
├───┐  ├─┐
4   5  6 7
├─┐ │
8 9 10

parent(i)
  return
"""


def parent(i):
    return i >> 1


def left(i):
    return i << 1


def right(i):
    return (i << 1) + 1


# This function is not pure. it has "effect".
def max_heapfy(A: List[int], i: int):
    l = left(i)
    r = right(i)
    # What is the definition of heap_size?
    heap_size = len(A)

    # Find the largest subscript in A[left], A[right] and A[i - 1]
    if l <= heap_size and A[l - 1] > A[i - 1]:
        largest = l
    else:
        largest = i
    if r <= heap_size and A[r - 1] > A[largest - 1]:
        largest = r

    if largest != i:
        # Change A[i] and A[largest]
        t = A[i - 1]
        A[i - 1] = A[largest - 1]
        A[largest - 1] = t

        max_heapfy(A, largest)

    return


def heap_sort(A: List[int]) -> List[int]:
    return


if __name__ == '__main__':
    print('x')
