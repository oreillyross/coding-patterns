from collections import deque

def find_indegree(graph):
  indegree = {node: 0 for node in graph}
  for node in graph:
    for neighbour in graph[node]:
      indegree[neighbour] += 1
  return indegree

def topological_sort(graph):
  res = []
  q = deque()
  indegree = find_indegree(graph)
  for node in indegree:
    if indegree[node] == 0:
      q.append(node)
  while q:
    node = q.popleft()
    res.append(node)
    for neighbour in graph[node]:
      indegree[neighbour] -= 1
      if indegree[neighbour] == 0:
        q.append(neighbour)
    return res if len(res) == len(graph) else None
  
