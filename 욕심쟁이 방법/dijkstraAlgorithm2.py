import numpy as np


# class Vertex:
#     def __init__(self, vertex):
#         self.name = vertex
#         self.neighbors = []
#
#     def add_neighbor(self, neighbor):
#         if isinstance(neighbor, Vertex):
#             if neighbor.name not in self.neighbors:
#                 self.neighbors.append(neighbor.name)
#                 neighbor.neighbors.append(self.name)
#                 self.neighbors = sorted(self.neighbors)
#                 neighbor.neighbors = sorted(neighbor.neighbors)
#         else:
#             return False
#
#     def add_neighbors(self, neighbors):
#         for neighbor in neighbors:
#             self.add_neighbor(neighbor)
#
#     def __repr__(self):
#         return str(self.neighbors)
#
#
# class Graph:
#     def __init__(self):
#         self.vertices = {}
#
#     def add_vertex(self, vertex):
#         if isinstance(vertex, Vertex):
#             self.vertices[vertex.name] = vertex.neighbors
#
#     def add_vertices(self, vertices):
#         for vertex in vertices:
#             if isinstance(vertex, Vertex):
#                 self.vertices[vertex.name] = vertex.neighbors
#
#     def add_edge(self, vertex_from, vertex_to):
#         if isinstance(vertex_from, Vertex) and isinstance(vertex_to, Vertex):
#             vertex_from.add_neighbor(vertex_to)
#             if isinstance(vertex_from, Vertex) and isinstance(vertex_to, Vertex):
#                 self.vertices[vertex_from.name] = vertex_from.neighbors
#                 self.vertices[vertex_to.name] = vertex_to.neighbors
#
#     def add_edges(self, edges):
#         for edge in edges:
#             self.add_edge(edge[0], edge[1])
#
#     def adjacencyList(self):
#         if len(self.vertices) >= 1:
#             return [str(key) + ":" + str(self.vertices[key]) for key in self.vertices.keys()]
#         else:
#             return dict()
#
#     def adjacencyMatrix(self):
#         if len(self.vertices) >= 1:
#             self.vertex_names = sorted(self.vertices.keys())
#             self.vertex_indices = dict(zip(self.vertex_names, range(len(self.vertex_names))))
#             self.adjacency_matrix = np.zeros(shape=(len(self.vertices), len(self.vertices)))
#             for i in range(len(self.vertex_names)):
#                 for j in range(i, len(self.vertices)):
#                     for el in self.vertices[self.vertex_names[i]]:
#                         j = self.vertex_indices[el]
#                         self.adjacency_matrix[i, j] = 1  # distance
#             return self.adjacency_matrix
#         else:
#             return dict()
#
#
# def graph(g):
#     """ Function to print a graph as adjacency list and adjacency matrix. """
#     return str(g.adjacencyList()) + '\n' + '\n' + str(g.adjacencyMatrix())
#
#
# if __name__ == "__main__":
#     a = Vertex('a')
#     b = Vertex('b')
#     c = Vertex('c')
#     d = Vertex('d')
#     e = Vertex('e')
#     f = Vertex('f')
#     g = Vertex('g')
#     z = Vertex('z')
#     a.add_neighbors([b,c])
#     b.add_neighbors([a,c,d])
#     c.add_neighbors([a,b,d,e])
#     d.add_neighbors([b,c,e,f])
#     e.add_neighbors([c,d,g])
#     f.add_neighbors([d,g,z])
#     g.add_neighbors([e,f,z])
#     z.add_neighbors([f,g])
#
#     print(a)

from collections import defaultdict


class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}

    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.distances[(from_node, to_node)] = distance
        self.distances[(to_node, from_node)] = distance


from collections import defaultdict
import heapq


def dijkstra_heapq(graph, initial, target):
    visited = {initial: 0}
    h = [(0, initial)]
    path = {}
    nodes = set(graph.nodes)

    while nodes and h:
        current_weight, min_node = heapq.heappop(h)
        try:
            while min_node not in nodes:
                current_weight, min_node = heapq.heappop(h)
        except IndexError:
            break

        if min_node == target:
            return visited, path

        nodes.remove(min_node)

        for v in graph.edges[min_node]:
            weight = current_weight + graph.distances[min_node, v]
            if v not in visited or weight < visited[v]:
                visited[v] = weight
                heapq.heappush(h, (weight, v))
                path[v] = min_node

    return visited, path


def dijkstra(graph, start):
    visited = {start: 0}
    path = {}
    nodes = set(graph.nodes)

    while nodes:
        min_node = None
        for node in nodes:
            if node in visited:
                if min_node is None:
                    min_node = node
                elif visited[node] < visited[min_node]:
                    min_node = node

        if min_node is None:
            break

        nodes.remove(min_node)
        current_weight = visited[min_node]

        for v in graph.edges[min_node]:
            weight = current_weight + graph.distances[(min_node, v)]
            if v not in visited or weight < visited[v]:
                visited[v] = weight
                path[v] = min_node

    return visited, path


if __name__ == "__main__":
    g = Graph()
    #     a = Vertex('a')
    #     b = Vertex('b')
    #     c = Vertex('c')
    #     d = Vertex('d')
    #     e = Vertex('e')
    #     f = Vertex('f')
    #     g = Vertex('g')
    #     z = Vertex('z')
    #     a.add_neighbors([b,c])
    #     b.add_neighbors([a,c,d])
    #     c.add_neighbors([a,b,d,e])
    #     d.add_neighbors([b,c,e,f])
    #     e.add_neighbors([c,d,g])
    #     f.add_neighbors([d,g,z])
    #     g.add_neighbors([e,f,z])
    #     z.add_neighbors([f,g])
    g.add_node("a")
    g.add_node("b")
    g.add_node("c")
    g.add_node("d")
    g.add_node("e")
    g.add_node("f")
    g.add_node("g")
    g.add_node("z")

    g.add_edge("a", "b", 4)
    g.add_edge("a", "c", 3)
    g.add_edge("b", "c", 2)
    g.add_edge("b", "d", 5)
    g.add_edge("c", "d", 3)
    g.add_edge("c", "e", 6)
    g.add_edge("d", "e", 1)
    g.add_edge("d", "f", 5)
    g.add_edge("e", "g", 5)
    g.add_edge("f", "g", 2)
    g.add_edge("f", "z", 7)
    g.add_edge("g", "z", 4)
    visited, path = dijkstra(g, "a")
    visited, path = dijkstra_heapq(g, "a", "z")
    print(visited,
          path)
    start = "a"
    end = "z"
    while end != start:
        print(end)
        end = path[end]
    print(end)
    """ 5, 6, 3 , 1 """