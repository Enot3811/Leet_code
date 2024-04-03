"""House Rubber.

You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed,
the only constraint stopping you from robbing each of them is that
adjacent houses have security systems connected and it will automatically
contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house,
return the maximum amount of money you can rob tonight
without alerting the police.

 

Example 1:
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 2:
Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9)
and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12. 

Constraints:
1 <= nums.length <= 100
0 <= nums[i] <= 400
"""


from typing import List

# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         self.memo = [-1 for _ in range(len(nums))]
#         # Смысл подобных задач в том, чтобы выстроить зависимость текущего шага
#         # от последующих.
#         # Здесь для текущего дома мы решаем задачу брать его или нет.
#         # Если берём, то необходимо узнать последствия этого решения,
#         # то есть продолжить задачу для дома i + 2
#         # Если же не берём, то смотрим, насколько много нам даст путь
#         # через дом i + 1.
#         # В итоге получается, что для решения всей задачи, нам необходимо
#         # найти решение для первого дома, а он уже впоследствии пройдёт через
#         # всю улицу
#         res = self.solve_step(nums, 0)
#         return res

#     # Смысл данной функции в том, чтобы найти оптимальное решение для i-го дома
#     def solve_step(self, nums: List[int], i: int) -> int:
#         if len(nums) == 0:
#             return 0
        
#         # Условие остановки рекурсии
#         # Если дом на текущем шаге уже выходит за улицу, то не обрабатываем его
#         if i >= len(nums):
#             return 0
        
#         # Если мы уже находили оптимальное решение для этого дома
#         if self.memo[i] != -1:
#             # то сразу возвращаем его
#             return self.memo[i]
        
#         # Вычисляем оптимальное решение для текущего дома
#         result = max(
#             self.solve_step(nums, i + 2) + nums[i],  # Либо берём его в связке с домом i + 2,
#             # и идём искать оптимальное решение для дома i + 2
#             self.solve_step(nums, i + 1)  # Либо не берём текущий дом и идём к следующему i + 1
#             # и уже ищем оптимальное решение для него
#         )

#         # Найдя оптимальное решение для текущего дома, запомним его для последующего использования
#         self.memo[i] = result
#         # Возвращаем это решение туда, где ранее его запрашивали (57 или 59)
#         return result


# class Solution:
#     def rob(self, nums):
#         if len(nums) == 0:
#             return 0
#         memo = [0 for _ in range(len(nums))]
#         memo[0] = nums[0]
#         for i in range(1, len(nums)):
#             val = nums[i]
#             if i == 1:
#                 memo[i] = max(memo[i - 1], val)
#             else:
#                 memo[i] = max(memo[i - 1], memo[i - 2] + val)
#         return memo[len(nums)]
    

class Solution:
    def rob(self, nums: List[int]) -> int:
        minus2, minus1 = 0, 0
        for n in nums:
            new_rob = max(minus2 + n, minus1)
            minus2 = minus1
            minus1 = new_rob
        return minus1


sol = Solution()
tests = [
    # ([1, 2, 3, 1], 4),
    # ([2, 7, 9, 3, 1], 12),
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
