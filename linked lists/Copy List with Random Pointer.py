'''

https://leetcode.com/problems/copy-list-with-random-pointer/

https://www.youtube.com/watch?v=OvpKeraoxW0

Use hashmap to store connection between original nodes and clone nodes

Trickier approach with no hashmap on video

'''

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None

        clone = dict()
        current = head

        while current:
            clone[current] = Node(current.val)
            current = current.next

        current = head
        while current:
            current_clone = clone[current]
            if current.next:
                current_clone.next = clone[current.next]
            if current.random:
                current_clone.random = clone[current.random]

            current = current.next

        return clone[head]
