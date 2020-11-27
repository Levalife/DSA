"""

BACKTRACKING

https://leetcode.com/problems/letter-combinations-of-a-phone-number/

https://www.youtube.com/watch?v=a-sMgZ7HGW0

"""

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        self.numbers = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        mnemonics = []
        current_mnemonic = []
        if digits:
            self.helper(digits, 0, current_mnemonic, mnemonics)
        return mnemonics

    def helper(self, digits, digit_num, current_mnemonic, mnemonics):

        if digit_num == len(digits):
            mnemonics.append("".join(current_mnemonic))
        else:
            digit = digits[digit_num]
            for i in self.numbers[int(digit)]:
                current_mnemonic.append(i)
                self.helper(digits, digit_num + 1, current_mnemonic, mnemonics)
                current_mnemonic.pop()

