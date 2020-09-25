# -*- coding: utf-8 -*-
# Given a list of numbers, find if there exists a pythagorean triplet in that list. A pythagorean triplet is 3 variables a, b, c where a^2 + b^2 = c^2

# Example:
# Input: [3, 5, 12, 5, 13]
# Output: True
# Here, 5^2 + 12^2 = 13^2.


def solution1(a):
    '''
    Time O(n^3)
    Space O(1)
    '''
    for i in range(len(a)):
        for j in range(1, len(a)):
            for k in range(2, len(a)):
                if a[i] ^ 2 + a[j] ^ 2 == a[k] ^ 2:
                    return True


def solution2(a):
    '''
    Time O(n)
    Space O(1)
    '''
    pointer1 = 0
    pointer2 = 1
    pointer3 = 2
    n = len(a)
    while pointer1 < len(a) - 2:
        print('{}^2 + {}^2 = {}^2'.format(a[pointer1], a[pointer2], a[pointer3]))
        if a[pointer1] ** 2 + a[pointer2] ** 2 == a[pointer3] ** 2:
            return True
        else:
            if pointer3 < n - 1:
                pointer3 += 1
            else:
                if pointer2 < n - 2:
                    pointer2 += 1
                    pointer3 = pointer2 + 1
                else:
                    pointer1 += 1
                    pointer2 = pointer1 + 1
                    pointer3 = pointer1 + 2


def helper(nums):
    if len(nums) < 3:
        return False

    first = 0
    second = first + 1
    third = second + 1
    while first < len(nums) - 2:
        print('{}^2 = {}^2 + {}^2'.format(nums[first], nums[second], nums[third]))
        print('{}^2 + {}^2 = {}^2'.format(nums[first], nums[second], nums[third]))

        if nums[first] ** 2 == nums[second] ** 2 + nums[third] ** 2:
            return True
        if nums[first] ** 2 + nums[second] ** 2 == nums[third] ** 2:
            return True

        if third == len(nums) - 1:
            first += 1
            second = first + 1
            third = second + 1
        else:
            third += 1

    return False



a = [3, 5, 12, 5, 13]
# print(solution1(a))
# print(solution2(a))

if __name__ == "__main__":
    # assert solution2(a)
    assert solution2([3, 12, 5, 13])
    print()
    assert helper([3, 12, 5, 13])
