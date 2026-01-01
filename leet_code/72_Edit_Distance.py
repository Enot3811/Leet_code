"""72. Edit Distance

https://leetcode.com/problems/edit-distance/

Given two strings word1 and word2, return the minimum number of operations
required to convert word1 to word2.

You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character

Example 1:
Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')

Example 2:
Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')

Constraints:
0 <= word1.length, word2.length <= 500
word1 and word2 consist of lowercase English letters.
"""

# Теги
# Динамическое программирование (DP)

# Размышления
# Задача на 2d DP, которую очень важно правильно представить.
# У нас будет 2 указателя, указывающие на текущую букву в двух словах.
# Если буквы равны, то оба указателя сдвигаются, и мы не делаем никакой операции.
# А если не равны, то нужно применить одну из операций.
# Так как мы не знаем, какая будет профитнее, то применим все 3.
# При этом, если мы делаем replace, то сдвинутся оба указателя.
# Если delete, то двинется только указатель первого слова.
# А если insert, то только второго.
# Этого, должно быть достаточно чтобы сделать dfs.
# Делаем dict, представляющий собой таблицу len(word1) на len(word2).
# Запускаем 3 варианта со сдвинутыми индексами когда не равны, и 1 когда равны.
# Стремимся к концам слов.
# Но чтобы убрать рекурсию сразу пойдём в bottom-up DP.
# Постановка задачи для букв i и j остаётся та же.
# Если не равны, то нам нужно решить задачи с (i+1,j), (i,j+1), (i+1,j+1),
# то есть 3 возможные операции, и сделать к ним +1.
# Но так как это теперь bottom-up, у нас в таблице уже уже будут ответы для этих задач.
# Просто возьмём минимальный из них.
# Если же буквы равны, то мы можем сдвинуть оба указателя не делая +1.
# То есть берём решение (i + 1, j + 1).
# Для удобства так же можно добавить дополнительный столбец и строку, представляющие
# сравнение с пустотой после слова.
# То есть когда указатель доходит до конца строки, он указывает на её пустоту,
# и у него всего один выбор - delete/insert вплоть до тех пор, пока не дойдёт
# до пустоты второй строки.
# Также это покроет случай с пустой изначальной строкой.
# "" и "abc". "" и "". Равны, ответ 0. "" и "c". Нужно добавить букву +1.
# "" и "bc". Нужно добавить букву и взять предыдущее решение = 2.

# Что имеем в итоге:
# Таблица размером (len(word1) + 1, len(word2) + 1).
# Последняя строка и столбец заполнены базовыми случаями со значениями от 0 до len.
# Заполняем всю таблицу последовательно.
# Если word[i] != word[j], то берём лучшее из всех предыдущих решений
# min(delete, insert, replace) и делаем +1.
# Если же равны, то берём вариант с replace (i + 1, j + 1) и не прибавляем 1.
# (Берём replace потому, что это кратчайший путь до одинаковых букв.
# Иначе пришлось бы делать delete и insert)

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]
        # Заполняем дополнительную строку/столбец
        for i in range(len(word1) - 1, -1, -1):
            dp[i][-1] = len(word1) - i
        for i in range(len(word2) - 1, -1, -1):
            dp[-1][i] = len(word2) - i

        # Заполняем таблицу
        for i in range(len(word1) - 1, -1, -1):
            for j in range(len(word2) - 1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    dp[i][j] = min(dp[i + 1][j], dp[i][j + 1], dp[i + 1][j + 1]) + 1
        return dp[0][0]


cases = [
    (("horse", "ros"), 3),
    (("intention", "execution"), 5),
    (("aaabbccc", "aabc"), 4),
    (("xaaabbccc", "yaabc"), 5),
    (("xabbcc", "yadcc"), 3),
    (("xabbcc", "yyadcc"), 4),
    (("abbbbbbbbbcc", "adddddddddcc"), 9)
]
sol = Solution()
for inp, ans in cases:
    res = sol.minDistance(*inp)
    print(inp, res, ans)
