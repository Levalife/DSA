# -*- coding: utf-8 -*-

# https://www.youtube.com/watch?v=wGbuCyNpxIg&ab_channel=BackToBackSWE

'''

Question: Write a program which returns all distinct nonattacking placements of n queens on an nxn chessboard, where n
is an input to the program.

A nonattacking placement of queens is one in which no two queens are in the same row, column, or diagonal.

We will use backtracking to solve this problem.

This can be one of the most confusing topics that you have to learn, expecially if you have shaky foundations in
thinking recursively and calculating harder complexities.

Other Well Know Backtracking Problems:
-) Generate The Powerset of An Array (Subsets)
-) Generate All Permutations of A String

Backtracking/Recursion is about following a path to a base case...our target...our answer. If a certain path ends up
not meeting our constraints we will backtrack to an earlier state and try something else from there.

The 3 Keys To Backtracking Problems:

Our Choice

-) What choice are we making at each call of the function
-) RECURSION REPRESENTS A DECISION.
-) RECURSION REPRESENTS A CHOICE & its associated state
-) Each function call represents a state. From that state decisions can be made.

Our Constraints

-) What tells us to stop following a certain path that we are searching on?
-) Have we exhausted all possibilities?

Our Goal

-) What is our target?
-) What are we trying to find?
-) These will craft our base cases.

Example: You lost your keys. Where do you go? The most recent place you were. Then the most recent place from there.
And so on. Then you go to somewhere else...eventually you find your keys or give up the search.

So for this problem:
Our Choice - Where to place a queen
Our Constraints - The placement must non-attacking
Our Goal - Place n-queens on the chess board

'''


def NQueen(n):
    result = []
    nQueenHelper(n, 0, [], result)
    return result


def isValidPlacement(col_placement):
    '''

    :param col_placement: list
    :return: boolean

    Вспомогательная функция, принимает массив, каждый элемент которого является номером столбца или, другими словами,
    позицией Королевы в строке. А каждый индекс массива соответствует номеру строки. Например, массив:

    [1, 3, 0, 2] соответствует расположению Королев на доске:

    0 строка 1 столбец      | 0 * 0 0 |
    1 строка 3 столбец      | 0 0 0 * |
    2 строка 0 столбец      | * 0 0 0 |
    3 строка 2 столбец      | 0 0 * 0 |

    Все строки в цикле сравниваем с последней строкой:

    col_diff = abs(col_placement[i] - col_placement[last_row]) - находим разницу между номерами столбцев
    row_diff = abs(i - last_row) - находим разницу между номерами строк

    Если col_diff == 0 - значит королевы находятся в одном столбце (то есть находятся на линии огна)
    Если col_diff == row_diff значит разница столбцов и разница строк равно, то есть Королевы находятся на диагонали (также на линии огня)

        col_placement = [1, 3, 1]

        | 0 * 0 0 |     i = 0, last_row = 2
        | 0 0 0 * |     col_diff = | col_placement[0] - col_placement[2] | = | 1 - 1 | = 0
        | 0 * 0 0 |     col_diff == 0 - - элементы в первой и последней строке находятся на вертикальной линии огня

        col_placement = [1, 3, 3]

        | 0 * 0 0 |     i = 0, last_row = 2
        | 0 0 0 * |     col_diff = | col_placement[0] - col_placement[2] | =  | 1 - 3 | = 2
        | 0 0 0 * |     row_diff = | 0 - 2 | = 2
                        2 == 2 - элементы в первой и последней строке находятся на диагональной линии огня


    '''

    last_row = len(col_placement) - 1

    for i in range(last_row):
        col_diff = abs(col_placement[i] - col_placement[last_row])
        row_diff = abs(i - last_row)
        # if queens located in the same column or in diagonal cells then its wrong location
        if col_diff == 0 or col_diff == row_diff:
            return False
    return True


def nQueenHelper(n, row, col_placement, result):

    '''

    :param n: int
    :param row: int
    :param col_placement: lidt
    :param result: list
    :return: list

    if we reached end of the "board" - append to the result copy of the given columns placement (use copy because we
    will delete elements from the list during backtracking)

    else:

    in cycle try every possible queen position in given row one by one
        if given position is valid (isn't located at the attacking placement):
            call function in recursive way with the next row, checking every possible location in the next row

        Regardless of placement characteristics (attacking or nonattacking) delete it from list and try next one in
        the cycle to find every possible arrangement.

    '''

    if n == row:
        result.append(col_placement.copy())
    else:
        for i in range(n):
            col_placement.append(i)

            if isValidPlacement(col_placement):
                nQueenHelper(n, row+1, col_placement, result)

            col_placement.pop()


total = NQueen(4)
print(total)


total = NQueen(5)
print(total)