'''


BACKTRACKING

https://leetcode.com/problems/sudoku-solver/
https://www.youtube.com/watch?v=JzONv5kaPJM


'''


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.helper(board, 0, 0)
        
        
    def helper(self, board, i, j):

        # if we got to the last cell of the board - we have found the solution and can stop searching
        if i == len(board) and j == 0:
            return True

        if board[i][j] == ".":
            # is cell is empty - try all numbers from 1 to 9
            k = 1
            while k < 10:
                # if number satisfy all sudoku conditions - try next cell (next in row or next row first column if
                # current cell is last in the row
                if self.is_valid(board, i, j, str(k)):
                    board[i][j] = str(k)  # make choise
                    if j == len(board) - 1:
                        if self.helper(board, i + 1, 0):
                            return True
                    else:
                        if self.helper(board, i, j + 1):
                            return True
                    board[i][j] = "."  # unchoice previous choice
                k += 1
        else:
            # if cell is not empty - skip square
            if j == len(board) - 1:
                if self.helper(board, i + 1, 0):
                    return True
            else:
                if self.helper(board, i, j + 1):
                    return True
                    

        
    def is_valid(self, board, i, j, num):
        
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