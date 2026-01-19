"""91. Decode Ways

https://leetcode.com/problems/decode-ways/

You have intercepted a secret message encoded as a string of numbers.
The message is decoded via the following mapping:
"1" -> 'A'
"2" -> 'B'
...
"25" -> 'Y'
"26" -> 'Z'

However, while decoding the message, you realize that there are many different ways
you can decode the message because some codes are contained in other codes
("2" and "5" vs "25").

For example, "11106" can be decoded into:

"AAJF" with the grouping (1, 1, 10, 6)
"KJF" with the grouping (11, 10, 6)
The grouping (1, 11, 06) is invalid because "06" is not a valid code (only "6" is valid)
Note: there may be strings that are impossible to decode.

Given a string s containing only digits, return the number of ways to decode it.
If the entire string cannot be decoded in any valid way, return 0.

The test cases are generated so that the answer fits in a 32-bit integer.

Example 1:
Input: s = "12"
Output: 2
Explanation:
"12" could be decoded as "AB" (1 2) or "L" (12).

Example 2:
Input: s = "226"
Output: 3
Explanation:
"226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

Example 3:
Input: s = "06"
Output: 0
Explanation:
"06" cannot be mapped to "F" because of the leading zero ("6" is different from "06").
In this case, the string is not a valid encoding, so return 0.

Constraints:
1 <= s.length <= 100
s contains only digits and may contain leading zero(s).
"""

# Теги
# Динамическое программирование (DP)

# Размышления
# Задача сразу показалась решаемой с помощью разбиения на подзадачи.
# То есть когда решаем текущий символ + решения для оставшейся строки.
# Либо же подойти с методикой DP, где мы решаем задачу для каждого символа,
# начиная с конца и наращивая строку справа-налево.
# Однако то, как мы сращиваем решение текущего символа с предыдущими оказалось
# немного необычно.
# Пришлось покрутить примеры и вручную посчитать несколько из них, внимательно следя
# за поведением цифр
# 1 - строка
# 1 - способы декодировать
# Один символ только так и декодируется. Добавим ещё один слева
# 11  первый символ мы уже решили, а второй мы можем представить как "1" и как "11".
# 21  если представим как "1", то берём предыдущее решение, а если как "11",
# то 1 способ. Итого 2 способа
# 111  если "1", то предыдущее решение, то есть 2. А если как "11", то i - 2 решение,
# 321  то есть 1. Итого 3
# 1111  продолжаем так же и видим постоянную закономерность. Объяснить её я не могу,
# 5321  но она просто эмпирически подтверждается.
# При этом если использовать способы, где нельзя декодировать, и ставить 0,
# то ничего не нарушается.
# 1039  "39" нельзя, потому можно взять только как "3". "0" никак нельзя, потому 0.
# 1011  "1" берём и i-1 = 0, а "10" = 1, и итого 1.
# В общем, нужна насмотренность с DP и немного наблюдательности в исследовании задачи.

class Solution:
    def numDecodings(self, s: str) -> int:
        range6 = ['0','1','2','3','4','5','6']
        last_idx = len(s) - 1
        ways_to_decode = [0] * (len(s) + 2)
        ways_to_decode[-1] = 1
        ways_to_decode[-2] = 1

        for i in range(last_idx, -1, -1):
            # Если ранние строки уже не декодировались, то не продолжаем
            if ways_to_decode[i + 1] == 0 and ways_to_decode[i + 2] == 0:
                return 0

            # Способы декодировать, если воспринимать текущий символ как одиночный
            if s[i] != '0':
                decode1 = ways_to_decode[i + 1]
            else:
                decode1 = 0
            # Способы декодировать, если воспринимать текущий символ как двойной
            if (i != last_idx and (s[i] == '1' or s[i] == '2' and s[i + 1] in range6)):
                decode2 = ways_to_decode[i + 2]
            else:
                decode2 = 0

            ways_to_decode[i] = decode1 + decode2
            
        return ways_to_decode[0]


sol = Solution()
cases = [
    ("12", 2),
    ("226", 3),
    ("06", 0),
    ("123031", 0),
    ("0011111", 0),
    ("720132", 2),
]
for s, ans in cases:
    res = sol.numDecodings(s)
    print(s, res, ans)
