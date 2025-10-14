from collections import deque

def bfs(root):
  queue = deque([root])
  visited = set([root])
  while len(queue) > 0:
    node = queue.popleft()
    for neighbour in get_neighbours(node):
      if neighbour in visited:
        continue
      queue.append(neighbour)
      visited.add(neighbour)

      
  
  
