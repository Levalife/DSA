# -*- coding: utf-8 -*-
from collections import deque

#You are given a pointer to the root of a binary tree. You need to print the level order traversal of this tree. In level order traversal, we visit the nodes level by level from left to right. You only have to complete the function. For example:
#
#     1
#      \
#       2
#        \
#         5
#        /  \
#       3    6
#        \
#         4
#For the above tree, the level order traversal is 1 -> 2 -> 5 -> 3 -> 6 -> 4.

class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

    # You are given a pointer to the root of a binary search tree and values to be inserted into the tree. Insert
    # the values into their appropriate position in the binary search tree and return the root of the updated binary tree.
    # You just have to complete the function.

    def find_parent(self, node, val):
        if val < node.info:
            if not node.left:
                return node
            return self.find_parent(node.left, val)
        else:
            if not node.right:
                return node
            return self.find_parent(node.right, val)

    def insert(self, val):
        # Enter you code here.
        if not self.root:
            self.root = Node(val)
        else:
            node = self.find_parent(self.root, val)
            if node:
                if val < node.info:
                    node.left = Node(val)
                else:
                    node.right = Node(val)
        return self.root


"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""

def levelOrder(root):
    #Write your code here
    q = [root]
    while q:
        node = q.pop(0)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
        print(node.info, end=" ")

def levelOrder(root):
    deck = deque()
    if not root:
        return None
    else:
        deck.append(root)
        while deck:
            x = deck.popleft()
            print(x.info, end=" "),
            if x.left:
                deck.append(x.left)
            if x.right:
                deck.append(x.right)

tree = BinarySearchTree()
inp = '1 2 5 3 4 6'

arr = list(map(int, inp.split()))
for i in arr:
    tree.create(i)

levelOrder(tree.root)