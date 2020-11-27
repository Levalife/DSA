'''

Design and stack

https://leetcode.com/problems/min-stack/

https://www.youtube.com/watch?v=nGwn8_-6e7w

'''


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = []

    def push(self, x: int) -> None:
        self.stack.append(x)

        if not self.min or x < self.min[-1][0]:
            self.min.append([x, 1])
        elif x == self.min[-1][0]:
            self.min[-1][1] = self.min[-1][1] + 1
        print(x, self.min)

    def pop(self) -> None:
        value = self.stack.pop()

        if value == self.min[-1][0]:
            if self.min[-1][1] > 1:
                self.min[-1][1] = self.min[-1][1] - 1
            else:
                self.min.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min[-1][0]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()