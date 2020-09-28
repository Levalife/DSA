# -*- coding: utf-8 -*-

'''

Self-Balancing Binary Search Trees

Height = max(LeftSubTreeHeight, RightSubTreeHeight) + 1
Balanced = LeftSubTreeBalance - RightSubTreeBalance
abs(Balance) <= 1 - tree is balanced
Balance  < 0 - tree is left heavy
Balance >= 2 - tree is right heavy

https://www.youtube.com/watch?v=vRwi_UcZGjU&t=3s

1. Handle left heavy tree (Balance  < 0 or LeftSubTreeHeight > 1 + RightSubTreeHeight):
    1.1 Right rotation (LL imbalance):
          3                    2
        /                   /   \
       2      ----------> 1     3
      /
    1

         4                      2                       2
        /                        \                    /  \
       2     ----------->         4         ------>  1    4
     /   \                                               /
    1     3                                             3

    Right child of 2 goes as left child of 4

    node = 4
    node.left = 2
    node.left.right = 3

    temp = node.left.right
    node.left.right = node (set 4 as 2 right child)
    node.left = temp (set 3 as 4's left child instead of 2)

    1.2 Left - Right rotation (LR imbalance)

      3                       3
     /                       /
    1     -------------->   2      ---------> 1.1
     \                     /
      2                   1

2. Handle Right heavy tree (Balance >= 2 or RightSubTreeHeight > 1 + LeftSubTreeHeight):
    2.1 Left rotation (RR imbalance):
          1                        2
           \                     /   \
            2   ----------->    1     3
             \
              3


        1                       3                       3
         \                     /                      /   \
          3     -----------> 1        --------->    1       4
        /   \                                        \
       2    4                                         2

       Left child of 3 goes as  right child of 1

       node = 1
       node.right = 3
       node.right.left = 2

       temp = node.right.left
       node.right.left = 1
       node.right = temp

    2.2 Right left rotation (RL imbalance)

        1               1
         \               \
          3 -------->     2      --------> 2.1
         /                 \
        2                   3


    insert
    remove
'''

class Node:

    def __init__(self, val, left=None, right = None, parent = None):
        self.left = left
        self.right = right
        self.parent = parent
        self.val = val
        self.height = 0

    def __str__(self):
        return "{} {}".format(self.val, self.height)

class Tree:

    def __init__(self, root=None):
        self.root = root

    def insert(self, val):
        if not self.root:
            new_node = Node(val)
            self.update_height(new_node)
            self.root = new_node
        else:
            new_node = Node(val)
            current = self.root
            while True:
                if val > current.val:
                    if not current.right:

                        current.right = new_node
                        new_node.parent = current
                        break
                    else:
                        current = current.right
                else:
                    if not current.left:

                        current.left = new_node
                        new_node.parent = current
                        break
                    else:
                        current = current.left
            self.rebalance(new_node)

    def rebalance(self, node):
        while node:
            self.update_height(node)
            balance = self.height(node.left) - self.height(node.right)

            if balance < -1:
                # right side unbalanced tree
                # need to make left rotation
                # or right left rotation
                print("right heavy tree")
                if node.right.right:
                    self.left_rotation(node)
                else:
                    print("right left rotation")
                    self.right_rotation(node.right)
                    self.left_rotation(node)

            elif balance > 1:
                # left side unbalanced tree
                # need to make right rotation
                # or left right rotation
                print("left heavy tree")
                if node.left.left:
                    self.right_rotation(node)
                else:
                    print("left right rotation")
                    self.left_rotation(node.left)
                    self.right_rotation(node)

            node = node.parent


    def update_height(self, node):
        if node:
            node.height = max(self.height(node.left),
                              self.height(node.right)) + 1

    def height(self, node):
        if not node:
            return -1
        return node.height

    def left_rotation(self, node):
        temp = node.right.left
        node.right.left = node
        node.right.parent = node.parent

        if not node.parent:
            self.root = node.right
        elif node.parent.left == node:
            node.parent.left = node.right
        elif node.parent.right == node:
            node.parent.right = node.right
        node.parent = node.right
        node.right = temp

        self.update_height(node)
        self.update_height(node.parent)

    def right_rotation(self, node):

        temp = node.left.right
        node.left.right = node
        node.left.parent = node.parent

        if not node.parent:
            self.root = node.left
        elif node.parent.right == node:
            node.parent.right = node.left
        elif node.parent.left == node:
            node.parent.left = node.left
        node.parent = node.left
        node.left = temp

        self.update_height(node)
        self.update_height(node.parent)

    def __str__(self):
        stack = []
        current = tree.root
        result = []
        while stack or current:

            if current:
                result.append(str(current))
                stack.append(current)
                current = current.left
            else:
                current = stack.pop()


                current = current.right
        return ','.join(result)

tree = Tree()
tree.insert(30)
tree.insert(10)
tree.insert(20)

print(tree)

