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

Inorder
left node right

1 6 7 8 9 10 11 14 20 22

'''

def inorder_iter_mine(tree):

    stack = [tree.root]
    current = tree.root
    while stack:

        if current:
            if current.left:
                stack.append(current.left)
            current = current.left
        else:

            current = stack.pop()
            print(current.value)

            if current.right:
                stack.append(current.right)
            current = current.right


def inorder_iter(tree):
    stack = []
    current = tree.root
    while stack or current:

        if current:
            stack.append(current)
            current = current.left
        else:
            current = stack.pop()
            print(current.value)
            current = current.right


def inorder_rec(node):

    if node.left:
        inorder_rec(node.left)

    print(node.value)

    if node.right:
        inorder_rec(node.right)

#inorder_rec(tree.root)

inorder_iter(tree)



def inorder_repeat(tree):
    stack = []
    current = tree.root
    while stack or current:

        if current:
            stack.append(current)
            current = current.left
        else:
            current = stack.pop()

            print(current.value)
            current = current.right
print("repeat")
inorder_repeat(tree)









































