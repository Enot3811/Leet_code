"""191. Number of 1 Bits

https://leetcode.com/problems/number-of-1-bits/

Given a positive integer n, write a function that returns the number of set bits
in its binary representation (also known as the Hamming weight).

Example 1:
Input: n = 11
Output: 3
Explanation:
The input binary string 1011 has a total of three set bits.

Example 2:
Input: n = 128
Output: 1
Explanation:
The input binary string 10000000 has a total of one set bit.

Example 3:
Input: n = 2147483645
Output: 30
Explanation:
The input binary string 1111111111111111111111111111101 has a total of thirty set bits.

Constraints:
1 <= n <= 2**31 - 1

Follow up: If this function is called many times, how would you optimize it?
"""


# Размышления
# Задача легко решается после Reverse Bits (190)
# Вспоминаем бинарные операции. Чтобы легко узнать младший бит, можно сделать & 1.
# Чтобы двигаться по битам используем двоичный сдвиг.


class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        while n > 0:
            if n & 1:
                ans += 1
            n = n >> 1
        return ans


sol = Solution()
cases = [
    (11, 3),
    (3, 2),
    (0, 0),
    (1, 1),
    (2147483645, 30),
    (128, 1)
]
for n, ans in cases:
    res = sol.hammingWeight(n)
    print(n, res, ans)
