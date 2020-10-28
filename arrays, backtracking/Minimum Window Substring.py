'''

Utilizing Two Pointers & Tracking Character Mappings With A Hashtable

https://leetcode.com/problems/minimum-window-substring/

https://www.youtube.com/watch?v=eS6PZLjoaq8

Thw simpliest approach is to check all possible combinations like in Maximum Subarray

S = "ADOBECODEBANC", T = "ABC"

A

A D

A D O

......

A D O B E C O D E B A N C

  D

  D O

  D O B

  .......

  D O B E C O D E B A N C

  ........

                    A N C
                      N C
                        C

Check every time is all symbols from the T is in substring, save minimum substring which satisfies the conditions.

Second approach is to increase right pointer till substring is satisfies condition and move left pointer forward (because
from this point every string will satisfy condition but the length of the string will grow)

To track condition w'll use a hashmap:

d = {A: 1, B: 1, C: 1}

A D O B E C O D E B A N C
L
R                           A   d = {A: 0, B: 1, C: 1}

A D O B E C O D E B A N C
L
  R                         A D     d = {A: 0, B: 1, C: 1}

A D O B E C O D E B A N C
L
    R                       A D O    d = {A: 0, B: 1, C: 1}

A D O B E C O D E B A N C
L
      R                     A D O B   d = {A: 0, B: 0, C: 1}

A D O B E C O D E B A N C
L
        R                   A D O B E   d = {A: 0, B: 0, C: 1}

A D O B E C O D E B A N C
L
          R                 A D O B E C   d = {A: 0, B: 0, C: 0}


A,B,C == 0, substring A D O B E C satisfies condition, we can move L forward in cycle while substring satisfies condition
(to shorten substring if it possible) and if S[L] in d -> return tracked letter

d = {A: 1, B: 0, C: 0}

A D O B E C O D E B A N C
  L
          R                 D O B E C   d = {A: 1, B: 0, C: 0}

A > 0, so substring unsatisfies condition and we need move R again to open new possibilities

A D O B E C O D E B A N C
  L
            R               D O B E C O  d = {A: 1, B: 0, C: 0}

A > 0, so substring unsatisfies condition and we need move R again to open new possibilities

A D O B E C O D E B A N C
  L
              R             D O B E C O D   d = {A: 1, B: 0, C: 0}

A > 0, so substring unsatisfies condition and we need move R again to open new possibilities

A D O B E C O D E B A N C
  L
                R           D O B E C O D E   d = {A: 1, B: 0, C: 0}

A D O B E C O D E B A N C
  L
                  R         D O B E C O D E B   d = {A: 1, B: -1, C: 0}

A D O B E C O D E B A N C
  L
                    R       D O B E C O D E B A   d = {A: 0, B: -1, C: 0}

A,B,C <= 0, substring D O B E C O D E B A satisfies condition, we can move L forward in cycle while substring satisfies condition
(to shorten substring if it possible) and if S[L] in d -> return tracked letter

    A D O B E C O D E B A N C
        L
                        R       D O B E C O D E B A   d = {A: 0, B: -1, C: 0}

    A D O B E C O D E B A N C
          L
                        R       D O B E C O D E B A   d = {A: 0, B: 0, C: 0}

                        ....

    A D O B E C O D E B A N C
              L
                        R       C O D E B A   d = {A: 0, B: 0, C: 0}

    A D O B E C O D E B A N C
                L
                        R       C O D E B A   d = {A: 0, B: 0, C: 1}

Mode R

A D O B E C O D E B A N C
            L
                      R       C O D E B A   d = {A: 0, B: 0, C: 1}

A D O B E C O D E B A N C
            L
                        R       C O D E B A   d = {A: 0, B: 0, C: 0}

A,B,C <= 0, substring O D E B A N C satisfies condition, we can move L forward in cycle while substring satisfies condition
(to shorten substring if it possible) and if S[L] in d -> return tracked letter

    A D O B E C O D E B A N C
                  L
                            R       O D E B A N C   d = {A: 0, B: 0, C: 0}

    A D O B E C O D E B A N C
                    L
                            R       O D E B A N C   d = {A: 0, B: 0, C: 0}

    A D O B E C O D E B A N C
                      L
                            R       B A N C   d = {A: 0, B: 0, C: 0}

    A D O B E C O D E B A N C
                        L
                            R       B A N C   d = {A: 0, B: 1, C: 0}

B > 0, condition unsatisfied. Move R, but R is == len(S). Exit from the cycle

B A N C is result
'''


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        d = {}

        for letter in t:
            d[letter] = d.get(letter, 0) + 1

        l = 0
        r = 0
        min_s = ""
        while r < len(s):
            if s[r] in d:
                d[s[r]] -= 1

            while self.is_satisfies(d) and l < len(s):

                if not min_s or len(s[l:r]) < len(min_s):
                    min_s = s[l:r + 1]

                if s[l] in d:
                    d[s[l]] += 1
                l += 1

            r += 1

        return min_s

    def is_satisfies(self, d):
        if max(d.values()) > 0:
            return False
        return True



