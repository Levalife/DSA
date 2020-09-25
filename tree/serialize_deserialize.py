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


def serialize(node):
    if not node:
        return "X,"

    return "{},{}{}".format(node.value, serialize(node.left), serialize(node.right))

serialized_tree = serialize(tree.root)
print(serialized_tree)

def deserialize(tree_str):
    tree_list = tree_str.split(',')
    return deserialize_helper(tree_list)


def deserialize_helper(tree_list):
    if tree_list:
        if tree_list[0] == 'X':
            tree_list.pop(0)
            return None
        newNode = Node(value=tree_list.pop(0))
        newNode.left = deserialize_helper(tree_list)
        newNode.right = deserialize_helper(tree_list)

        return newNode

deserialized_tree = deserialize(serialized_tree)

def preorder(node):

    print(node.value)
    if node.left:
        preorder(node.left)
    if node.right:
        preorder(node.right)

preorder(deserialized_tree)