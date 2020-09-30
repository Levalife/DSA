# -*- coding: utf-8 -*-

'''

Depth First Search

Uses a stack. Either our own or the call stack via recursion

LIFO

USES: Backtracking, complete search, exhausting possible paths

Goes deep


Searching relationships not just graphs: string distance, a tree etc

'''


def dfs(graph, vertex):
    stack = []
    seen = set()
    stack.append(vertex)
    while stack:
        current = stack.pop()
        if current not in seen:
            seen.add(current)
            print(current)

            for vertex in graph.get(current):
                if vertex not in seen:
                    stack.append(vertex)


graph = {
        'a': ['b', 'd'],
        'b': ['c', 'a', 'd'],
        'd': ['b', 'a', 'c'],
        'c': ['d', 'e', 'b'],
        'e': ['c', 'f'],
        'f': ['f', 'e']
    }

dfs(graph, 'a')