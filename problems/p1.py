# -*- coding: utf-8 -*-

# Write a function that receives two sorted arrays of integers as arguments and outputs the intersection
#of these two arrays.

#Example:
#a1: 1, 3, 4, 11, 107
#a2: 2, 3, 11
#result = > 3, 11

# Time: O(n)
# Space: O(n)

#If а2 very short (3), а1 very long (10000)

# Time: O(n + m)
# Space: O(min(n, m))

# a1 = [1, 2, 3, 4]
# a2 = [1, 2, 3, 4]


def solution1(a, b):
    '''
    Time O(n^2)
    Space O(n)
    '''
    result = []
    for el1 in a:
        for el2 in b:
            if el1 == el2:
                result.append(el1)
    return result


def solution2(a, b):
    '''

    Time O(n)
    Space O(n)
    '''
    n = len(a)
    m = len(b)
    pointer1 = pointer2 = 0
    result = []
    while pointer1 < n and pointer2 < m:
        if a[pointer1] == b[pointer2]:
            result.append(a[pointer1])
            pointer1 += 1
            pointer2 += 1
        elif a[pointer1] < b[pointer2]:
            pointer1 += 1
        else:
            pointer2 += 1
    return result


def solution3(a, b):
    '''
    Time O(m + n)
    Space min(n, m)
    '''
    b = {el for el in b}
    result = []
    for el in a:
        if el in b: # O(1)
            result.append(el)
    return result


a1 = [1, 3, 4, 11, 107]
a2 = [2, 3, 11]
print(solution1(a1, a2))
print(solution2(a1, a2))
print(solution3(a1, a2))

a1 = [1, 2, 3, 4]
a2 = [1, 2, 3, 4]
print(solution1(a1, a2))
print(solution2(a1, a2))
print(solution3(a1, a2))