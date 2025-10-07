ans = []
def dfs(start_index, path, [...additional_states]):
  if is_leaf(start_index):
    ans.append(path[:])
    return
  for edge in get_edges(start_index, [...additional_states]):
    if not is_valid(edge):
      continue
    path.append(edge)
    if additional_states:
      update(...additional_states)
    dfs(start_index + len(edge), path, [...additional_states])
    path.pop()
      
  
  
