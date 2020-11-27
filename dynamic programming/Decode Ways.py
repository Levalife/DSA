'''

TOP TO BOTTOM DYNAMIC PROGRAMMING WITH MEMOIZATION

https://www.youtube.com/watch?v=YcJTyrG3bZs

https://leetcode.com/problems/decode-ways/

Memorize number of combinations for each index

'''


class Solution:
    def numDecodings(self, s: str) -> int:

        if s == "0":
            return 0

        self.memo = dict()

        return self.helper(s, 0)

    def helper(self, s, startIndex):

        # if we reached the end of the string - we got 1 combination ( 1 or 2 symbol number)
        if startIndex == len(s):
            return 1

        # check if index with number of all possible combinations is already exists
        if startIndex in self.memo:
            return self.memo[startIndex]

        # if not - calculate possible combinations for current starting index for numbers with 1 and 2 symbold (<=26)
        output = 0
        if startIndex + 1 <= len(s):
            if not s[startIndex: startIndex + 1].startswith("0") and int(s[startIndex: startIndex + 1]) <= 26:
                output += self.helper(s, startIndex + 1)

        if startIndex + 2 <= len(s):
            if not s[startIndex: startIndex + 2].startswith("0") and int(s[startIndex: startIndex + 2]) <= 26:
                output += self.helper(s, startIndex + 2)

        # save to map
        self.memo[startIndex] = output

        # return current number of compinations
        return output





