'''

BACKTRACKING

https://leetcode.com/problems/generate-parentheses/

https://www.youtube.com/watch?v=sz1qaKt0KGQ

We can place a "(" and recurse or we can place a ")" and recurse.

But we can't just do that placement, we need 2 critical pieces of information.

The amount of left parens left to place.
The amount of right parens left to place.

We have 2 critical rules at each placement step.

We can place a left parentheses if we have more than 0 left to place.

We can only place a right parentheses if there are left parentheses that we can match against.

We know this is the case when we have less left parentheses to place than right parentheses to place.

n = 3

                                left 3 right 3
                                    |
                                  2   3
                                   "("
                            /               \
                        /                      \
                     /                          \
                    1 3                         2 2
                    "(("                        "()"
                /          \                    /
             0  3          1  2               1 2
             "((("        "(()"               "()("
              \         /       \           /       \
             0 2      0  2      1  1       0 2      1 1
             "((()"  "(()("    "(())"     "()(("    "()()"
              \         \          /        \          /
              0 1       0 1      0 1       0 1       0 1
              "((())"   "(()()" "(())("   "()(()"   "()()("
               \        \          \        \           \
               0 0      0 0        0 0      0 0         0 0
               "((()))" "(()())"  "(())()"  "()(())"    "()()()"

'''


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        self.helper(n, n, "", result)
        return result

    def helper(self, left, right, current, result):
        if left == 0 and right == 0:
            result.append(current)
            return True

        if left > 0:
            self.helper(left - 1, right, current + "(", result)
        if left < right:
            self.helper(left, right - 1, current + ")", result)
        return False
