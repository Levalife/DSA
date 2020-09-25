# -*- coding: utf-8 -*-
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/submissions/
# https://www.youtube.com/watch?v=py3R23aAPCA&list=PLiQ766zSC5jND9vxch5-zT7GuMigiWaV_&index=2&ab_channel=BackToBackSW

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None

        if root == p or root == q:
            return root

        leftChild = self.lowestCommonAncestor(root.left, p, q)
        rightChild = self.lowestCommonAncestor(root.right, p, q)

        if not leftChild:
            return rightChild
        if not rightChild:
            return leftChild

        return root