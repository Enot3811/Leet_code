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

# Теги
# Плавающее окно (left-right pointers), Словарь счётчиков (dict counter)

# Размышления
# Задача на плавающее окно и dict counter.
# Считаем буквы в искомой строке, чтобы понимать что и сколько мы ищем.
# Проходя по s2 смотрим, пытаемся собрать точно такой же счётчик словарь.
# Если встречаем ненужную букву, то сразу сброс.
# Если переполнение нужной, то придётся сужать окно, двигать левый указатель,
# выбрасывая предыдущие буквы до тех пор, пока не устранится переполнение.
# И ещё один финт, для проверки окончания сбора.
# Обычно бы нам пришлось всё время сравнивать два словаря.
# Но вместо этого заведём общий счётчик букв.
# Ведь если мы собираем только нужные буквы, то в итоге длина перестановки совпадёт
# с длиной искомой строки.

from collections import Counter, defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        source_counter = Counter(s1)
        curr_counter = defaultdict(int)
        left = 0
        total_lets = 0
        for right, let in enumerate(s2):
            # Нужная буква, счётчик
            if let in source_counter:
                # Перебор, выкидываем левые буквы, пока не устраним перебор
                while curr_counter[let] == source_counter[let]:
                    curr_counter[s2[left]] -= 1
                    total_lets -= 1
                    left += 1
                # Добавляем текущую
                curr_counter[let] += 1
                total_lets += 1
                # Заканчиваем по счётчику букв
                if total_lets == len(s1):
                    return True
            # Не нужная, сброс, начинаем заново
            else:
                curr_counter.clear()
                # Перескакиваем текущую лишнюю
                left = right + 1
                total_lets = 0
        return False

cases = [
    (['ab', 'eidbaooo'], True),
    (['ab', 'eidboaoo'], False),
    (['a', 'bbb'], False),
    (['getf', 'badfetgethf'], True),
    (["ab", "aaaab"], True),
    (["cba", "abc"], True),
    (["cbaa", "abccacba"], True)
]
sol = Solution()
for inp, ans in cases:
    res = sol.checkInclusion(*inp)
    print(inp, res, ans)
