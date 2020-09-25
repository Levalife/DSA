# -*- coding: utf-8 -*-


# Во время прохода запоминается индекс самого большого неотсортированного элемента и свапится в конец
# O(n^2) time
# O(1) space


def selection_sort(a):
    for i in range(len(a)):
        max = 0
        for j in range(len(a) - i):
            if a[j] > a[max]:
                max = j
        a[j], a[max] = a[max], a[j]
    return a


a = [5, 2, 4, 6, 1, 3]
print(selection_sort(a))
print(selection_sort([4, 7, 5, 3, 8, 9, 5, 2, 6, 8, 19, 10, 12, 11]))
