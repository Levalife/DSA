
def solveSudoku(board):
    """
    Do not return anything, modify board in-place instead.
    """
    helper(board, 0, 0)

def helper(board, i, j):

    if i == len(board) and j == 0:
        print("success")
        return True

    ф

def is_valid(board, i, j, num):

    if num in board[i]:
        return False

    for k in range(len(board)):
        if num == board[k][j]:
            return False

    mod_i = i % 3
    mod_j = j % 3
    for sub_i in range(i - mod_i, i - mod_i + 3):
        for sub_j in range(j - mod_j, j - mod_j + 3):
            if board[sub_i][sub_j] == num:
                return False

    return True

b = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

solveSudoku(b)
print(b)