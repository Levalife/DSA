'''

https://leetcode.com/problems/coin-change-2/

https://www.youtube.com/watch?v=DJ4a7cmjZY0

amount = 5, coins = [1, 2, 5]

Subproblems:

coins        0   1   2   3   4   5 (amount)
[]           1   0   0   0   0   0                  if coins[i] <= amouns:
[1]          1   1   1   1   1   1                      sub[i][j] = sub[i - 1][j] + sub[i][j - coins[i]
[1, 2]       1   1   2   2   3   3                  else:
[1, 2, 5]    1   1   2   2   3   4                      sub[i][j] = sub[i - 1][j] # take upper row without using
             ^                                                                      coins[i]
             |
        (one way -
        do nothing)
'''


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        subproblems = []
        for i in range(len(coins) + 1):
            subproblems.append([0] * (amount + 1))

        for i in range(len(coins) + 1):
            subproblems[i][0] = 1

        for i in range(1, len(coins) + 1):
            for j in range(1, amount + 1):
                if coins[i - 1] <= amount:
                    subproblems[i][j] = subproblems[i - 1][j] + subproblems[i][j - coins[i - 1]]
                else:
                    subproblems[i][j] = subproblems[i - 1][j]
        return subproblems[-1][-1]