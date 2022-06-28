class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

from collections import deque

def bottom_right_value(root):
  queue = deque([root])
  while queue:
    node = queue.popleft()
    if node.left is not None:
      queue.append(node.left)
    if node.right is not None:
      queue.append(node.right)
    if len(queue) == 0:
      return node.val
      
      
a = Node(3)
b = Node(11)
c = Node(10)
d = Node(4)
e = Node(-2)
f = Node(1)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#       3
#    /    \
#   11     10
#  / \      \
# 4   -2     1

bottom_right_value(a) # -> 1
