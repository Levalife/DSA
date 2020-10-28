'''

DYNAMIC PROGRAMMING

https://leetcode.com/problems/edit-distance/

https://www.youtube.com/watch?v=We3YDTzNXEk

       ' ' a b c d e f
    ' ' 0  1 2 3 4 5 6      if a == a, than no additional operations are needed and we can set diagonal value 0
    a   1  0 1 2 3 4 5      else: take minimal of possible operations (top, left and diagonal) and add one operation (replacing)
    z   2  1 1 2 3 4 5
    c   3  2 2 1 2 3 4
    e   4  3 3 2 2 2 3
    d   5  4 4 3 3 3 3

'''


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        word1 = "_" + word1
        word2 = "_" + word2

        T = [list(range(len(word1)))]

        for i in range(1, len(word2)):
            T.append([i] + [0] * (len(word1) - 1))

        for i in range(1, len(word2)):
            for j in range(1, len(word1)):
                if word2[i] == word1[j]:
                    T[i][j] = T[i - 1][j - 1]
                else:

                    T[i][j] = min(T[i - 1][j - 1], T[i - 1][j], T[i][j - 1]) + 1
        return T[-1][-1]
