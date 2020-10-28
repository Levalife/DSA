# -*- coding: utf-8 -*-
'''

https://www.youtube.com/watch?v=ER4ivZosqCg

A =  [0, 1, 2, 0, 2, 1, 1]
Pivot Index = 1

'''


def dutch_national_flag(a, pivot_index):
    forward_pointer = 0
    pivot = a[pivot_index]
    for i in range(len(a)):
        if a[i] < pivot:
            a[i], a[forward_pointer] = a[forward_pointer], a[i]
            forward_pointer += 1

    i = len(a) - 1
    backward_pointer = len(a) - 1
    while i >= 0 and a[i] >= pivot:

        if a[i] > pivot:
            a[i], a[backward_pointer] = a[backward_pointer], a[i]
            backward_pointer -= 1
        i -= 1
        
    return a


A = [0, 1, 2, 0, 2, 1, 1]
pivot = 1

print(dutch_national_flag(A, pivot))