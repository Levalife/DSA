# -*- coding: utf-8 -*-

# For the purposes of this challenge, we define a binary tree to be a binary search tree with the following ordering requirements:
#
# The  value of every node in a node's left subtree is less than the data value of that node.
# The  value of every node in a node's right subtree is greater than the data value of that node.
# Given the root node of a binary tree, can you determine if it's also a binary search tree?
#
# Complete the function in your editor below, which has  parameter: a pointer to the root of a binary tree. It must return a boolean denoting whether or not the binary tree is a binary search tree. You may have to write one or more helper functions to complete this challenge.
#
# Input Format
#
# You are not responsible for reading any input from stdin. Hidden code stubs will assemble a binary tree and pass its root node to your function as an argument.
#
# Constraints
# 0 <= data <=10000

""" Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""

def check(node, min, max):
    if not node:
        return True
    if min < node.data < max:
        return check(node.left, min, node.data) and check(node.right, node.data, max)

def check_binary_search_tree_(root):
    return check(root, -1, 10001)

# OR

def inOrder(stack, node):
    if node:
        if node.left:
            inOrder(stack, node.left)
        stack.append(node.data)
        if node.right:
            inOrder(stack, node.right)

def check_binary_search_tree_(root):
    stack = []
    inOrder(stack, root)
    prev = 10001
    while stack:
        c = stack.pop()
        if c >= prev:
            return False
        prev = c
    return True