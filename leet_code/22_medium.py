"""Generate Parentheses

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
            # Add new variants when we open parentheses
            current_str.append('(')
            variants += Solution.solve_step(
                current_str, open_cnt - 1, close_cnt + 1)
            current_str.pop()
        if close_cnt > 0:
            # Add new variant when we close parentheses
            current_str.append(')')
            variants += Solution.solve_step(
                current_str, open_cnt, close_cnt - 1)
            current_str.pop()
        return variants


sol = Solution()

examples = [
    (1, ['()']),
    (2, ['()()', '(())']),
    (3, ['()()()', '(())()', '()(())', '((()))', '(()())']),
    (4, ["(((())))","((()()))","((())())","((()))()","(()(()))","(()()())",
         "(()())()","(())(())","(())()()","()((()))","()(()())","()(())()",
         "()()(())","()()()()"])
]

for inp, ans in examples:
    out = sol.generateParenthesis(inp)
    print(inp, out, ans, set(out) == set(ans))
