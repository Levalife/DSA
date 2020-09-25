# -*- coding: utf-8 -*-

# Priority Queue Abstract Data Type
# Heap is a complete binary tree (complete means it's filled from left to right)
# There are two types of heap: min heap and max heap

# When see problems like "the largest of smth/ the lowest of smth immediately think of using heap"

class MinHeap:

    def __init__(self, *args):
        self.heap = list(*args)

    def insert(self, value):
        self.heap.append(value)

        self.siftUp()


    def siftUp(self):
        current = len(self.heap) - 1
        parent = (current - 1) // 2
        #print(current, parent, self.heap[current], self.heap[parent], self.heap[current] < self.heap[parent])
        while parent >= 0 and self.heap[current] < self.heap[parent]:

            self.heap[current], self.heap[parent] = self.heap[parent], self.heap[current]
            current = parent
            parent = (current - 1) // 2


    def remove(self):

        self.heap[0] = self.heap[-1]
        self.heap = self.heap[:-1]

        self.siftDown()

    def siftDown(self):
        current = 0
        leftChild = current * 2 + 1
        rightChild = current * 2 + 2
        flag = True
        while leftChild < len(self.heap) and flag:

            if rightChild < len(self.heap):
                if self.heap[rightChild] < self.heap[leftChild]:
                    minIndex = rightChild
                else:
                    minIndex = leftChild
            else:
                minIndex = leftChild

            if self.heap[minIndex] < self.heap[current]:
                self.heap[minIndex], self.heap[current] = self.heap[current], self.heap[minIndex]
                current = minIndex
                leftChild = current * 2 + 1
                rightChild = current * 2 + 2
            else:
                flag = False

    def __str__(self):
        return "{}".format(self.heap)


heap = MinHeap()
heap.insert(10)
heap.insert(4)
heap.insert(15)
heap.remove()
#print(heap.heap)
heap.insert(20)
heap.insert(0)
heap.insert(30)
heap.remove()
#print(heap.heap)
heap.remove()
#print(heap.heap)
heap.insert(2)
heap.insert(4)
heap.insert(-1)
heap.insert(-3)

print(heap)