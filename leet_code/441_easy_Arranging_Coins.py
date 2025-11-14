"""441. Arranging Coins

https://leetcode.com/problems/arranging-coins/description/
"""

# class Solution:
#     def arrangeCoins(self, n: int) -> int:
#         sum = 0
#         i = 0
#         while sum < n:
#             i += 1
#             sum += i
#         if sum > n:
#             i -= 1
#         return i


class Solution:
    def arrangeCoins(self, n: int) -> int:
        # k * (k + 1) / 2 <= n
        # Необходимо найти наибольший k, удовлетворяющий этому условию
        # Ищем бинарным поиском среди чисел 0...n
        left = 0
        right = n
        while left <= right:
            k = (left + right) // 2
            cur_sum = k * (k + 1) / 2
            if cur_sum < n:
                left = k + 1
            elif cur_sum > n:
                right = k - 1
            else:
                return k
        return right


sol = Solution()
samples = [(0, 0), (1, 1), (5, 2), (8, 3)]
for inp, ans in samples:
    res = sol.arrangeCoins(inp)
    print(inp, res, ans)
