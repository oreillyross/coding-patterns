import abc

import numpy as np

class Graph(abc.ABC):

    def __init__(self, num_vertices, directed=False) -> None:
        self.num_vertices = num_vertices
        self.directed = directed
    
    @abc.abstractmethod
    def add_edge(self, v1, v2, weight):
        pass 
    
    @abc.abstractmethod
    def remove_edge(self, v1, v2, weight):
        pass 
    
    @abc.abstractmethod
    def get_adjacent(self, v):
        pass 
    
    @abc.abstractmethod
    def is_adjacent(self, v1, v2):
        pass
    
    @abc.abstractmethod
    def get_indegree(self, v):
        pass 
    
    @abc.abstractmethod
    def get_edge_weight(self, v1, v2):
        pass

    @abc.abstractmethod
    def show(self):
        pass

class Vertex:
    def __init__(self, id) -> None:
        self.id = id
        self.adjacency_set = set()

    def add_edge(self, v):
        if self.id == v:
            raise ValueError("The vertex %d cannot be adjacent to itself" % v)
        self.adjacency_set.add(v)
    
    def remove_edge(self, v):
        if self.id == v:
            raise ValueError("The vertex %d cannot be adjacent to itself" % v)
        self.adjacency_set.remove(v)
    
    def get_adjacent_vertices(self):
        return sorted(self.adjacency_set)
    
    def is_adjacent(self, v):
        return v in self.adjacency_set
    
class AdjacencySetGraph(Graph):

    def __init__(self, num_vertices, directed=False) -> None:
        super().__init__(num_vertices, directed)

        self.vertex_list = []
        for i in range(num_vertices):
            v = Vertex(i)
            self.vertex_list.append(v)
    
    
        