class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
g = Node('g')
h = Node('h')

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g
e.right = h

#      a
#    /    \
#   b      c
#  / \      \
# d   e      f
#    / \
#    g  h


def lowest_common_ancestor(root, val1, val2):
    val1Path = path(root, val1)
    val2Path = path(root, val2)
    set2Path = set(val2Path)
    for val in val1Path:
        if val in set2Path:
            return val


def path(node, targetVal):
    if node is None:
        return None

    if node.val == targetVal:
        return [node.val]

    leftPath = path(node.left, targetVal)
    if leftPath is not None:
        leftPath.append(node.val)
        return leftPath

    rightPath = path(node.right, targetVal)
    if rightPath is not None:
        rightPath.append(node.val)
        return rightPath
