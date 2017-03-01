import heapq
import sys


class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex, edge):
        self.vertices[vertex] = edge

    def shortest_paths(self, source, destination):
        distances = {}
        unv_nodes = []
        prev_nodes = {}

        for vertex in self.vertices:
            if source == vertex:
                distances[vertex] = 0
                heapq.heappush(unv_nodes, [0, vertex])
            else:
                distances[vertex] = sys.maxsize
                heapq.heappush(unv_nodes, [sys.maxsize, vertex])

        while unv_nodes:
            near_node = heapq.heappop(unv_nodes)[1]

            if near_node == destination:
                path = []
                while near_node in prev_nodes:
                    path.append(near_node)
                    near_node = prev_nodes[near_node]
                return path

            if distances[near_node] == sys.maxsize:
                break

            for neighbour in self.vertices[near_node]:
                d = distances[near_node] + self.vertices[near_node][neighbour]
                if d < distances[neighbour]:
                    distances[neighbour] = d
                    prev_nodes[neighbour] = near_node

                    for node in unv_nodes:
                        if neighbour == node[1]:
                            node[0] = d
                            break

                    heapq.heapify(unv_nodes)


g = Graph()
g.add_vertex('A', {'B': 7, 'C': 8})
g.add_vertex('B', {'A': 7, 'F': 2})
g.add_vertex('C', {'A': 8, 'F': 6, 'G': 4})
g.add_vertex('D', {'F': 8})
g.add_vertex('E', {'H': 1})
g.add_vertex('F', {'B': 2, 'C': 6, 'D': 8, 'G': 9, 'H': 3})
g.add_vertex('G', {'C': 4, 'F': 9})
g.add_vertex('H', {'E': 1, 'F': 3})
print(g.shortest_paths('A', 'E'))
