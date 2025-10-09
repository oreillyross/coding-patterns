from collections import deque

def bfs_queue(root):
  queue = deque([root])
  while len(queue) > 0:
    node = queue.popleft()
    for child in node.children:
      if is_goal(child):
        return FOUND(child) # early return, condition found/met
      queue.append(child) # add all children to queue
    return NOT_FOUND # bfs complete condition not met 
