# -*- coding: utf-8 -*-
import queue


'''

To find shortest path - use BFS (with queque)
And save every node with its prev node in a hashmap 

'''

def createMaze0():
    maze = []
    maze.append(["#","#", "#", "#", "#", "O","#"])
    maze.append(["#"," ", " ", " ", "#", " ","#"])
    maze.append(["#"," ", "#", " ", "#", " ","#"])
    maze.append(["#","#", "#", "#", "#", "X","#"])

    return maze

def createMaze():
    maze = []
    maze.append(["#","#", "#", "#", "#", "O","#"])
    maze.append(["#"," ", " ", " ", "#", " ","#"])
    maze.append(["#"," ", "#", " ", "#", " ","#"])
    maze.append(["#"," ", "#", " ", " ", " ","#"])
    maze.append(["#"," ", "#", "#", "#", " ","#"])
    maze.append(["#"," ", " ", " ", "#", " ","#"])
    maze.append(["#","#", "#", "#", "#", "X","#"])

    return maze

def createMaze2():
    maze = []
    maze.append(["#","#", "#", "#", "#", "O", "#", "#", "#"])
    maze.append(["#"," ", " ", " ", " ", " ", " ", " ", "#"])
    maze.append(["#"," ", "#", "#", " ", "#", "#", " ", "#"])
    maze.append(["#"," ", "#", " ", " ", " ", "#", " ", "#"])
    maze.append(["#"," ", "#", " ", "#", " ", "#", " ", "#"])
    maze.append(["#"," ", "#", " ", "#", " ", "#", " ", "#"])
    maze.append(["#"," ", "#", " ", "#", " ", "#", "#", "#"])
    maze.append(["#"," ", " ", " ", " ", " ", " ", " ", "#"])
    maze.append(["#","#", "#", "#", "#", "#", "#", "X", "#"])

    return maze


def findExit(maze):
    path = []
    queue = []
    cell = [0, 5]
    seen = []
    paths = {}
    queue.append(cell)
    isEnd = False
    current = None
    while queue and not isEnd:
        current = queue.pop(0)
        isEnd = helper(maze, queue, current, seen, paths)


    while current:
        path.append(current)
        current = paths.get("{},{}".format(*current))

    return path[::-1]


def helper(maze, queue, cell, seen, paths):
    seen.append(cell)

    x, y = cell

    if x < 0 or x >= len(maze) or y < 0 or y >= len(maze[0]):
        return False

    if maze[x][y] == 'X':
        return True

    # UP
    point = [x - 1, y]
    if maze[point[0]][point[1]] != "#" and point not in seen:
        paths["{},{}".format(*point)] = cell
        queue.append(point)

    # RIGHT
    point = [x, y + 1]
    if maze[point[0]][point[1]] != "#" and point not in seen:
        paths["{},{}".format(*point)] = cell

        queue.append(point)

    # DOWN
    point = [x + 1, y]
    if maze[point[0]][point[1]] != "#" and point not in seen:
        paths["{},{}".format(*point)] = cell

        queue.append(point)

    # LEFT
    point = [x, y - 1]
    if maze[point[0]][point[1]] != "#" and point not in seen:
        paths["{},{}".format(*point)] = cell

        queue.append(point)

def find_exit2(maze):
    seen = []
    paths = {}
    queue = []
    cell = [0,5]
    queue.append(cell)
    current = None
    isEnd = False

    while queue and not isEnd:
        current = queue.pop(0)
        isEnd = helper2(maze, queue, current, seen, paths)

    path = []
    while current:
        path.append(current)
        current = paths.get("{},{}".format(*current))
    return path[::-1]


def helper2(maze, queue, cell, seen, paths):

    if maze[cell[0]][cell[1]] == "X":
        return True

    if cell[0] < 0 or cell[0] >= len(maze) or cell[1] < 0 or cell[1] >= len(maze[0]):
        return False

    seen.append(cell)
    dx = [-1, 1, 0, 0] # bottom / up
    dy = [0, 0, -1, 1] # left / right

    for i in range(len(dx)):
        x = dx[i] + cell[0]
        y = dy[i] + cell[1]

        if maze[x][y] != "#" and [x, y] not in seen:
            paths['{},{}'.format(x,y)] = cell

            queue.append([x, y])






maze = createMaze2()

print(findExit(maze))

print(find_exit2(maze))
