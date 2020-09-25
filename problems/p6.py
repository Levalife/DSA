# -*- coding: utf-8 -*-


import sys

# save actual stdin in case we need it again later
stdin = sys.stdin

sys.stdin = open('simulatedInput.txt','r')
# or whatever else you want to provide the input eg. StringIO
# Enter your code here. Read input from STDIN. Print output to STDOUT
# Enter your code here. Read input from STDIN. Print output to STDOUT

# 1 -419921
# 1 429676
# 3
# 2 429676
# [-419921] INDEX ERROR if A[index] < A[parent]: line 30

heap = []

def min_heapify_up(A, index):
    if index % 2 == 0:
        # right child
        parent = (index - 2) // 2
    else:
        parent = (index - 1) // 2

    if parent >= 0 and index<len(A):
        if A[index] < A[parent]:
            A[index], A[parent] = A[parent], A[index]
            if parent > 0:
                min_heapify_up(A, parent)


def min_heapify_down(A, index):
    l = 2 * index + 1
    r = 2 * index + 2
    if l < len(A) and A[l] < A[index]:
        smallest = l
    else:
        smallest = index

    if r < len(A) and A[r] < A[smallest]:
        smallest = r

    if smallest != index:
        A[index], A[smallest] = A[smallest], A[index]
        min_heapify_down(A, smallest)


i = 0
n = int(input())
for _ in range(n):
    nums = list(map(int, input().split(' ')))

    if nums[0] == 1:
        heap.append(nums[1])
        min_heapify_up(heap, i)
        i += 1

    if nums[0] == 2:
        index = heap.index(nums[1])
        heap[index] = heap[i - 1]
        heap.pop()
        i -= 1
        min_heapify_up(heap, index)
        min_heapify_down(heap, index)

    if nums[0] == 3:
        print(heap[0])




