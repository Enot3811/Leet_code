"""70. Climbing Stairs

https://leetcode.com/problems/climbing-stairs/

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps.
In how many distinct ways can you climb to the top? 

Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

Constraints:
1 <= n <= 45
"""

# Размышления
# Количество путей на текущий ступеньке - это количество на предыдущей + предпредыдущей.
# При этом зададим стартовые значения: первая ступень = 1, и нулевая (пол) = 1.
# По сути, получаются числа Фибоначчи.


class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        prev = 1
        prev_prev = 1
        for _ in range(1, n):
            curr = prev + prev_prev
            prev_prev = prev
            prev = curr
        return curr

sol = Solution()
cases = [
    (4, 5),
    (1, 1),
    (2, 2)
]
for n, ans in cases:
    res = sol.climbStairs(n)
    print(n, res, ans)
