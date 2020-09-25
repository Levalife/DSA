# -*- coding: utf-8 -*-

# Улучшеная Insertion Sort, где каждый список разбит на подсписки. Выбирает подсписки, где элементы находятся с шагом i
# Сведенные списки сортируются Insertion Sort
# O(n^2) time

def insertion_sort(a, start, step):
    for i in range(start, len(a), step):
        k = a[i]
        while i > start and a[i - step] > k:
            a[i] = a[i - step]
            i -= step
        a[i] = k
    return a


def shell_sort(a):
    i = 2
    for j in range(i):
        insertion_sort(a, j, 2)
    return insertion_sort(a, 0, 1)


a = [5, 2, 4, 6, 1, 3]
# print(shell_sort(a))
print(shell_sort([4, 7, 5, 3, 8, 9, 5, 2, 6, 8, 19, 10, 12, 11]))
