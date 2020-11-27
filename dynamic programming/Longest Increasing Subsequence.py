'''

https://leetcode.com/problems/longest-increasing-subsequence/
https://www.youtube.com/watch?v=fV-TF4OvZpk

Divide problem into subproblems.
Create array len(nums) filled with 1 (because every number is increasing subsequence of length 1
Create two pointers: i = 0, j = i + 1
Go through array with pointer j. Compare nums[j] with every nums[i] while i < j.

    if result[i] + 1 > result[j] (sequence is remaining) ---> result[j] = result[i] + 1
                 i j
            -1 3 4 5 2 2 2 2
result       1 2 3 3

             i       j
            -1 3 4 5 2 2 2 2
result       1 2 3 4 2 2 2 2


'''


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        if not nums:
            return 0

        result = [1] * len(nums)

        current_i = i = 0
        j = i + 1

        while i < len(nums) and j < len(nums):
            while i < j:
                if nums[j] > nums[i]:
                    if result[i] + 1 > result[j]:
                        result[j] = result[i] + 1
                i += 1
            i = current_i
            j += 1

        return max(result)


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        if not nums:
            return 0

        result = [1] * len(nums)

        i = 0
        j = i + 1

        while i < len(nums) and j < len(nums):

            if nums[j] > nums[i]:
                if result[i] + 1 > result[j]:
                    result[j] = result[i] + 1
            j += 1

            if j >= len(nums):
                i += 1
                j = i + 1

        return max(result)