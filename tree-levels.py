# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

from collections import deque

def tree_levels(root):
 # edge case for an empty tree
  if root is None:
    return []
 # initialize your levels to be returned
  levels = []
  # setup a queue, and initialize it with a tuple 
  # of the root node, and the level which is 0
  queue = deque([ ( root, 0 ) ])
  # condition to check if tree has been fully traversed
  while queue: 
    # pull out or destructure tuple 
    current, level = queue.popleft()
    # core logic, if the current length of levels is equal to current levels
    # then start a new level otherwise add to existing level 
    if len(levels) == level:
      levels.append([current.val])
    else:
      levels[level].append(current.val)
    
    #core bfs traversal ensure your tuple properly passed in with 
    # level being incremented
    if current.left is not None:
      queue.append((current.left, level + 1))
      
    if current.right is not None:
      queue.append((current.right, level + 1))
  
  return levels
