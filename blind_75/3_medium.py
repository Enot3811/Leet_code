"""3. Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without duplicate characters.


Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


Constraints:
0 <= s.length <= 5 * 10**4
s consists of English letters, digits, symbols and spaces.
"""


# Размышления
# Типичная задача на два указателя
# Правым двигаемся и запоминаем, что за символы были
# Когда наткнулись на дубликат, начинает двигать левый и выбрасывать символы до тех пор
# пока дубликат не выбросится

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        memory = set()
        left = 0
        max_len = 0
        for right in range(len(s)):
            if s[right] not in memory:
                memory.add(s[right])
            else:
                max_len = max(max_len, right - left)
                while s[right] in memory:
                    memory.remove(s[left])
                    left += 1
                memory.add(s[right])
        max_len = max(max_len, right - left + 1)
        return max_len


sol = Solution()

examples = [
    ("abcabcbb", 3),
    ("bbbbb", 1),
    ("pwwkew", 3),
    ("", 0),
    (" ", 1),
    ("abcabcde", 5)
]
for s, ans in examples:
    res = sol.lengthOfLongestSubstring(s)
    print(s, res, ans)
