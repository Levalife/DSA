'''

Brute force or Dynamic programming

https://leetcode.com/problems/maximum-subarray

https://www.youtube.com/watch?v=2MmGzdiKR9Y

[-2,1,-3,4,-1,2,1,-5,4]

Brute Force:
Check all combinations from the start of the array:

-2

-2 1

-2 1 -3

-2 1 -3 4
...
-2 1 -3 4 -1 2 1 -5 4

   1

   1 -3

   1 -3 4

   ....

              1 -5 4
                -5 4
                   4

Dynamic programming:
Identify maximum sum for all subarrays which end at defined element

-2 1 -3 4 -1 2 1 -5 4

for first point mux sum is -2

for second element max sum could be previous sum + element (-2 + 1 == -1) or element itself 1 --> max(-1, 1) = 1

for third element it could be previous sum + element(1 - 3 == -2) or element itself -3 --> max(-2, -3) = -2

for foutrh element it could be previous sum + element(-2 + 4 == 2) or element itself 4 --> max(2, 4) = 4

etc:

-2 1 -2 4 3 5 6 1 4 ->>> max sum is 6


'''


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_s = nums[0]
        for i in range(0, len(nums)):
            s = nums[i]
            max_s = max(max_s, s)
            for j in range(i + 1, len(nums)):
                s += nums[j]
                max_s = max(max_s, s)

        return max_s


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s = nums[0]
        max_s = nums[0]
        for i in range(1, len(nums)):
            s = max(s + nums[i], nums[i])

            if s > max_s:
                max_s = s
        return max_s