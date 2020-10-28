'''

REQUIRES TO USE MIN HEAP FOR MERGE PURPOSES

https://leetcode.com/problems/merge-k-sorted-lists/

https://www.youtube.com/watch?v=ptYUCjfNhJY

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        self.heap = []
        self.sorted = None
        self.last = None
        for el in lists:
            if el:
                self.insert(el)

        while self.heap:
            self.remove()

            if self.last.next:
                self.insert(self.last.next)
        return self.sorted

    def insert(self, value):
        self.heap.append(value)
        self.sift_up()

    def sift_up(self):
        current = len(self.heap) - 1
        parent = (current - 1) // 2
        while current > 0 and self.heap[current].val < self.heap[parent].val:
            if self.heap[current].val < self.heap[parent].val:
                self.heap[current], self.heap[parent] = self.heap[parent], self.heap[current]
                current = parent
                parent = (current - 1) // 2

    def remove(self):

        if not self.sorted:
            self.sorted = self.heap[0]
            self.last = self.heap[0]
        else:
            self.last.next = self.heap[0]
            self.last = self.last.next

        self.heap[0] = self.heap[-1]
        self.heap = self.heap[:-1]
        self.sift_down()

    def sift_down(self):
        current = 0
        left = current * 2 + 1
        right = current * 2 + 2
        flag = False

        while left < len(self.heap) and not flag:
            if right < len(self.heap):
                if self.heap[right].val < self.heap[left].val:
                    min_index = right
                else:
                    min_index = left
            else:
                min_index = left

            if self.heap[min_index].val < self.heap[current].val:
                self.heap[min_index], self.heap[current] = self.heap[current], self.heap[min_index]
                current = min_index
                left = current * 2 + 1
                right = current * 2 + 2
            else:
                flag = True




