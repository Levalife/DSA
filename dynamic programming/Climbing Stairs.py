"""

Top Down (with memoization) and Bottom Up (split into subproblems) approach

https://leetcode.com/problems/climbing-stairs/

https://www.youtube.com/watch?v=NFJ3m9a1oJQ

"""


class Solution:
    memo = {}

    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 1

        if n == -1:
            return 0

        if self.memo.get(n):
            return self.memo[n]

        self.memo[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        return self.memo[n]


class Solution:

    def climbStairs(self, n: int) -> int:
        self.solutions = [0] * (n + 1)
        self.solutions[0] = self.solutions[1] = 1

        for i in range(2, n + 1):
            self.solutions[i] = self.solutions[i - 1] + self.solutions[i - 2]

        return self.solutions[-1]



