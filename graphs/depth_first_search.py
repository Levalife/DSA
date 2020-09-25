# -*- coding: utf-8 -*-
import queue

stack = []

def dfs_visit(vertex, graph):
    for v in graph[vertex]:
        if v in stack:
            print('{} -> {} is a back edge'.format(vertex, v))
        if v not in parent:
            parent[v] = vertex
            stack.append(v)
            dfs_visit(v, graph)
            stack.pop()


def dfs(V, vertex, graph):

    for v in V:
        if v not in parent:
            parent[v] = None
            stack.append(v)
            dfs_visit(v, graph)
            stack.pop()
    print(parent)

if __name__ == '__main__':
    graph = {
        'a': ['b', 'd'],
        'b': ['c'],
        'd': ['b'],
        'c': ['d'],
        'e': ['c', 'f'],
        'f': ['f']
    }
    vertex = 'a'
    # parent = {vertex: None}
    # dfs_visit(vertex, graph)
    # print(parent)
    # v = 'd'
    # print(v, end="")
    # while parent[v]:
    #     print('->', parent[v], end='')
    #     v = parent[v]

    V = ('a', 'b', 'c', 'd', 'e', 'f')
    parent = {}
    dfs(V, vertex, graph)
