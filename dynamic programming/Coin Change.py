'''

https://leetcode.com/problems/coin-change/

https://www.youtube.com/watch?v=jgiZlGzXMBw

Problem can be solved both top-bottom (recursion + memoization) and bottom-top (from subproblems to result) ways.

Bottom-Top approach:

create result array which will contain minimum possible coin change for every amoun <= amount of change

for initial value take 0 for amount of 0 and (amount + 1) for others

  i =  0 1 2 3 4 5 6 7 8 9 10 11
       0 1 1 2 2 1 2 2 3 3  2  3

Top - Bottom approach:

from the biggest coin start to branch all possible combination of change. Memorize solution for future reuse

                                    11
                        / (5)                      | (2)      \ (1)
                        6                           9           10
            /(5) |(2)               \(1)
          1      4                  5
        /(1)    /(2)\(1)        /(5) |(2) \(1)
      0        2    3           0     3    4           memo: {1: 1}
            /(2)\(1) /(2)\(1)
           0    X   X     X                            memo: {1: 1, 2:1}
                  (memo 1)                             memo: {1: 1, 2:1, 4:2, 3: 2, 6: 2, 11: 3}
                  ........
'''

# BOTTOM - TOP

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        result = [amount + 1] * (amount + 1)
        result[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i:
                    left = i - coin
                    result[i] = min(result[left] + 1, result[i])
        return result[-1] if result[-1] <= amount else -1


# TOP - BOTTOM

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        if amount == 0:
            return 0

        self.coins = coins
        self.amount = amount
        self.memo = dict()

        self.helper(self.amount)
        result = self.memo.get(self.amount, self.amount + 1)
        return result if result <= self.amount else -1

    def helper(self, amount_left):

        if amount_left == 0:
            return 0

        if self.memo.get(amount_left):
            return self.memo.get(amount_left)

        output = []
        for i in range(len(self.coins) - 1, -1, -1):
            if amount_left >= self.coins[i]:

                num = self.helper(amount_left - self.coins[i])
                if num or num == 0:
                    output.append(num)
        if output:
            min_output = min(output)

            self.memo[amount_left] = min(min_output + 1, self.memo.get(amount_left, self.amount + 1))
            return min_output + 1
        return self.amount + 1
