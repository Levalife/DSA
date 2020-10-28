'''


UNDERSTAND PATTERN OF PERMUTATION

https://www.youtube.com/watch?v=quAS1iydq7U

https://leetcode.com/problems/next-permutation/

If describe permutations in sequnce of actions than it would look like sequence of loops. Every time we would take
minimal number from decision pool:

1 2 3 4

For i in range 1..4:
    1 --> decision pool 2 3 4:
        for i in range 1..3:
            2 --> decision pool 3 4:
                for i in range 1..2:
                    3 --> decision pool 4:
                        for i in range 1:
                            4
                            1 2 3 4
                        step back
                    decision pool is empty
                    step back

                    4 --> decision pool 3:
                        for i in range 1:
                            3
                            1 2 4 3
                        step back
                    number of combinations exhausted
                    step back
            3 --> decision pool 2 4:
                for i in range 1..2:
                    2 --> decision pool 4:
                        for i in range 1:
                            4
                            1 3 2 4
                        step back
                    4 --> decision pool 2:
                        for i in range 1:
                            2
                            1 3 4 2
                        step back
                    numbers of combinations exhausted
                    step back
            4 --> decision pool 2 3:
                for i in range 1..2:
                    2 --> decision pool 3:
                        for i in range 1:
                            3
                            1 4 2 3
                        step back
                    3 --> decision pool 2:
                        for i in range 1:
                            2
                            1 4 3 2
                        step back
                    number of combinations exhausted
                    step back
            number of combinations exhausted
            step back
    2 --> decision pool 1 3 4:
        for i in range 1..3:
            1 --> decision pool 3 4:
                for i in range 1..2:
                    3 --> decision pool 4:
                        for i in range 1:
                            4
                            2 1 3 4
                        step back
                    4 --> decision pool 3:
                        for i in range 1:
                            3
                            2 1 4 3
        etc

    If look closely we can see a pattern:
        last number choice is the first decreasing number from the end of the sequence:
            1 3 4 2 --> 3

            1 4 3 2 --> 1
        to find next permutation: swap decreasing number with next greatest item from the decreasing subsequense (minimum
        number from the greatest):
            1 3 4 2 --> 3 and 4 (because 3 > 2) --> 1 4 3 2
            1 4 3 2 --> 1 and 2 --> 2 4 3 1
        and reverse decreasing subsequence so it would increase:
            1 3 4 2 --> 3 and 4 (because 3 > 2) --> 1 4 3 2 --> 1 4 2 3
            1 4 3 2 --> 1 and 2 --> 2 4 3 1 --> 2 1 3 4

        because every permutation - is the next circle in the loop where i is going in increasing order

'''


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 1
        j = i - 1

        # find first decreasing number
        while nums[i] <= nums[j] and j >= 0:
            i -= 1
            j -= 1

        if j < 0:
            nums.reverse()

        else:
            decr_index = j

            # find minimal number that greater than decreasing number
            while i < len(nums) and nums[decr_index] < nums[i]:
                i += 1

            next_index = i - 1

            # swap minimal number and decreasing number
            nums[decr_index], nums[next_index] = nums[next_index], nums[decr_index]

            # reverse sub sequence after first decreasing number
            nums[decr_index + 1:] = nums[decr_index + 1:][::-1]


