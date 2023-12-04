"""House Rubber."""

from typing import List


# class Solution:
#     def solve(self, nums, i, memory):
#         if i not in memory:
#             next1 = self.solve(nums, i + 2, memory) if i + 2 < len(nums) else 0
#             next2 = self.solve(nums, i + 3, memory) if i + 3 < len(nums) else 0
#             memory[i] = nums[i] + max(next1, next2)
#         return memory[i]

#     def rob(self, nums: List[int]) -> int:
#         memory = {}
#         if len(nums) == 1:
#             return nums[0]
#         return max(self.solve(nums, 0, memory), self.solve(nums, 1, memory))


# class Solution:

#     def rob(self, nums: List[int]) -> int:
#         memory = {}

#         def solve(i):
#             if i >= len(nums):
#                 return 0
#             if i not in memory:
#                 # Значение для текущего выбираем не как текущий плюс один из
#                 # следующих, а как либо текущий и +2, либо вместо идёт просто
#                 # сосед
#                 # В итоге та же сетка, где может быть как через 1 или 2,
#                 # но решение принимает не solve(i), а solve(i + 1)
#                 memory[i] = max(solve(i + 1), nums[i] + solve(i + 2))
#             return memory[i]
#         solve(0)
#         return memory[0]
    
class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        for n in nums:
            new_rob = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = new_rob
        return rob2


sol = Solution()
tests = [
    ([1, 2, 3, 1], 4),
    ([2, 7, 9, 3, 1], 12),
    ([5, 1, 6, 4, 2, 6, 1, 2, 8, 9], 28),
    ([3, 6, 6, 4, 9, 1], 18),
    ([94, 23, 33, 150, 39, 3, 46, 54, 27, 71, 12, 41, 64, 14, 82], 518),
    ([82, 94, 23, 1], 105),
    ([200, 275, 7, 305, 146, 9, 86, 371, 104, 192, 69, 254, 236, 143, 271, 238,
      202, 356, 274, 196, 157, 165, 375, 29, 89, 160, 130, 197, 390, 52, 151,
      11, 217, 349, 60, 313, 66, 160, 230, 46, 112, 349, 314, 285, 117, 216,
      353, 59, 119, 50, 364, 84, 256, 154, 244, 196, 131, 96, 338, 344, 91,
      142, 3, 209, 338, 57, 321, 329, 351, 174, 391, 169, 7, 153, 109, 127,
      300, 54, 362, 198, 304, 249, 192, 136, 34, 75, 333, 337, 388, 311, 50,
      38, 157, 184, 52, 107, 66, 60, 389, 122], 11150),
]

for inp, ans in tests:
    out = sol.rob(inp)
    print('Out:', out, 'Exp:', ans)
