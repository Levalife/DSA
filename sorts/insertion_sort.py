# -*- coding: utf-8 -*-

# O(n^2) time
# O(1) space (in-place sorting)

# В лекциях MIT курс 6,006 производили не просто сдвиг, а свапали все значения местами, пока не находили нужное место


def insertion_sort(a):
    for i in range(1, len(a)):
        k = a[i]
        while i > 0 and k < a[i - 1]:
            if a[i] < a[i - 1]:
                a[i], a[i - 1] = a[i - 1], a[i]
            i -= 1
    return a


a = [5, 2, 4, 6, 1, 3]
print(insertion_sort(a))
print(insertion_sort([4, 7, 5, 3, 8, 9, 5, 2, 6, 8, 19, 10, 12, 11]))


# Первый элемент принимается за отсортированный список и при каждой итерации расширяется на 1 элемент.
# Сравнивается и сдвигается все, пока не найдена позиция нового эл-нта. Эффективнее обмена (одно присвоение вместо трез)

def insertion_sort1(a):
    for i in range(1, len(a)):
        k = a[i]
        while i > 0 and a[i - 1] > k:
            a[i] = a[i - 1]
            i -= 1
        a[i] = k

    return a


a = [5, 2, 4, 6, 1, 3]
print(insertion_sort1(a))
print(insertion_sort1([4, 7, 5, 3, 8, 9, 5, 2, 6, 8, 19, 10, 12, 11]))
