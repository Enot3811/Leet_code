"""271. Encode and Decode Strings

Premium lock.
https://neetcode.io/problems/string-encode-and-decode/question

Design an algorithm to encode a list of strings to a single string.
The encoded string is then decoded back to the original list of strings.

Please implement encode and decode

Example 1:
Input: ["neet","code","love","you"]
Output:["neet","code","love","you"]

Example 2:
Input: ["we","say",":","yes"]
Output: ["we","say",":","yes"]

Constraints:
0 <= strs.length < 100
0 <= strs[i].length < 200
strs[i] contains only UTF-8 characters.
"""

# Размышления
# Творческая задача. По сути, если нам нужно склеить строки с возможностью
# их восстановления, то просто добавляем разделительные символы или их комбинацию.
# Можно сделать немного запутанней и интереснее.
# Можно отсортировать слова по длине и разбить их по "бакетам".
# Потом при их склеивании можно будет делать шаг размером с представителя этого
# бакета, чтобы их расклеить. Тогда сохранить размер по типу:
# "abc", "cde" -> "#3#abccde"
# То есть декодируем номер и делаем шаги пока не упрёмся в следующий ограничитель.
# Я сделал ещё запутаннее. Символы слов одной длины можно смешать в шахматном порядке,
# и затем обратно распутать, если знать, сколько слов в бакете.
# "abc", "cde" -> "#2#acbdce"

from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = []
        # Сортируем по длинам, чтобы легче отбирать строки одной длины
        strs = sorted(strs, key=len)
        left = right = 0
        while right < len(strs):
            curr_len = len(strs[left])

            # Находим left-right строк с текущей длиной
            while right < len(strs) and len(strs[right]) == curr_len:
                right += 1

            # Добавляем количество слов в виде разделителя
            ans.append('#' + str(right - left) + '#')

            # Смешиваем символы слов в шахматном порядке
            curr_comb = []
            for i in range(curr_len):
                for j in range(left, right):
                    curr_comb.append(strs[j][i])
            ans += curr_comb
            left = right
        return ''.join(ans)


    def decode(self, s: str) -> List[str]:
        ans = []
        left = right = 0
        while right < len(s):
            # Декодируем ограничитель с количеством слов
            if s[right] == '#':
                right += 1
                left = right
                while s[right] != '#':
                    right += 1
                num_words = int(s[left:right])
            right += 1
            
            # Ищем следующий ограничитель
            left = right
            while right < len(s) and s[right] != '#':
                right += num_words  # ускоренный шаг (минимальное слово 1 символ)

            # Распутываем слова
            for i in range(num_words):
                ans.append(s[left + i:right:num_words])
            left = right
        return ans

            


sol = Solution()
encoded = sol.encode([
    "cup","tea","late","lane","lame","tame","pirate","yellow","joke","night","version",
    "morning","task","detective","dare","care","door","core","more","rule","hello"
])
print(encoded)
decoded = sol.decode(encoded)
print(decoded)
