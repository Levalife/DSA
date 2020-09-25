# -*- coding: utf-8 -*-

def threeSumClosest(nums, target):
    nums.sort()
    result = nums[0] + nums[1] + nums[2]
    diff = abs(result - target)

    for pointer1 in range(len(nums)):

        l = pointer1 + 1
        r = len(nums) - 1
        while l < r:
            s = nums[pointer1] + nums[l] + nums[r]
            if abs(s - target) < diff:
                diff = abs(s - target)
                result = s

            if s < target:
                l += 1
            elif s > target:
                r -= 1
            else:
                return result

    return result


print(threeSumClosest([0,2,1,-3], 1))