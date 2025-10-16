num_rows, num_cols = len(grid), len(grid[0])

def get_neighbours(coord):
  row, col = coord
  delta_row = [-1, 0, 1, 0]
  delta_col = [0, 1, 0, -1]
  res = []
  for i in range(len(delta_row)):
    neighbour_row = row + delta_row[i]
    neighbour_col = col + delta_col[i]
    if 0 <= neighbour_row < num_rows and 0 <= neighbour_col < num_cols:
      res.append((neighbour_row, neighbour_col))
  return res

from collections import deque

def bfs(starting_node):
  queue = deque([starting_node])
  visited = set([starting_node])
  while len(queue) > 0:
    node = queue.popleft()
    for neighbour in get_neighbours(node):
      if neighbour in visited:
        continue
      # do something with node
      queue.append(neighbour)
      visited.add(neighbour)







  
