"""5. Longest Palindromic Substring

https://leetcode.com/problems/longest-palindromic-substring

Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"


Constraints:
1 <= s.length <= 1000
s consist of only digits and English letters.
"""

# Теги
# Раздвигающиеся указатели (left-right pointers), Неоптимальное решение

# Размышления
# Проверка строки на палиндром производится за линейное время, если идти из центра
# симметрично.
# Делаем такую проверку для каждой буквы, получаем O(n^2) решение.
# Есть алгоритм Manacher, который позволяет найти палиндром за O(n) времени,
# но он очень сложный и не очень понятный.

class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_palindrome = ""
        for i in range(len(s)):
            # Проверяем нечётный центр
            right = i
            left = i
            cur_len = 0
            while left >= 0 and right < len(s) and s[right] == s[left]:
                cur_len += 1
                left -= 1
                right += 1
            if len(max_palindrome) < len(s[left + 1:right]):
                max_palindrome= s[left + 1:right]
            # Проверяем чётный центр
            right = i + 1
            left = i
            cur_len = 0
            while left >= 0 and right < len(s) and s[right] == s[left]:
                cur_len += 1
                left -= 1
                right += 1
            if len(max_palindrome) < len(s[left + 1:right]):
                max_palindrome= s[left + 1:right]
        return max_palindrome


sol = Solution()

examples = [
    ("babad", "bab"),
    ("bbbbb", "bbbbb"),
    ("cbbd", "bb"),
    ("a", "a"),
    ("abcde", "a"),
    ("babcbab", "babcbab"),
    ("babnhycacacmam", "cacac")
]
for s, ans in examples:
    res = sol.longestPalindrome(s)
    print(s, res, ans)
