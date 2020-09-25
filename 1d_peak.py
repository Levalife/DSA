# -*- coding: utf-8 -*-


def linear_1d_peak(a):
    for i in range(1, len(a) - 1):
        if a[i] > a[i - 1] and a[i] > a[i + 1]:
            return a[i]
        elif a[i] < a[i - 1]:
            return a[i - 1]
        elif a[i] < a[i + 1] and i + 1 == len(a) - 1:
            return a[i + 1]


# print(linear_1d_peak([1, 2, 3, 4, 2, 1]))
# print(linear_1d_peak([4, 3, 2, 1]))
# print(linear_1d_peak([1, 2, 3, 4]))

def binary_1d_peak(a):
    l = 0
    r = len(a) - 1
    while True:
        m = (l + r) // 2
        if a[m] > a[m - 1] and a[m] < a[m + 1]:
            l = m + 1
        elif a[m] < a[m - 1] and a[m] > a[m + 1]:
            r = m
        else:
            return a[m]


print(binary_1d_peak([1, 2, 3, 4, 2, 1]))
print(linear_1d_peak([4, 3, 2, 1]))
print(linear_1d_peak([1, 2, 3, 4]))
