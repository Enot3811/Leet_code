"""424. Longest Repeating Character Replacement

https://leetcode.com/problems/longest-repeating-character-replacement/

You are given a string s and an integer k. You can choose any character of the string
and change it to any other uppercase English character.
You can perform this operation at most k times.

Return the length of the longest substring containing the same letter
you can get after performing the above operations. 

Example 1:
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.

Example 2:
Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.

Constraints:
1 <= s.length <= 10**5
s consists of only uppercase English letters.
0 <= k <= s.length
"""




# Моё первое решение

# Размышления
# Основная идея здесь - проходим по строке. Если наша буква, то +1.
# Если же нет, то мы можем занять букву у k, таким образом продолжив монотонный
# отрезок
# В какой-то момент мы не сможем занять букву у k, и тогда придётся двигать ту,
# что мы ставили ранее, и тогда отрежется отрезок, который она соединяла

# from collections import deque

# class Solution:
#     def characterReplacement(self, s: str, k: int) -> int:
#         letters = set(s)
#         max_len = 0
#         stack = deque()
#         # Решаем задачу для всех букв строки
#         for curr_let in letters:
#             seg_len = 0
#             total_len = 0
#             stack.clear()
#             curr_k = 0
#             for let in s:
#                 # Если наша буква, то ++
#                 if let == curr_let:
#                     seg_len += 1
#                 else:                    
#                     # Сегмент закончился, вливаем в общую длину
#                     total_len += seg_len
#                     # Запомним длину, если придётся его отрезать
#                     stack.append(seg_len)
#                     seg_len = 0

#                     # Пытаемся занять букву у k
#                     if curr_k < k:
#                         curr_k += 1

#                     # Если занимать не получится, то надо вернуть ранее занятую
#                     else:
#                         # Перед возвратом надо проверить ответ
#                         max_len = max(max_len, total_len + curr_k)

#                         # Отрезаем то, что она соединяла
#                         total_len -= stack.popleft()
#             else:
#                 max_len = max(max_len, total_len + seg_len + curr_k)
#         return max_len

# Оптимальное решение
# Подход основан на двух указателях - расширяем окно до тех пор,
# пока выполняется условие
# Условие: если k >= всех букв в окне, кроме самой частой
# Или же k >= len - most_freq
# Здесь немного сложно было интуитивно додумать о том, как нам работать со всеми
# буквами одновременно. И вот, отталкиваемся от самой частой в окне.
# Для начала можно было бы делать поиск по дикту из 26 значений, но тогда бы
# получилось не намного лучше, чем моё верхнее решение
# Для улучшения нужна ещё одна очень неочевидная логика
# Будем смотреть max_freq не по всему дикту счётчиков, а только последний редактируемый,
# что интуитивно понятно
# Но вот когда мы двигаем left, счётчики уменьшаются, а max_freq остаётся старым.
# Теперь он стал "историческим" максимумом. Нас не интересует max_freq текущего окна до
# тех пор, пока он не станет больше предыдущего исторического.
# Почему? Потому что без увеличения max_freq не увеличится и длина окна из-за while.
# Мы продолжаем идти по строке, считать счётчики. В какой-то момент max_freq увеличится,
# и тогда мы найдём новое решение

from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = defaultdict(int)
        max_freq = 0
        left = 0
        best = 0

        for right, ch in enumerate(s):
            counts[ch] += 1
            max_freq = max(max_freq, counts[ch])

            while (right - left + 1) - max_freq > k:
                counts[s[left]] -= 1
                left += 1

            best = max(best, right - left + 1)

        return best


sol = Solution()
examples = [
    (("ABAB", 2), 4),
    (("AABABBA", 1), 4),
    (("AAABAABBAAAA", 1), 6),
    (("AAABAABBAAAA", 2), 8),
    (("AAABAABBAAAA", 0), 4),
    (("A", 0), 1),
    (("A", 1), 1),
    (("ABA", 2), 3),
    (("ABABBB", 2), 6),
    (("AAABBABBB", 2), 7),
    (("CCCCCCCCAAABBABBB", 2), 10),
    (("ABC", 3), 3),
    (("AAABBAAAACCAAA", 3), 10)
]
for inp, ans in examples:
    res = sol.characterReplacement(*inp)
    print(inp, res, ans)
