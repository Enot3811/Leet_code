"""198. House Rubber

https://leetcode.com/problems/house-robber/

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

# Теги
# Поиск в глубину (dfs), Мемоизация словарём (dict memoization),
# Конечный автомат (finite state machine)

# Размышления
# Смысл подобных задач в том, чтобы выстроить зависимость текущего шага от последующих.
# Здесь для текущего дома мы решаем задачу брать его или нет.
# Если берём, то необходимо узнать последствия этого решения,
# то есть продолжить задачу для дома i + 2.
# Если же не берём, то смотрим, насколько много нам даст путь через дом i + 1.
# В итоге получается, что для решения всей задачи, нам необходимо найти решение
# для первого дома, а он уже впоследствии пройдёт через всю улицу.

from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        self.memo = [-1 for _ in range(len(nums))]
        res = self.solve_step(nums, 0)
        return res

    # Решаем задачу для i-го дома
    def solve_step(self, nums: List[int], i: int) -> int:
        if len(nums) == 0:
            return 0
        
        # Условие остановки рекурсии
        # Если дом на текущем шаге уже выходит за улицу, то не обрабатываем его
        if i >= len(nums):
            return 0
        
        # Если мы уже находили оптимальное решение для этого дома
        if self.memo[i] != -1:
            # то сразу возвращаем его
            return self.memo[i]
        
        # Вычисляем оптимальное решение для текущего дома
        result = max(
            # Либо берём его в связке с домом i + 2,
            self.solve_step(nums, i + 2) + nums[i],
            # Либо не берём текущий дом и идём к следующему i + 1
            self.solve_step(nums, i + 1)
        )

        # Найдя оптимальное решение для текущего дома,
        # запомним его для последующего использования
        self.memo[i] = result
        return result


# Оптимизируем эту задачу. Удалим рекурсию и память. Сделаем похожим на DP.
# В первом решении мы брали текущий и смотрели вперёд, здесь же смотрим назад.
# У нас есть: n - текущий, prev - предыдущий, prev_prev - предыдущий через 1.
# Мы можем взять текущий + prev_prev или взять prev.
# То, что окажется больше, будет результатом для текущего дома.
# Сдвигаясь вперёд текущее решение становится prev, а prev -> prev_prev

class Solution:
    def rob(self, nums: List[int]) -> int:
        prev_prev, prev = 0, 0
        for n in nums:
            new_rob = max(prev_prev + n, prev)
            prev_prev = prev
            prev = new_rob
        return prev

# Дополнение
# Оказалось, что решение выше - это конечный автомат.
# Хороший разбор есть в задаче 309.
# Очень хороший алгоритм, позволяющий решить любую задачу на автоматы.
# 1) Определим возможные состояния:
# - rest - решили сейчас ничего не делать
# - rob - решили сейчас грабить дом
# 2) Определить переходы в эти состояния:
# - В rest мы можем попасть если ничего не делали ранее (rest)
# или ограбили предыдущий дом (rob)
# - В rob мы можем попасть если ничего не делали ранее (rest)
# и грабим текущий дом (num)
# И каждый раз берём максимальное из возможных состояний.
# В итоге решение немного отличается, но остаётся верным и интуитивно понятным.
class Solution:
    def rob(self, nums: List[int]) -> int:
        rest = 0  # Ничего не делаем
        rob = 0  # Грабим дом
        for num in nums:
            prev_rest = rest
            prev_rob = rob
            # ничего не делать можем если:
            # 1) Ничего не делали и продолжаем
            # 2) Ограбили дом и сейчас не можем грабить текущий
            rest = max(prev_rest, prev_rob)
            # Грабить можем, если ничего не делали ранее (нет ограничения) и грабим текущий
            rob = prev_rest + num
        return max(rest, rob)


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

for nums, ans in tests:
    res = sol.rob(nums)
    print(nums, res, ans)
