"""438. Find All Anagrams in a String

https://leetcode.com/problems/find-all-anagrams-in-a-string/

Given two strings s and p, return an array of all the start indices
of p's anagrams in s. You may return the answer in any order.

Example 1:
Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

Example 2:
Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
 
Constraints:
1 <= s.length, p.length <= 3 * 10**4
s and p consist of lowercase English letters.
"""

# Теги
# Плавающее окно (left-right pointers), Словарь счётчиков (dict counter)

# Размышления
# Задачи с анаграммами сразу наталкивают на использование counter.
# При его использовании может возникнуть вопрос,
# в какой момент мы собрали нужную строку. Не проверять же весь counter на равенство 0.
# Пользуемся длиной. В итоге нужная строка будет той длины, что и `p`, при том, что
# в counter не будет переполнения.
# И ещё один момент, на который наталкивает второй кейс.
# Анаграммы могут наслаиваться друг на друга.
# Тогда может помочь sliding window.
# Если собрали слово или переполнение, то можем двинуть левый конец.

from typing import List
from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        source_chars = Counter(p)
        orig_dict = source_chars.copy()
        left = 0
        ans = []
        for right, char in enumerate(s):
            # Если нужна эта буква
            if char in source_chars:
                source_chars[char] -= 1
                # Если переполнение - выбрасываем левые, чтобы вместить правую
                while source_chars[char] < 0 and left <= right:
                    left_char = s[left]
                    source_chars[left_char] += 1
                    left += 1
                # Проверяем, что собрали все буквы
                if right - left + 1 == len(p):
                    ans.append(left)

            # Ненужная буква обрывает всю последовательность.
            # Начинаем заново
            else:
                left = right + 1
                source_chars = orig_dict.copy()
        return ans

cases = [
    (("cbaebabacd", "abc"), [0,6]),
    (("abab", "ab"), [0,1,2]),
    (("aaaa", "a"), [0,1,2,3]),
    (("aaaa", "b"), []),
    (("aaaabaaa", "aabaa"), [0,1,2,3]),
]
sol = Solution()
for inp, ans in cases:
    res = sol.findAnagrams(*inp)
    print(inp, res, ans)
