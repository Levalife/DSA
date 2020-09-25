# -*- coding: utf-8 -*-
# Tree is acyclic connected graph
# While preorder, inorder and postorder are similar to DFS and use stacks
# Level order traversal is similar to BFS and uses queues
from typing import List


class Tree:

    def __init__(self, root=None):
        self.root = root


class Node:

    def __init__(self, value, parent=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

    def __str__(self):
        return self.value

    def __unicode__(self):
        return self.value

    def __repr__(self):
        return str(self.value)


'''
                    10
            7               11
        6       8               20
    1               9       14      22

'''
tree = Tree()
tree.root = Node(10)
tree.root.left = Node(7, tree.root)
tree.root.right = Node(11, tree.root)
tree.root.left.left = Node(6, tree.root.left)
tree.root.left.right = Node(8, tree.root.left)
#tree.root.right.left = Node(12, tree.root.right)
tree.root.right.right = Node(20, tree.root.right)
tree.root.left.left.left = Node(1, tree.root.left.left)
tree.root.left.right.right = Node(9, tree.root.left.right)
tree.root.right.right.left = Node(14, tree.root.right.right)
tree.root.right.right.right = Node(22, tree.root.right.right)

'''

Level order
node left1 right1 left2.1 right2.1 left2.2 right 2.2

10 7 11 6 8 20 1 9 14 22

'''

def levelOrder(tree):
    queue = []
    queue.append(tree.root)
    while queue:
        current = queue.pop(0)
        print(current.value)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

levelOrder(tree)


# https://leetcode.com/problems/binary-tree-level-order-traversal/submissions/
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        queue = []
        if root:
            queue.append(root)
        result = []
        while queue:
            level = []
            for _ in range(len(queue)):
                current = queue.pop(0)
                level.append(current.val)

                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)

            result.append(level)
        return result