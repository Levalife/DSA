# -*- coding: utf-8 -*-


def max_heapify(a, i):
    n = len(a)
    l = 2 * i + 1
    r = 2 * i + 2
    heapified = False
    while not heapified:
        if r < n and a[r] > a[l] and a[r] > a[i]:
            a[r], a[i] = a[i], a[r]
            i = r
        elif l < n and a[l] > a[i]:
            a[l], a[i] = a[i], a[l]
            i = l
        else:
            heapified = True
        l = 2 * i + 1
        r = 2 * i + 2

    return a


def max_heapify_req(a, i):
    n = len(a)
    l = 2 * i + 1
    r = 2 * i + 2
    if l > n and r > n:
        return a
    if r < n and a[r] > a[l] and a[r] > a[i]:
        a[r], a[i] = a[i], a[r]
        return max_heapify_req(a, r)
    elif l < n and a[l] > a[i]:
        a[l], a[i] = a[i], a[l]
        return max_heapify_req(a, l)


def build_max_heap(a):
    for i in range(len(a) // 2, -1, -1):
        max_heapify(a, i)
    return a


def build_max_heap_with_req(a):
    for i in range(len(a) // 2, -1, -1):
        max_heapify_req(a, i)
    return a


if __name__ == '__main__':
    a1 = [4, 14, 7, 2, 8, 1]
    print(max_heapify(a1, 0))

    a2 = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1]
    print(build_max_heap(a2))

    a3 = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
    print(build_max_heap(a3))

    a1 = [4, 14, 7, 2, 8, 1]
    print(max_heapify_req(a1, 0))
    a2 = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1]
    print(build_max_heap_with_req(a2))

    a3 = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
    print(build_max_heap_with_req(a3))

