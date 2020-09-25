# -*- coding: utf-8 -*-
# Given a sequence of numbers, find the longest sequence that contains only 2 unique numbers.

# Example:
# Input: [1, 3, 5, 3, 1, 3, 1, 5]
# Output: 4
# The longest sequence that contains just 2 unique numbers is [3, 1, 3, 1]


def findSequence(seq):
    subseq = []
    max_len = 0
    for el in seq:
        subseq.append(el)

        if len(set(subseq)) > 2:
            if len(subseq) - 1 > max_len:
                max_len = len(subseq) - 1
            subseq = subseq[-2:]

    if len(subseq) > max_len:
        max_len = len(subseq)
    return subseq, max_len


# print(findSequence([1, 3, 5, 3]))
# 3
# print(findSequence([1, 3, 5, 3, 1, 3, 1, 5]))
# 4
# print(findSequence([1, 3, 5, 3, 1, 3, 1, 3, 1, 1, 3, 5]))
# 8

def findSequence2(seq):
    subseq = set()
    max_len = 0
    start = 0
    end = 0
    for i, el in enumerate(seq):
        if len(subseq) < 2:
            if el not in subseq:
                subseq.add(el)
            end = i
        else:
            if el in subseq:
                end = i
            else:
                subseq_len = end - start + 1

                if subseq_len > max_len:
                    max_len = subseq_len
                start = end
                end = i
                subseq = {seq[start], seq[end]}

    subseq_len = end - start + 1
    if subseq_len > max_len:
        max_len = subseq_len

    return max_len


print(findSequence2([1, 3, 5, 3]))
# 3
print(findSequence([1, 3, 5, 3, 1, 3, 1, 5]))
# 4
print(findSequence([1, 3, 5, 3, 1, 3, 1, 3, 1, 1, 3, 5]))
# 8

def helper(s):
    memo = {}

    longest = [0, 1]
    start_index = 0

    for idx, i in enumerate(s):
        if i not in memo:
            memo[i] = idx
        else:
            start_index = max(start_index, memo[i])
            d = {}
            for y in range(start_index, idx + 1):
                if s[y] not in d:
                    d[s[y]] = 1
                else:
                    d[s[y]] += 1
            if len(d) == 2 and longest[1] - longest[0] < idx + 1 - start_index:
                longest = [start_index, idx + 1]
                memo[i] = idx

    return len(s[longest[0]:longest[1]])

# print(helper([1, 3, 5, 3]))
# 3
# print(helper([1, 3, 5, 3, 1, 3, 1, 5]))
# 4
# print(helper([1, 3, 5, 3, 1, 3, 1, 3, 1, 1, 3, 5]))
# 8
