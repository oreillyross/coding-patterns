# def dft_iterative(graph, start):
#     stack = [start]            
#     while len(stack) > 0:
#         current = stack[-1]
#         print(current)
#         stack.pop()
#         for neighbor in graph[current]:
#             stack.append(neighbor)

# def dft_recursive(graph, current):
#     print(current)
#     for neighbor in graph[current]:
#         dft_recursive(graph, neighbor)

from collections import deque
def bft(graph, start):
   queue = deque([start]) 
   while len(queue) > 0:
      current = queue.popleft() 
      print(current)
      for neighbor in graph[current]:
          queue.append(neighbor)




graph = {
	"a": ["b", "c"],
	"b": ["d"],
	"c": ["e"],
	"d": ["f"],
	"e": [],
	"f": [],
	}


# dft_iterative(graph, "a")
# dft_recursive(graph, "a")
bft(graph, "a")