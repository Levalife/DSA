# -*- coding: utf-8 -*-


class Node:

    def __init__(self, value=None, parent=None, left=None, right=None, rank=1):
        self.parent = parent
        self.left = left
        self.right = right
        self.rank = rank
        self.value = value

    def has_left_child(self):
        return self.left

    def has_right_child(self):
        return self.right

    def is_root(self):
        return not self.parent

    def is_leaf(self):
        return not (self.left or self.right)

    def is_left_child(self):
        return self.parent and self.parent.left == self

    def is_right_child(self):
        return self.parent and self.parent.left == self

    def has_any_child(self):
        return self.left or self.right

    def has_both_chhild(self):
        return self.left and self.right

    def replace_node(self, value, left, right, parent):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent
        if self.has_left_child():
            self.left.parent = self

        if self.has_right_child():
            self.right.parent = self

    def find_min(self):
        if self.has_left_child():
            return self.left.find_min()
        return self

    def find_successor(self):
        if self.has_right_child():
            return self.right.find_min()
        else:
            if self.parent:
                if self.is_left_child():
                    return self.parent
                else:
                    return self.parent.find_successor()

    def splice_out(self):
        if self.is_leaf():
            if self.is_left_child():
                self.parent.left = None
            else:
                self.parent.right = None
        elif self.has_any_child():
            if self.has_left_child():
                if self.is_left_child():
                    self.parent.left =self.left
                else:
                    self.parent.right = self.left
                self.left.parent = self.parent
            else:
                if self.is_left_child():
                    self.parent.left = self.right
                else:
                    self.parent.right =self.right
                self.right.parent = self.parent

    def delete(self, value):
        if self.size > 1:
            node = self.find(self.root, value)
            if node:
                self.remove(node)
                self.size -=1
            else:
                raise KeyError('Error, value not in tree')
        elif self.size == 1 and self.root.value == value:
            self.root = None
            self.size -= 1
        else:
            raise KeyError('Error, value not in tree')

    def remove(self, node):
        if not node.left and not node.right:
            self.check_root(node, None)
        elif node.left and node.right:
            succ = node.find_successor()
            succ.splice_out()
            node.value = succ.value
        else:
            if node.right:
                node.right.parent = node.parent
                self.check_root(node, node.right)
            else:
                node.left.parent = node.parent
                self.check_root(node, node.left)

    def check_root(self, old_node, new_node):
        if old_node.parent:
            if old_node == old_node.parent.right:
                old_node.parent.right = new_node
            else:
                old_node.parent.left = new_node


class Tree:

    def __init__(self, root=None):
        self.root = root

    def find(self, node, value):
        if node:
            if node.value == value:
                return node
            elif node.value > value:
                if node.left and node.left.value == value:
                    return node.left
                else:
                    return self.find(node.left, value)
            else:
                if node.right and node.right.value == value:
                    return node.right
                else:
                    return self.find(node.right, value)

    def insert(self, value):
        node = Node(value=value)
        if not self.root:
            self.root = node
        else:
            current = self.root
            while True:
                if current.value >= node.value:
                    current.rank += 1
                    if not current.left:
                        current.left = node
                        node.parent = current
                        break
                    else:
                        current = current.left
                else:
                    current.rank += 1
                    if not current.right:
                        current.right = node
                        node.parent = current
                        break
                    else:
                        current = current.right


def serialize(node):
    if not node:
        return 'None'
    if not node.left and not node.right:
        return '{} ({})'.format(str(node.value), str(node.rank))
    return '<{} ({}): <{}, {}>>'.format(node.value, node.rank, serialize(node.left), serialize(node.right))


# t = Tree()
# t.insert(30)
#
# print(serialize(t.root))
#
# t.insert(17)
# print(serialize(t.root))
#
# t.insert(40)
# t.insert(14)
# print(serialize(t.root))
#
# t.insert(20)
# print(serialize(t.root))


t2 = Tree()
t2.insert(49)
t2.insert(46)
t2.insert(79)
t2.insert(43)
t2.insert(83)
t2.insert(64)
print(t2.root.find_min().value)
print(serialize(t2.root))
