"""190. Reverse Bits

https://leetcode.com/problems/reverse-bits/

Reverse bits of a given 32 bits signed integer.

Example 1:
Input: n = 43261596
Output: 964176192
Explanation:
Integer	Binary
43261596	00000010100101000001111010011100
964176192	00111001011110000010100101000000

Example 2:
Input: n = 2147483644
Output: 1073741822
Explanation:
Integer	Binary
2147483644	01111111111111111111111111111100
1073741822	00111111111111111111111111111110

Constraints:
0 <= n <= 2**31 - 2
n is even.

Follow up: If this function is called many times, how would you optimize it?
"""


# Размышления
# С помощью питона можно сделать
# bn = bin(n)[:1:-1]
# bn += (32 - len(bn)) * '0'
# print(bin(int(bn, base=2)))
# Если делать си подобный алгоритм, то вспоминаем бинарные операции.
# Чтобы быстро узнать значение младшего бита числа используем бинарное И: n & 1
# Чтобы двинуть биты влево, используем бинарный сдвиг: ans << 1

class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        for _ in range(32):
            ans = ans << 1
            ans += n & 1
            n = n >> 1
        return ans

sol = Solution()
# n = 4294967294  # 2**31 - 2
n = 19
print(bin(n), len(bin(n)) - 2)
ans = sol.reverseBits(n)
print(bin(ans), len(bin(ans)) - 2)
