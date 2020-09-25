# -*- coding: utf-8 -*-

# Rooted tree are defined by some as a directed graph.
# In graph theory a tree is an undirected graph

# https://www.youtube.com/watch?v=nPtARJ2cYrg
# https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/
# We need to turn directed graph into undirected graph
# 1. With traversal create hashtable that shows pairs of node - parent
# 2. Use BFS (breadth first search) to find K's level of nodes

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:

        parents = dict()
        # inorder traversal to create hashmap with parents
        stack = []
        current = root
        while current or stack:
            if current:
                stack.append(current)
                current = current.left
            else:
                current = stack.pop()
                if current.left:
                    parents[current.left] = current
                if current.right:
                    parents[current.right] = current

                current = current.right

        seen = set()
        queue = []
        current_level = 0
        queue.append(target)
        while current_level < K:
            for _ in range(len(queue)):
                current = queue.pop(0)
                seen.add(current)
                if current.left and current.left not in seen:
                    queue.append(current.left)
                if current.right and current.right not in seen:
                    queue.append(current.right)
                if parents.get(current) and parents.get(current) not in seen:
                    queue.append(parents.get(current))
            current_level += 1

        return [node.val for node in queue]

