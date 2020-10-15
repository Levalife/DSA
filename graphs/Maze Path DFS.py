# -*- coding: utf-8 -*-
import queue


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

    cell = [0, 5]
    seen = []
    helper(maze, cell, seen, path)
    return path[::-1]


def helper(maze, cell, seen, path):
    seen.append(cell)

    x, y = cell

    if x < 0 or x >= len(maze) or y < 0 or y >= len(maze[0]):
        return False

    if maze[x][y] == 'X':
        return True

    # UP
    point = [x - 1, y]
    if maze[point[0]][point[1]] != "#" and point not in seen:
        step = helper(maze, point, seen, path)

        if step:
            path.append(point)
            return True

    # RIGHT
    point = [x, y + 1]
    if maze[point[0]][point[1]] != "#" and point not in seen:
        step = helper(maze, point, seen, path)
        if step:
            path.append(point)
            return True


    # DOWN
    point = [x + 1, y]
    if maze[point[0]][point[1]] != "#" and point not in seen:
        step = helper(maze, point, seen, path)
        if step:
            path.append(point)
            return True

    #LEFT
    point = [x, y - 1]
    if maze[point[0]][point[1]] != "#" and point not in seen:
        step = helper(maze, point, seen, path)
        if step:
            path.append(point)
            return True

def find_exit2(maze):
    cell = [0, 5]
    seen = []
    path = []

    helper2(maze, cell, seen, path)
    return path[::-1]

def helper2(maze, cell, seen,path):
    seen.append(cell)

    if maze[cell[0]][cell[1]] == "X":
        return True

    if cell[0] < 0 or cell[1]< 0 or cell[0] >= len(maze) or cell[1] >= len(maze[0]):
        return False

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(len(dx)):

        x = cell[0] + dx[i]
        y = cell[1] + dy[i]

        if maze[x][y] != "#" and [x, y] not in seen:

            if helper2(maze, [x, y], seen, path):
                path.append([x, y])
                return True


maze = createMaze2()

print(findExit(maze))

# In second case get different path because it searches for the first path (not shortest) and we have different
# consequence of steps directions (bottom, up, left, right) instead of up, right, down, left.
print(find_exit2(maze))