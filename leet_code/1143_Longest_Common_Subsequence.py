"""1143. Longest Common Subsequence

https://leetcode.com/problems/longest-common-subsequence/

Given two strings text1 and text2, return the length of their longest common subsequence
If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string
with some characters (can be none) deleted without changing the relative order
of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.

Example 1:
Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.

Example 2:
Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.

Example 3:
Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.

Constraints:
1 <= text1.length, text2.length <= 1000
text1 and text2 consist of only lowercase English characters.
"""

# Размышления
# Задача, в которой необходимо было увидеть DFS или DP.
# Однако из необычного здесь то, что память для мемоизации или DP здесь n^2,
# что могло сбить с толку.
# У нас есть два указателя, на первую и на вторую строку.
# Если символы равны, то мы двигаем и один, и второй, и прибавляем +1 к ответу.
# Если символы не равны то решаем 2 подзадачи:
# 1) Если двинуть символ в первой строке
# 2) Если двинуть символ во второй строке
# Запоминаем ответы по значениям двух индексов.

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memory = {}
        def dfs(i: int, j: int) -> int:
            if i == len(text1) or j == len(text2):
                return 0
            indices = (i, j)
            if indices in memory:
                return memory[indices]
            if text1[i] == text2[j]:
                memory[indices] = dfs(i + 1, j + 1) + 1
            else:
                memory[indices] = max(dfs(i + 1, j), dfs(i, j + 1))
            return memory[indices]
        return dfs(0, 0)

# DP всё то же самое, но идём с конца и заполняем всё таблицу индексов полностью.
# Начинаем с одной последней буквы у обоих строк и просто заполняем построчно,
# двигаясь по символам одной строки, но не трогая символы другой.
# А потом добавляем 1 символ медленной строке и снова полностью заполняем строку
# таблицы, проходя по быстрой.

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Добавляем строку и столбец нулей для удобства
        dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]
        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                # Немного не интуитивно почему берём диагональный элемент,
                # если буквы равны.
                # В правых элементах уже могла быть использована текущая буква медленной
                # строки, а снизу могла быть использована текущая буква быстрой.
                # По диагонали же есть гарантия, что text1[i] и text2[j]
                # не использовались, но при этом там стоит оптимальное значение
                if text1[i] == text2[j]:
                    dp[i][j] = dp[i + 1][j + 1] + 1
                else:
                    # Берём лучшее решение из ранее решённых
                    dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])
        return dp[0][0]


sol = Solution()
cases = [
    (("ace", "aeeaccceaaee"), 3),
    (("aboba", "abobohbgjtjbbsva"), 5),
    (("zyxjkokbl", "kojob"), 3),
    (("a", "a"), 1),
    (("a", "b"), 0),
    (("jgelejghffhfdkdh", "nbmccnbnhbm"), 1),
    (("uurieootuyu", "hgkfkdjhg"), 0)
]
for inp, ans in cases:
    res = sol.longestCommonSubsequence(*inp)
    print(inp, res, ans)
