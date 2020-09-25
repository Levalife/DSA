# -*- coding: utf-8 -*-

class Tree:

    def __init__(self, root=None):
        self.root = root

class Node:

    def __init__(self, value, parent=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

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
tree.root.right.right = Node(20, tree.root.right)
tree.root.left.left.left = Node(1, tree.root.left.left)
tree.root.left.right.right = Node(9, tree.root.left.right)
tree.root.right.right.left = Node(14, tree.root.right.right)
tree.root.right.right.right = Node(22, tree.root.right.right)

'''

Preorder
node left right

10 7 6 1 8 9 11 20 14 22

'''

def preorder_iter(tree):

    stack = [tree.root]
    while stack:
        current = stack.pop()
        print(current.value)
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)

preorder_iter(tree)

print('------')

def preorder_rec(node):

    print(node.value)
    if node.left:
        preorder_rec(node.left)
    if node.right:
        preorder_rec(node.right)

preorder_rec(tree.root)


def preorder_repeat(tree):
    stack = [tree.root]
    current = None
    while stack:
        current = stack.pop()

        print(current.value)

        if current.right:
            stack.append(current.right)

        if current.left:
            stack.append(current.left)

print("repeat")
preorder_repeat(tree)


def preorder_20(tree):
    stack = []
    current = tree.root
    while stack or current:
        if current:
            print(current.value)
            stack.append(current)
            current = current.left
        else:
            current = stack.pop()
            current = current.right

print("repeat 2.0")
preorder_20(tree)



























