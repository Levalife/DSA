# -*- coding: utf-8 -*-
'''

https://www.youtube.com/watch?v=ZQQoHr-2stA

https://leetcode.com/problems/reverse-integer/



'''


class Solution:

    def reverse(self, x: int) -> int:
        result = 0
        remaining = abs(x)
        while remaining:
            result *= 10
            result += remaining % 10
            remaining //= 10

        result = result if x > 0 else result * -1

        if result < -2**31 or result > 2**31 - 1:
            return 0

        return result