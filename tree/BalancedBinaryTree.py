# -*- coding: utf-8 -*-

'''

Property of Balanced Binary Tree: absolute value (abs) of difference of left subtree and right subtree must be lower or
equal to 1.
Height of leaf is -1
Overall tree mite look as balanced (height left - height right <= 1) but if one of subtrees is unbalanced all tree is
unbalanced

Height of tree is equal to max value of height of the children plus 1: max(height_left, height_right) + 1

User helper function to call recursivly to track is_balanced status and height of the subtrees

https://leetcode.com/problems/balanced-binary-tree/

https://www.youtube.com/watch?v=LU4fGD-fgJQ

'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        is_balanced, height = self.helper(root)
        return is_balanced

    def helper(self, node: TreeNode) -> (bool, int):

        if not node:
            return True, -1

        is_balanced_left, height_left = self.helper(node.left)

        is_balanced_right, height_right = self.helper(node.right)

        height = max(height_left, height_right) + 1

        if not is_balanced_left or not is_balanced_right or abs(height_left - height_right) > 1:
            return False, height

        return True, height