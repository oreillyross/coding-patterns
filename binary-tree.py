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

    
 # This is an exhaustive dfs solution on a binary tree.   
def all_tree_paths(root):
  
  if root is None:
    return []
  if root.left is None and root.right is None:
    return [[root.val]]
  
  paths = []
  left = all_tree_paths(root.left)
  for sub in left:
    paths.append([root.val, *sub])
  right = all_tree_paths(root.right)
  for sub in right:
    paths.append([root.val, *sub])
  return paths    
      
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
