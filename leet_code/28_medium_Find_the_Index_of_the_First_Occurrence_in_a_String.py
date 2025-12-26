"""28. Find the Index of the First Occurrence in a String.

https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

Given two strings needle and haystack, return the index of the first occurrence
of needle in haystack, or -1 if needle is not part of haystack. 

Example 1:
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.

Example 2:
Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.

Constraints:
1 <= haystack.length, needle.length <= 10**4
haystack and needle consist of only lowercase English characters.
"""

# Теги
# Неоптимальное решение

# Размышления
# Находим первую букву needle в haystack и далее проходим по обоим словам.
# Сложность O(n * m)
# Более оптимальное решение - KMP алгоритм, которые слишком сложный для собеса.

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        answer = -1
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i] == needle[0]:
                answer = i
                for s_let, f_let in zip(haystack[i + 1:], needle[1:]):
                    if s_let != f_let:
                        answer = -1
                        break
                else:
                    return answer
        return answer


if __name__ == '__main__':
    sol = Solution()
    print(sol.strStr('mississippi', 'issip'))
