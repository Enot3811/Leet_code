"""22. Generate Parentheses

https://leetcode.com/problems/generate-parentheses/

Given n pairs of parentheses, write a function to generate all combinations
of well-formed parentheses.

Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
Input: n = 1
Output: ["()"]

Constraints:
1 <= n <= 8
"""

# Теги
# Поиск в глубину (dfs)

# Размышления
# Обычный dfs с полным перебором.
# На текущей итерации можем либо открыть скобку и отправить дальше,
# либо закрыть и отправить дальше.
# Для отслеживания прогресса используем счётчики открытых и закрытых скобок.

from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        open_cnt = n
        close_cnt = 0
        current_str = []
        variants = Solution.solve_step(current_str, open_cnt, close_cnt)
        return variants

    @staticmethod
    def solve_step(
        current_str: List[str], open_cnt: int, close_cnt: int
    ) -> List[str]:
        if open_cnt == 0 and close_cnt == 0:
            return [''.join(current_str)]
        variants = []
        if open_cnt > 0:
            # Добавляем новые вариант, когда открыли скобку
            current_str.append('(')
            variants += Solution.solve_step(
                current_str, open_cnt - 1, close_cnt + 1)
            current_str.pop()
        if close_cnt > 0:
            # Добавляем новые вариант, когда закрыли скобку
            current_str.append(')')
            variants += Solution.solve_step(
                current_str, open_cnt, close_cnt - 1)
            current_str.pop()
        return variants

examples = [
    (1, ['()']),
    (2, ['()()', '(())']),
    (3, ['()()()', '(())()', '()(())', '((()))', '(()())']),
    (4, ["(((())))","((()()))","((())())","((()))()","(()(()))","(()()())",
         "(()())()","(())(())","(())()()","()((()))","()(()())","()(())()",
         "()()(())","()()()()"])
]
sol = Solution()
for inp, ans in examples:
    out = sol.generateParenthesis(inp)
    print(inp, out, ans, set(out) == set(ans))
