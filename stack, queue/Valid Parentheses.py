'''

https://www.youtube.com/watch?v=CCyEXcNamC4

https://leetcode.com/problems/valid-parentheses/

'''


class Solution:
    def isValid(self, s: str) -> bool:
        left_stack = []
        for el in s:
            if el in ("{", "[", "("):
                left_stack.append(el)
            else:
                if not left_stack:
                    # "unbalanced" string with rights parentheses like "())"
                    return False
                else:
                    peek = left_stack.pop()
                    if el == ")" and peek != "(" or el == "}" and peek != "{" or el == "]" and peek != "[":
                        # if not balanced return False
                        return False

        # if stack is empty return True, if not - unbalanced like "(()"
        return not left_stack
