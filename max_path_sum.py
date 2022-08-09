def max_path_sum(grid):
  return _max_path_sum(grid, 0, 0, {})
  
def _max_path_sum(grid, r, c, memo):
  
  pos = (r,c)
  if pos in memo:
    return memo[pos]
    
  if r == len(grid) or c == len(grid[0]):
    return float("-inf")
  
  if r == len(grid) -  1 and len(grid[0]) - 1:
    return grid[r][c]
  
  bottom = _max_path_sum(grid, r + 1, c, memo)
  right = _max_path_sum(grid, r, c + 1, memo)
  
  memo[pos] = grid[r][c] + max(bottom, right)
  return memo[pos]
    
  
grid = [
  [1, 3, 12],
  [5, 1, 1],
  [3, 6, 1],
]
print(max_path_sum(grid)) # -> 18
