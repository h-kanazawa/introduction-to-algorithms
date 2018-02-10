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


def max_heapfy(A: List[int], i: int, heap_size: int):
    """O(ln (n))
    This function is not pure. it has "effect".
    """
    l = left(i)
    r = right(i)

    # Find the largest subscript in A[l - 1], A[r - 1] and A[i - 1]
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

        max_heapfy(A, largest, heap_size)

    return


def build_max_heap(A: List[int]):
    """O(n ln(n))
    This function is not pure. it has "effect".
    """
    for i in range(len(A) >> 1, 0, -1):
        max_heapfy(A, i, len(A))


def heap_sort(A: List[int]):
    """O(n ln(n))
    """
    heap_size = len(A)
    build_max_heap(A)
    for i in range(len(A) - 1, 0, -1):
        # Change A[0] and A[i]
        t = A[0]
        A[0] = A[i]
        A[i] = t

        heap_size = heap_size - 1
        max_heapfy(A, 1, heap_size)


if __name__ == '__main__':
    A = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
    print(A)
    heap_sort(A)
    print(A)
