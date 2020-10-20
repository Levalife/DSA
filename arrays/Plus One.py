'''

https://www.youtube.com/watch?v=vA0t42qwKO0

add 1 from the end of the array
if element > 9 (==10) -> set element to 0 and carry 1 to the next element

'''


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        digits[-1] += 1
        if digits[-1] > 9:
            digits[-1] = 0
            carry = 1

        i = len(digits) - 2
        while carry != 0 and i >= 0:
            digits[i] += 1

            if digits[i] > 9:
                digits[i] = 0
                i -= 1
            else:
                carry = 0

        if carry != 0:
            digits[0] = 0
            digits.insert(0, 1)

        return digits
