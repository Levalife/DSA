'''

https://www.youtube.com/watch?v=KU7Ae2513h0

https://leetcode.com/problems/restore-ip-addresses/

Problem similar to NQueens Placement problem
Whenever we see words "compute all", "generate all" possible combinations - we need to use BACKTRACKING

'''


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        all_addresses = []
        path = [0] * 4
        self.helper(all_addresses, 0, s, path, 0)
        return all_addresses

    def helper(self, all_addresses, pointer, s, path, segment):


        # Basecase
        # Add valid address or stop "overshooting"
        if segment == len(path) and pointer == len(s):
            all_addresses.append(".".join(path))
            return True
        elif segment == len(path) or pointer == len(s):
            return False

        # Check all possible combination for a segment for 1, 2 and 3 digit number
        l = 0
        while l < 3 and pointer + l < len(s):

            value = s[pointer: pointer + l + 1]
            if int(value) > 255 or (value.startswith("0") and len(value) > 1):
                return False

            # chase current valid value for IP serment
            path[segment] = value

            # explore next segments
            self.helper(all_addresses, pointer + l + 1, s, path, segment + 1)

            # unchase current segment and try next or return to previous segment
            # not necessary in current situation but better for understanding
            path[segment] = 0

            l += 1
        return False

