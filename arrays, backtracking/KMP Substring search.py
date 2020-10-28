'''

Knuth-Morris-Pratt Substring Search

Given a string s and a pattern p, determine if the pattern exists in the string. Return the index of where the first
occurrence starts.

https://www.youtube.com/watch?v=BXCEFAzhxGY

https://www.youtube.com/watch?v=GTJr8OvyEVQ
https://www.youtube.com/watch?v=KG44VoDtsAA

We will preprocess the pattern string and create an array that indicates the longest proper prefix which is also suffix
at each point in the pattern string.

If we can find the length of the longest prefix that matches a suffix to that point, we can skip len(prefix) comparisons
 at the beginning.

The key reason we care about the prefix to suffix is because we want to "teleport" back to as early in the string to the
point that we still know that there is a match.

Our goal is to minimize going backwards in our search string.


'''

istring = 'abxabcabcaby'
substring = 'abcaby'

substring2 = "aabaabaaa"


def kmp_matching(s, subs):
    table = ["_" for _ in subs]
    i = 0
    j = 1
    table[0] = 0

    # create prefix/suffix table

    while j < len(subs):

        if subs[i] == subs[j]:
            table[j] = i + 1
            i += 1
            j += 1
        else:
            if i == 0:
                table[j] = 0
                j += 1
            else:
                i = table[i - 1]

    i = 0
    j = 0

    while i < len(s) and j < len(subs):
        if s[i] == subs[j]:
            i += 1
            j += 1
        else:
            if j == 0:
                i += 1
            else:
                j = table[j - 1]

    if j == len(subs):
        return i-j, s[i - j: i]
    return -1


print(kmp_matching(istring, substring))
# kmp_matching(istring, substring2)
