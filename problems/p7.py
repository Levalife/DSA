# -*- coding: utf-8 -*-

def threeSum(nums):
    pointer1 = 0
    result = []
    nums.sort()
    while pointer1 < len(nums) - 2:
        if pointer1 == 0 or nums[pointer1] != nums[pointer1 - 1]:
            l = pointer1 + 1
            r = len(nums) - 1
            while l < r:
                s = nums[pointer1] + nums[l] + nums[r]
                if s == 0:
                    result.append([nums[pointer1], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1

                    while r > l and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
        pointer1 += 1
    return result

print(threeSum([11,-8,9,-6,-10,14,-5,-10,2,-1,-14,-13,-5,9,-5,-12,9,5,-1,-4,-14,5,-11,3,6,-7,2,-14,9,-6,-8,-2,-7,8,7,-2,7,9,3,-14,-14,5,-12,-4,-9,-1,-8,7,11,-2,-11,4,-11,-15,-7,10,-7,10,4,10,11,11,-7,-11,4,7,2,-12,1,12,-10,2,2,-15,6,1,-1,13,-7,-12,-4,-11,7,0,-11,-15,-12,-10,2,7,-15,-2,3,-15,-6,14,-1,11,-13,-15,9,14,-5,-12,-15,-14,4,-9,6,5,-6,-13,9]))