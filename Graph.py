from Colors import Colors
from collections import deque

class Graph:
  def __init__(self):
    self.vertices = []
    self.adj_list = {}
  
  def add_vertice(self, v):
    if not v in self.vertices:
      self.vertices.append(v)
      self.adj_list[v] = []
  
  def add_edge(self, v, w):
    if v not in self.adj_list: self.add_vertice(v)
    if w not in self.adj_list: self.add_vertice(w)
    self.adj_list[v].append(w)
    self.adj_list[w].append(v)
    
  def remove_vertice(self, v):
    if not v in self.vertices: return
    self.vertices.remove(v)
    self.adj_list.pop(v)
    for i in self.vertices:
      if v in self.adj_list[i]:
        self.adj_list[i].remove(v)
        
  def remove_edge(self, v, w):
    if not (w in self.adj_list[v] or v in self.adj_list[w]): return
    if w in self.adj_list[v]: self.adj_list[v].remove(w)
    if v in self.adj_list[w]: self.adj_list[w].remove(v)
  
  def get_vertices(self):
    return self.vertices
  
  def get_adj_list(self):
    return self.adj_list
  
  def getDegree(self, v):
    if not v in self.vertices: return -1
    return len(self.adj_list[v])

  def get_min_degree(self):
    if not self.vertices: return None, None
    min_degree = float('inf')
    min_vertices = []
    for vertex in self.vertices:
      degree = self.getDegree(vertex)
      if degree < min_degree:
        min_degree = degree
        min_vertices = [vertex]
      elif degree == min_degree:
        min_vertices.append(vertex)
    return min_vertices, min_degree

  def get_max_degree(self):
    if not self.vertices: return None, None
    max_degree = 0
    max_vertices = []
    for vertex in self.vertices:
      degree = self.getDegree(vertex)
      if degree > max_degree:
        max_degree = degree
        max_vertices = [vertex]
      elif degree == max_degree:
        max_vertices.append(vertex)
    return max_vertices, max_degree
    
  def num_edges(self):
    total_edges = 0
    for vertex in self.vertices:
      total_edges += self.getDegree(vertex) // 2
    return total_edges
    
  def num_vertices(self): return len(self.vertices)
  
  def components(self):
    components = 0
    visited = set()
    for vertex in self.vertices:
      if vertex not in visited:
        self._dfs(vertex, visited)
        components += 1
    return components
  
  def _dfs(self, start_vertex, visited):
    stack = [start_vertex]
    visited.add(start_vertex)

    while stack:
      current_vertex = stack.pop()
      for neighbor in self.adj_list[current_vertex]:
        if neighbor not in visited:
          stack.append(neighbor)
          visited.add(neighbor)