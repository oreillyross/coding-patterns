def dfs(start_index, [...additional_states]):
  if is_leaf_node(start_index):
    return 1
  ans = initial_value
  for edge in get_edges(start_index, [...additional_states]):
    if additional_states:
      update([...additional_states])
    ans = aggregate(ans, dfs(start_index + len(edge), [...additional_states]))
    if additional_states:
      revert([...additional_states])
                    
  return ans
