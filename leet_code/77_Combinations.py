"""77. Combinations

https://leetcode.com/problems/combinations/

Given two integers n and k, return all possible combinations of k numbers
chosen from the range [1, n].

You may return the answer in any order.

Example 1:
Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
Explanation: There are 4 choose 2 = 6 total combinations.
Note that combinations are unordered, i.e.,
[1,2] and [2,1] are considered to be the same combination.

Example 2:
Input: n = 1, k = 1
Output: [[1]]
Explanation: There is 1 choose 1 = 1 total combination.

Constraints:
1 <= n <= 20
1 <= k <= n
"""

# Теги
# Поиск в глубину (dfs)

# Размышления
# Задача на ветвление через dfs.
# На текущем шаге можем перебрать все числа от предыдущего числа до n.
# Вглубь идём до k.

from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        current = []
        n += 1  # для удобства range
        def dfs(curr_k: int, curr_n: int):
            if curr_k == k:
                ans.append(current.copy())
                return
            for num in range(curr_n, n):
                current.append(num)
                dfs(curr_k + 1, num + 1)
                current.pop()
        dfs(curr_k=0, curr_n=1)
        return ans

cases = [
    ((4, 2), [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]),
    ((1, 1), [[1]]),
    ((3,3),[[1,2,3]])
]
sol = Solution()
for inp, ans in cases:
    res = sol.combine(*inp)
    print(inp, res, ans)
