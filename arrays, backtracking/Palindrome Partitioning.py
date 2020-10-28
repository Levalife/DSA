'''

BACKTRACKING

https://leetcode.com/problems/palindrome-partitioning/

https://www.youtube.com/watch?v=4ykBXGbonlA

s = aab

find __all__ (backtracking) possible palindrome partitioning of s:

a a b - all palindromes

a ab - not all palindromes

aa b - all palindromes

aab - not palindrome


s = aaab
First outer cycle i == 0
a a a b - palindromes

a a ab

a aa b - palindromes

a aab

First outer cycle i == 1
aa a b - palindromes

aa ab

First outer cycle i == 2
aaa b - palindromes

First outer cycle i == 3
aaab


'''


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        partitions = []
        result = []
        self.helper(s, 0, partitions, result)
        return result

    def helper(self, s, pointer, partitions, result):

        # Base case, we reached the end of the string so all possible palindromes are added to partition
        if pointer == len(s):
            result.append(partitions.copy())
            return True

        for i in range(pointer, len(s)):
            # Check constrains
            if self.is_palindrom(s, pointer, i):
                # Choice of the next element to explore
                partitions.append(s[pointer: i + 1])

                # Exploration
                self.helper(s, i + 1, partitions, result)

                # Undo choice
                partitions.pop()

    def is_palindrom(self, s, pointer, i):
        return s[pointer: i + 1] == s[pointer:i + 1][::-1]
