# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-


class Node:

    def __init__(self, value=None, parent=None, left=None, right=None, rank=1):
        self.parent = parent
        self.left = left
        self.right = right
        self.rank = rank
        self.value = value


class Tree:

    def __init__(self, root=None):
        self.root = root
        self.size = 0

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
        self.size += 1
        self.rebalance(node)

    def rebalance(self, node):
        while node:
            self.update_height(node)
            if self.height(node.left)> 1 + self.height(node.right):
                # left unbalanced
                if self.height(node.left.left) >= self.height(node.left.right):
                    self.right_rotation(node)
                else:
                    self.left_rotation(node.left)
                    self.right_rotation(node)
            elif self.height(node.right) > 1 + self.height(node.left):
                # right unbalanced
                if self.height(node.right.right) >= self.height(node.right.left):
                    self.left_rotation(node)
                else:
                    self.right_rotation(node.right)
                    self.left_rotation(node)
            node = node.parent

    def update_height(self, node):
        node.height = max(self.height(node.left), self.height(node.right)) + 1

    @staticmethod
    def height(node):
        if not node:
            return -1
        else:
            return node.height

    def right_rotation(self, node):
        x = node
        y = node.left
        if not x.parent:
            self.root = y
        else:
            if x.parent.left == x:
                x.parent.left = y
            else:
                x.parent.right = y
        y.parent = x.parent
        x.parent = y
        x.left = y.right
        if x.left:
            x.left.parent = x
        y.right = x

        self.update_height(x)
        self.update_height(y)

    def left_rotation(self, node):
        x = node
        y = node.right

        if not x.parent:
            self.root = y
        else:
            if x.parent.left == x:
                x.parent.left = y
            else:
                x.parent.right = y
        y.parent = x.parent
        x.parent = y
        x.right = y.left
        if x.right:
            x.right.parent = x
        y.left = x

        self.update_height(x)
        self.update_height(y)

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
            self.rebalance(node.parent)
        elif node.left and node.right:
            self.check_root(node, node.right)
            node.right.parent = node.parent
            node.right.left = node.left
            node.left.parent = node.right
            self.rebalance(node.left)
        else:
            if node.right:
                node.right.parent = node.parent
                self.check_root(node, node.right)
                self.rebalance(node.right)
            else:
                node.left.parent = node.parent
                self.check_root(node, node.left)
                self.rebalance(node.left)

    def check_root(self, old_node, new_node):
        if old_node.parent:
            if old_node == old_node.parent.right:
                old_node.parent.right = new_node
            else:
                old_node.parent.left = new_node


def serialize(node):
    if not node:
        return 'None'
    if not node.left and not node.right:
        return '{} ({})'.format(str(node.value), str(node.rank))
    return '<{} ({}): <{}, {}>>'.format(node.value, node.rank, serialize(node.left), serialize(node.right))


def serialize_height(node):
    if not node:
        return 'None'
    if not node.left and not node.right:
        return '{} ({})'.format(str(node.value), str(node.height))
    return '<{} ({}): <{}, {}>>'.format(node.value, node.height, serialize_height(node.left), serialize_height(node.right))


t = Tree()
# t.insert(29)
# t.insert(26)
# t.insert(23)
# t.insert(30)
# t.insert(32)
# t.insert(36)
# print(serialize_height(t.root))

# t.insert(41)
# t.insert(20)
# t.insert(65)
# t.insert(11)
# t.insert(50)
# t.insert(29)
# t.insert(26)
# t.insert(23)
# t.insert(55)

t2 =Tree()
t2.insert(30)
t2.insert(17)
t2.insert(40)
t2.insert(14)
t2.insert(20)
t2.insert(42)
t2.insert(22)
t2.insert(24)
t2.insert(26)
t2.insert(44)
t2.insert(23)
t2.find(t2.root, 20)
print(serialize_height(t2.root))
t2.delete(22)
# t2.delete(24)
# t2.delete(40)
# t2.delete(17)
# t2.delete(30)
print(serialize_height(t2.root))


# t3 = Tree()
# t3.insert(2)
# print(serialize_height(t3.root))
# t3.delete(3)
# t3.delete(2)
# print(serialize_height(t3.root))

