# -*- coding: utf-8 -*-
# Given a binary tree, each node has value 0 or 1.  Each root-to-leaf path represents a binary number starting with the most significant bit.  For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary, which is 13.

# For all leaves in the tree, consider the numbers represented by the path from the root to that leaf.

# Return the sum of these numbers.

def sumRootToLeaf(root):
    def dfs(root):
        if root:
            arr = []
            if not root.left and not root.right:
                return [str(root.val)]
            if root.left:
                arr += dfs(root.left)
            if root.right:
                arr += dfs(root.right)

            return [str(root.val) + i for i in arr]
        return ['']

    # convert binary number to decimal number int(b, 2)
    return sum(int(i, 2) for i in dfs(root))
