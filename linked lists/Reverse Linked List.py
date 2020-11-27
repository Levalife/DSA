'''

Recursively and iteratively

https://leetcode.com/problems/reverse-linked-list/

https://www.youtube.com/watch?v=O0By4Zq0OFc

'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:

        if not head or not head.next:
            return head

        # go till the end of the list recursively
        reversedHead = self.reverseList(head.next)
        # starting from penult value reverse pointers
        head.next.next = head
        head.next = None

        return reversedHead

    def reverseListIteratively(self, head: ListNode) -> ListNode:
        prev = None
        current = head
        next_node = None
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        return prev