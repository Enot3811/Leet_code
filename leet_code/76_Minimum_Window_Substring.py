"""76. Minimum Window Substring

https://leetcode.com/problems/minimum-window-substring/

Given two strings s and t of lengths m and n respectively,
return the minimum window substring of s such
that every character in t (including duplicates) is included in the window.
If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

Example 1:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C'
from string t.

Example 2:
Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

Example 3:
Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.

Constraints:
m == s.length
n == t.length
1 <= m, n <= 10**5
s and t consist of uppercase and lowercase English letters.

Follow up: Could you find an algorithm that runs in O(m + n) time?
"""

# Теги
# Плавающее окно (left-right pointers)

# Размышления
# Задача на counter букв и left-right окно.
# Будем расширять окно, добавляя +1 к счётчику букв.
# Расширяем до тех пор, пока счётчики не станут равны.
# Как это сделать без постоянных проверок всего counter?
# Введём переменную, которая будет хранить сколько букв в counter
# надо ещё укомплектовать.
# Когда counter[let] == target[let], то -1 от переменной.
# В итоге мы хоть и не знаем, что за буквы нам не хватает, но счётчик может сказать,
# когда нам надо остановиться, а когда продолжать.
# Как насобирали, начинаем сужать опять же пока переменная равна нулю.
# Когда вычитаем из счётчика, смотрим на target и делаем +1 к переменной,
# когда букв становится недостаточно.
# Score и ответ считаем в конце сужения.

from collections import defaultdict, Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target_dict = Counter(t)
        current_dict = defaultdict(int)
        to_collect = len(target_dict)
        right, left = 0, 0
        answer = None
        best_score = None
        while right < len(s):
            if s[right] in target_dict:
                current_dict[s[right]] += 1
                if current_dict[s[right]] == target_dict[s[right]]:
                    to_collect -= 1
                    while to_collect == 0 and left <= right:
                        if s[left] in target_dict:
                            current_dict[s[left]] -= 1
                            if current_dict[s[left]] < target_dict[s[left]]:
                                to_collect += 1
                                score = right + 1 - left
                                if answer is None or score < best_score:
                                    answer = (left, right + 1)
                                    best_score = score
                                    if best_score == len(target_dict):
                                        return s[slice(*answer)]
                        left += 1
            right += 1
        return s[slice(*answer)] if answer else ''


if __name__ == '__main__':
    sol = Solution()
    s = 'bdab'
    t = 'ab'
    result = sol.minWindow(s, t)
    print(result)
