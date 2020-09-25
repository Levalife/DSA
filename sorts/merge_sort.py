# -*- coding: utf-8 -*-

# Рекурсивно разбивать список на 2 пока длина списка не будет равна 1
# Потом, с помощью двух указателей на два списка, постепенно собирать в правильном порядке
# O(n*lgn) time
# O(n) space


def merge(al, ar):
    l = 0
    r = 0
    result = []
    while l < len(al) and r < len(ar):
        if al[l] < ar[r]:
            result.append(al[l])
            l += 1
        else:
            result.append(ar[r])
            r += 1

    for i in range(r, len(ar)):
        result.append(ar[i])

    for i in range(l, len(al)):
        result.append(al[i])
    return result


def merge_sort(a):
    if len(a) == 1:
        return a
    return merge(merge_sort(a[: len(a) // 2]), merge_sort(a[len(a) // 2:]))

a = [5, 2, 4, 6, 1, 3]
print(merge_sort(a))
print(merge_sort([4,7,5,3,8,9,5,2,6,8,19,10,12,11]))