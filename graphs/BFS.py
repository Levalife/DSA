# -*- coding: utf-8 -*-

# Queue (first in first out) will make it BFS
# Stack (lirst in first out) will make it DFS

'''

Breadth First Search

Imple,enting iteretivly with a queue

FIFO

USES: check if a path exists between the nodes, finding levels away of something

Goes wide


Searching relationships not just graphs: string distance, a tree etc
'''


def bfs(graph, vertex):
    queue = []
    seen = set()
    queue.append(vertex)
    while queue:
        current = queue.pop(0)
        if current not in seen:
            seen.add(current)
            print(current)

            for vertex in graph.get(current):
                if vertex not in seen:
                    queue.append(vertex)


graph = {
        'a': ['b', 'd'],
        'b': ['c', 'a', 'd'],
        'd': ['b', 'a', 'c'],
        'c': ['d', 'e', 'b'],
        'e': ['c', 'f'],
        'f': ['f', 'e']
    }

bfs(graph, 'a')