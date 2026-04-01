"""1446. Consecutive Characters

https://leetcode.com/problems/consecutive-characters/

The power of the string is the maximum length of a non-empty substring
that contains only one unique character.

Given a string s, return the power of s. 

Example 1:
Input: s = "leetcode"
Output: 2
Explanation: The substring "ee" is of length 2 with the character 'e' only.

Example 2:
Input: s = "abbcccddddeeeeedcba"
Output: 5
Explanation: The substring "eeeee" is of length 5 with the character 'e' only.

Constraints:
1 <= s.length <= 500
s consists of only lowercase English letters.
"""


class Solution:
    def maxPower(self, s: str) -> int:
        left = 0
        max_len = 1
        for right, char in enumerate(s):
            if char != s[left]:
                max_len = max(max_len, right - left)
                left = right
        max_len = max(max_len, right - left + 1)
        return max_len

sol = Solution()
cases = [
    ("leetcode", 2),
    ("abbcccddddeeeeedcba", 5),
    ("a", 1),
    ("aaaa", 4),
    ("abbaabbaabbaa", 2),
    ("abbccc", 3)
]
for s, ans in cases:
    res = sol.maxPower(s)
    print(s, res, ans)
