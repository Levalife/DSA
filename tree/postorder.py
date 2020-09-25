
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
        return str(self.value)

    def __unicode__(self):
        return str(self.value)

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

Postorder
left right node 

1 6 9 8 7 14 22 20 11 10

'''

def postorder_iter_mine(tree):
    current = tree.root
    temp = None
    stack = []
    while stack or current:
        if current:
            stack.append(current)
            current = current.left

        else:

            if not stack[-1].right:
                temp = stack.pop()
                print(temp.value)
            else:
                if stack[-1].right == temp:
                    temp = stack.pop()
                    print(temp.value)
                else:
                    current = stack[-1].right


def postorder_iter(tree):
    current = tree.root

    stack = []
    while stack or current:
        if current:
            stack.append(current)
            current = current.left

        else:
            temp = stack[-1].right
            if not temp:
                temp = stack.pop()
                print(temp.value)
                while stack and temp == stack[-1].right:
                    temp = stack.pop()
                    print(temp.value)
            else:

                current = temp

postorder_iter(tree)


def postorder_rec(node):

    if node.left:
        postorder_rec(node.left)

    if node.right:
        postorder_rec(node.right)

    print(node.value)

postorder_rec(tree.root)


def postorder_repeat(tree):
    stack = []
    current = tree.root
    temp = None
    while stack or current:
        if current:
            stack.append(current)
            current = current.left
        else:

            if not stack[-1].right or stack[-1].right == temp:
                temp = stack.pop()
                print(temp.value)
            else:
                current = stack[-1].right


print("repeat")
postorder_repeat(tree)


























