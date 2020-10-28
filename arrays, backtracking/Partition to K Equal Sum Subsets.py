'''

https://leetcode.com/problems/partition-to-k-equal-sum-subsets/

https://www.youtube.com/watch?v=qpgqhp_9d1s

Time Limit Exceeded for leetcode
TODO: return to problem and check Dynamic Programming or other approaches

'''


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        start_pointer = 0
        used = [False] * len(nums)

        if k == 0 or sum(nums) % k != 0 or max(nums) > sum(nums) / k:
            return False

        return self.helper(start_pointer, nums, k, used, 0, sum(nums) / k)

    def helper(self, start_pointer, nums, k, used, current_sum, target_sum):

        if k == 1:
            return True

        if current_sum == target_sum:
            if k - 1 == 1:
                return True
            return self.helper(0, nums, k - 1, used, 0, target_sum)

        # increases time for large inputs
        # if current_sum > target_sum:
        #    return False

        for i in range(start_pointer, len(nums)):
            if not used[i] and current_sum + nums[i] <= target_sum:
                # current_sum += nums[i]

                used[i] = True
                if self.helper(start_pointer + 1, nums, k, used, current_sum + 1, target_sum):
                    return True
                used[i] = False
                # current_sum -= nums[i]

        return False

