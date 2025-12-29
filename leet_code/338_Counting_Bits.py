"""338. Counting Bits

https://leetcode.com/problems/counting-bits/

Given an integer n, return an array ans of length n + 1 such that
for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

Example 1:
Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10

Example 2:
Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101

Constraints:
0 <= n <= 10**5

Follow up:
It is very easy to come up with a solution with a runtime of O(n log n).
Can you do it in linear time O(n) and possibly in a single pass?
"""

# Размышления
# Задача на удивление оказалась на DP.
# Рассмотрим пример
# 0 0000
# 1 0001
# 2 0010
# 3 0011
# 4 0100
# 5 0101
# 6 0110
# 7 0111
# 8 1000
# Здесь необходимо увидеть закономерность, что биты имеют цикличность,
# а также правильно представить эту закономерность.
# Возьмём 5. Это 1 старший бит и повтор для "1".
# 6: 1 старший + биты для "2"
# 7: 1 старший + биты для "3"
# То есть 1 + dp[i - offset], а offset это текущий старший бит.
# Для 4-7 это 4. Для 8 - 15 это 8.
# Помним текущий старший бит для сдвига,
# проверяем i на равенство следующему старшему биту,
# наполняем список dp

from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0]
        curr_bit = 1
        next_bit = 2
        dp = [0]
        for i in range(1, n + 1):
            if i == next_bit:
                curr_bit = next_bit
                next_bit = next_bit * 2
            dp.append(dp[i - curr_bit] + 1)
            ans.append(dp[-1])
        return ans


sol = Solution()
cases = [
    (1, [0, 1]),
    (0, [0]),
    (2, [0, 1, 1]),
    (5, [0,1,1,2,1,2]),
]
for n, ans in cases:
    res = sol.countBits(n)
    print(n, res, ans)
