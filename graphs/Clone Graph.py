'''

https://leetcode.com/problems/clone-graph/

https://www.youtube.com/watch?v=vma9tCQUXk8

'''

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':

        if not node:
            return None

        queue = [node]
        clone = dict()
        seen = []
        while queue:
            current = queue.pop()

            if current.val not in clone:
                new = Node(current.val, [] if current.neighbors else None)
                clone[current.val] = new
            else:
                new = clone[current.val]

            seen.append(current)

            for n in current.neighbors:

                if n not in seen and n not in queue:
                    queue.insert(0, n)

                if n.val not in clone:
                    clone[n.val] = Node(n.val, [] if n.neighbors else None)

                new.neighbors.append(clone[n.val])

        return clone[node.val]
