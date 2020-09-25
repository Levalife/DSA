# -*- coding: utf-8 -*-


def bfs(vertex, graph):
    level = {vertex: 0}
    parent = {vertex: None}
    i = 1
    frontier = [vertex]
    while frontier:
        next = []
        for u in frontier:
            for v in graph[u]:
                if v not in level:
                    level[v] = i
                    parent[v] = u
                    next.append(v)
        i += 1
        frontier = next

    print(level)
    print(parent)
    vertex = 'V'
    print(vertex, end='')
    while parent[vertex]:
        print(' -> ', parent[vertex], end='')
        vertex = parent[vertex]

if __name__ == '__main__':
    G = {'S': ['A', 'X'],
         'A': ['S', 'Z'],
         'Z': ['A'],
         'X': ['S', 'D', 'C'],
         'D': ['X', 'C', 'F'],
         'C': ['X', 'D', 'F', 'V'],
         'F': ['D', 'C', 'V'],
         'V': ['C', 'F']
    }

    bfs('S', G)
