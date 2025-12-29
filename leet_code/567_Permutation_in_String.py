"""Permutation in String

Given two strings s1 and s2, return true if s2 contains a permutation 
of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

Example 1:
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:
Input: s1 = "ab", s2 = "eidboaoo"
Output: false

Constraints:
1 <= s1.length, s2.length <= 10^4
s1 and s2 consist of lowercase English letters.
"""


from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        search_cntr = Counter(s1)
        substr_cntr = Counter(s2[0:len(s1)])
        if substr_cntr == search_cntr:
            return True

        for i in range(1, len(s2) - len(s1) + 1):
            substr_cntr[s2[i - 1]] -= 1
            substr_cntr[s2[i + len(s1) - 1]] += 1
            if substr_cntr == search_cntr:
                return True
        return False


examples = [
    (['ab', 'eidbaooo'], True),
    (['ab', 'eidboaoo'], False),
    (['a', 'bbb'], False),
    (['getf', 'badfetgethf'], True),
]

sol = Solution()
for inp, ans in examples:
    out = sol.checkInclusion(*inp)
    print(inp, out, ans)
