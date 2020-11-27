'''

Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:

Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL

https://leetcode.com/problems/reverse-linked-list-ii/


'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        prev = None
        current = head
        next_node = None
        prev_all = None
        new_end = None
        i = 1

        while i <= n:
            if i > m:
                # while in interval m < i <= n reverse list
                next_node = current.next
                current.next = prev
                prev = current
                current = next
            elif i == m:
                # when i == m: reverse pointer to None and save pointer to this node in variable next_all
                next_node = current.next
                current.next = prev
                prev = current

                # save first node of the interval which at the end will be the last node of the
                # interval so we could set tail of the list to the new_end.next value
                new_end = current
                current = next_node
            else:
                # iterate through linked list until find start of the interval
                # last prev_all will point to the last node before reversed interval so we can set
                # prev_all.next to the new_start of the interval
                prev_all = current
                current = current.next

            i += 1
        if prev_all:
            # set last node before interval to the new first node of the interval (node at which we stopped iteration)
            prev_all.next = prev
        if new_end:
            # set new last node of the reversed interval to the next node after the interval
            new_end.next = current

        if m > 1:
            # if interval starts not from the head of the linked list -> return head
            return head
        else:
            # if interval starts from the head of the linked list -> return new start of the interval
            # (or last node of original interval at which stopped iteration)
            return prev
