# -*- coding: utf-8 -*-
from heap.max_heap import build_max_heap, max_heapify


# O(n * logn)

def heap_sort(a):
    max_heap = build_max_heap(a)
    n = len(a)
    result = []
    while n > 1:
        n = len(max_heap)
        max_heap[0], max_heap[n - 1] = max_heap[n - 1], max_heap[0]
        result.append(max_heap[n - 1])
        max_heap = max_heapify(max_heap[:n - 1], 0)
    return result


def asc_heap_sort(a):
    max_heap = build_max_heap(a)
    n = len(a)
    min_sort = []
    while n > 1:
        n = len(max_heap)
        max_heap[0], max_heap[n - 1] = max_heap[n - 1], max_heap[0]
        min_sort.insert(0, max_heap[n - 1])
        max_heap = max_heapify(max_heap[:n - 1], 0)
    return min_sort


a = [9, 10, 16, 3, 2, 14, 4, 8, 1, 7]
print(heap_sort(a))

a = [9, 10, 16, 3, 2, 14, 4, 8, 1, 7]
print(asc_heap_sort(a))
