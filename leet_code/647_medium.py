"""647. Palindromic Substrings

https://leetcode.com/problems/palindromic-substrings/

Given a string s, return the number of palindromic substrings in it.
A string is a palindrome when it reads the same backward as forward.
A substring is a contiguous sequence of characters within the string.

Example 1:
Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".

Example 2:
Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

Constraints:
1 <= s.length <= 1000
s consists of lowercase English letters.
"""


# Размышления
# Как и в задаче с поиском самой длинной подстроки палиндрома, пользуемся
# проверкой из центра симметрично. А это так или иначе n^2 операций.


class Solution:
    def countSubstrings(self, s: str) -> int:
        result = 0
        for i in range(len(s)):
            # Берём i-й символ за центр потенциального палиндрома
            left = right = i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                result += 1
                left -= 1
                right += 1
            # Берём i-й и i+1-й символы за центр потенциального палиндрома
            if i < len(s) - 1:  # Чтобы влез i+1
                left = i
                right = i + 1
                while left >= 0 and right < len(s) and s[left] == s[right]:
                    result += 1
                    left -= 1
                    right += 1
        return result

        
sol = Solution()

examples = [
    ("abc", 3),
    ("aaa", 6),
    ("aabac", 7)
]
for s, ans in examples:
    res = sol.countSubstrings(s)
    print(s, res, ans)
        