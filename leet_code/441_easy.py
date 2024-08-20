"""441. Arranging Coins

https://leetcode.com/problems/arranging-coins/description/
"""

class Solution:
    def arrangeCoins(self, n: int) -> int:
        sum = 0
        i = 0
        while sum < n:
            i += 1
            sum += i
        if sum > n:
            i -= 1
        return i
    

sol = Solution()
samples = [(0, 0), (1, 1), (5, 2), (8, 3)]
for inp, ans in samples:
    res = sol.arrangeCoins(inp)
    print(inp, res, ans)
