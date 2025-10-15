def dfs(root, visited):
  for neighbour in get_neighbours(root):
    if neighbour in visited:
      continue
    visited.add(neighbour)
    dfs(neighbour, visited)
