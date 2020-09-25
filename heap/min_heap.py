# -*- coding: utf-8 -*-
'''
Heap is complete binary tree where every parent node greater then it's children (max heap) or every parent smaller
then it's children (min heap)

sink_up (insert node at the and and sink up)

sink_down (delete root node, move last node to root and sink down to bottom)

create_heap (add node one by one and sink up on every step if needed)

heapify (start from the end and compare each node with it's children, sink down if needed to the bottom)


Making the correct choice between siftUp and siftDown is critical to get O(n) performance for buildHeap,
but does nothing to help one understand the difference between buildHeap and heapSort in general.
Indeed, proper implementations of both buildHeap and heapSort will only use siftDown. The siftUp operation
is only needed to perform inserts into an existing heap, so it would be used to implement a priority queue
using a binary heap, for example.

The heap property specifies that each node in a binary heap must be at least as large as both of its children.
In particular, this implies that the largest item in the heap is at the root. Sifting down and sifting up are
essentially the same operation in opposite directions: move an offending node until it satisfies the heap property:

*    siftDown swaps a node that is too small with its largest child (thereby moving it down) until it is at least as
    large as both nodes below it.
*   siftUp swaps a node that is too large with its parent (thereby moving it up) until it is no larger than the node
    above it.


https://stackoverflow.com/questions/9755721/how-can-building-a-heap-be-on-time-complexity
'''


def sift_up(heap):
    index = len(heap) - 1
    parent = (index - 1) // 2
    while index > 0 and heap[parent] > heap[index]:
        heap[parent], heap[index] = heap[index], heap[parent]
        index = parent
        parent = (index - 1) // 2
    return heap

def insert(heap, a):
    heap.append(a)
    return sift_up(heap)


min_heap = [1,2,3,5,7,9,12,14,17]

#print(insert(min_heap, 4))

def sift_down(heap):
    index = 0
    left = 2 * index + 1
    right = 2 * index + 2
    flag = True

    while flag and left < len(heap):

        if right < len(heap):
            if heap[right] < heap[left]:
                minIndex = right
            else:
                minIndex = left
        else:
            minIndex = left

        if heap[minIndex] < heap[index]:
            heap[minIndex], heap[index] = heap[index],  heap[minIndex]
            index = minIndex
            left = 2 * index + 1
            right = 2 * index + 2
        else:
            flag = False
    return heap


def delete(heap):
    heap[0] = heap[-1]
    return sift_down(heap[:-1])

min_heap = [1, 2, 3, 5, 4, 9, 12, 14, 17, 7]

#print(delete(min_heap))

def make_heap(array):

    '''

    add node one by one and sink up on every step if needed

    '''

    heap = []
    for a in array:
        heap.append(a)
        heap = sift_up(heap)

    return heap

def heap_sort(array):

    '''

    make heap or heapify array
    delete root node one by one, add it to new array (or to the end of the heap in place), sink_down

    '''

    heap = make_heap(array)

    result = []
    while heap:
        result.append(heap[0])
        heap = delete(heap)

    return result

array = [2,5,7,8,3,1,3,6,9,11,32,9]
print(heap_sort(array))


def heapify(heap):

    '''

    start from the end and compare each node with it's children, sink down if needed to the bottom

    '''

    for i in range(len(heap)//2, -1, -1):
        heap[i:] = sift_down(heap[i:])
    return heap

array = [2,5,7,8,3,1,3,6,9,11,32,9]
#print(heapify(array))

def inplace_heapsort(array):

    heap = heapify(array)

    n = len(heap)
    while n > 0:
        heap[0], heap[n - 1] = heap[n - 1], heap[0]
        heap[:n - 1] = sift_down(heap[:n - 1])
        n -= 1
        print(heap)
    return heap[::-1]

array = [2,5,7,8,3,1,3,6,9,11,32,9]
print(inplace_heapsort(array))
