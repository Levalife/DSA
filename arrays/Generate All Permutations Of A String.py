'''

WHEN SEE WORDS "PRINT ALL", "GENERATE ALL", "COMPUTE ALL" it's always about BACKTRACKING

Problem similar to NQueens Placement problem and Restore IP addresses

https://www.youtube.com/watch?v=GCm7m5671Ps
Times complexity n * n! (cycle + recurcive calls for all combinations that left)

Space complexity: n if print resuld
                  n * n! if safe result to an array



Time: O(n * n!)

- There are n! permutations and it takes O(n) time to add each one to our result array

Space: O(n)
- We are not returning an array here so linear space because our recursion will go at maximum n elements deep since we
make n choices of placement at maximum

- If we did store and return an array our space complexity would be O(n * n!) since we would have n! permutations and
each permutation would be of length n. If we consider the returned array of all permutation strings as NOT part of
space, the call stack dominates space. We are back to O(n).

'''


def permute(s):
    helper(s, '')

def helper(s, choices):

    if len(s) == 1:
        print(choices + s[0])
        return True

    for i in range(len(s)):


        decision_space = s[:i]
        if i < len(s):
            decision_space += s[i + 1:]

        # chase current letter choice (exp: "b")
        choices += s[i]

        # explore all letters that left (exp: "oat"
        helper(decision_space, choices)

        # uncheck previous choice (exp: "" to get ability choose next letter "o" for the first place in the next cycle)
        choices = choices[:-1]

permute('boat')
