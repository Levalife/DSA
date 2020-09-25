# -*- coding: utf-8 -*-
'''

https://leetcode.com/problems/symmetric-tree/

https://www.youtube.com/watch?v=XV7Sg2hJO3Q

'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:

        return not root or self.check(root.left, root.right)

    def check(self, leftSubtree: TreeNode, rightSubtree: TreeNode) -> bool:

        if not leftSubtree and not rightSubtree:
            return True
        elif not leftSubtree or not rightSubtree:
            return False
        elif leftSubtree.val == rightSubtree.val and \
                self.check(leftSubtree.left, rightSubtree.right) and \
                self.check(leftSubtree.right, rightSubtree.left):
            return True

        return False
