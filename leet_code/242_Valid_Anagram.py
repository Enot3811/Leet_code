"""242. Valid Anagram

https://leetcode.com/problems/valid-anagram/

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

Constraints:
1 <= s.length, t.length <= 5 * 10**4
s and t consist of lowercase English letters.

Follow up: What if the inputs contain Unicode characters? 
How would you adapt your solution to such a case?
"""

# Размышления
# Задача на знакомство с Counter. Считаем буквы в словах, сравниваем счётчики

from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter = Counter(s)
        for let in t:
            val = counter.get(let, 0)
            if val == 0:
                return False
            counter[let] -= 1
        for let in counter:
            if counter[let] != 0:
                return False
        return True

# Быстрее за счёт оптимизации на С, но больше памяти
# Так же здесь будет проход по всем уникальным char всего раз,
# тогда как в верхнем 2 раза
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)

sol = Solution()
cases = [
    (("abcda", "dcaba"), True),
    (("abcda", "dcab"), False),
    (("abcd", "dcaba"), False),
    (("nagaram", "anagram"), True),
    (("car", "rat"), False),
    (("a", "aaa"), False),
    (("aa", "a"), False)
]
for inp, ans in cases:
    res = sol.isAnagram(*inp)
    print(inp, res, ans)
