mgraph = {'A': ['B', 'C'],
          'B': ['A', 'D', 'E'],
          'C': ['A', 'F'],
          'D': ['B'],
          'E': ['B', 'F'],
          'F': ['C', 'E']}


# go to children and then siblings
def dfs_traversal_rec(graph, start, visited=None):
    if visited is None:
        visited = []
    for vertex in graph[start]:
        if vertex not in visited:
            visited.append(vertex)
            dfs_traversal_rec(graph, vertex, visited)

    return visited


def dfs_paths_stack(graph, start, end):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for node in set(graph[vertex]) - set(path):
            if node == end:
                yield path + [node]
            else:
                stack.append((node, path + [node]))


def dfs_paths_recursive(graph, start, end, path=None):
    if path is None:
        path = [start]
    if start == end:
        yield path
    for node in graph[start]:
        if node not in path:
            yield from dfs_paths_recursive(graph, node, end, path + [node])









