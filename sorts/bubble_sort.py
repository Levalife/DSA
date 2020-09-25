# -*- coding: utf-8 -*-

# Каждый раз "всплывает" самый большой элемент в конец, попарным сравнением
# O(n^2) time
# O(1) space


def bubble_sort(a):
    """
    >>> bubble_sort([5, 2, 4, 6, 1, 3])
    [1, 2, 3, 4, 5, 6]
    """

    for i in range(1, len(a)):
        for j in range(len(a) - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a

a = [5, 2, 4, 6, 1, 3]
print(bubble_sort(a))
print(bubble_sort([4,7,5,3,8,9,5,2,6,8,19,10,12,11]))