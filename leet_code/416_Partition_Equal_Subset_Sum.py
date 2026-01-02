"""416. Partition Equal Subset Sum

https://leetcode.com/problems/partition-equal-subset-sum/

Given an integer array nums, return true if you can partition the array
into two subsets such that the sum of the elements in both subsets is equal
or false otherwise.

Example 1:
Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].

Example 2:
Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.

Constraints:
1 <= nums.length <= 200
1 <= nums[i] <= 100
"""

# Размышления
# Задача на dfs или DP.
# Проходим по числам, и на каждом числе варианты брать его или не брать.
# В итоге получается ветвление со сложностью 2^n.
# Чтобы ускорить добавим мемоизацию, где будем хранить индекс и сумму, которую смогли
# получить дойдя до него.
# При этом для каждого i может быть множество возможных сумм.
# И здесь очень интересная оценка этой оптимизации.
# Может показаться, что она не сильно помогает, ведь могут быть такие числа, 
# что они будут давать суммы, которые совсем не пересекаются.
# Но даже так, эта мемоизация всё равно ускоряет.
# Ведь для каждого i будет всего target состояний суммы.
# А вместе это будет n * target.

# Всегда когда есть dfs, есть менее очевидный, но более эффективный вариант с DP.
# Создадим таблицу размера target + 1.
# Индекс элемента будет показывать на число (сумму),
# которую мы получили или можем получить.
# Изначально заполним весь массив False, кроме нуля.
# Затем получая текущее num, мы можем прибавить его ко всем i, которые не False,
# и получить новые варианты сумм, добавив новые True в массиве.
# В итоге получается такая же сложность n * target, но без рекурсий, доп. памяти и
# прочих расходов.

from typing import List

# dfs с ручным стеком: медленнее чем рекурсия, много памяти
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)
        if target % 2 != 0:
            return False
        target = target // 2

        memory = set()
        stack = [(0, 0)]
        while stack:
            i, s = stack.pop()
            # Уже был этот вариант
            if (i, s) in memory:
                continue
            # Дошли до цели
            if s == target:
                return True
            # Перебрали все числа или перескочили цель
            if i >= len(nums) or s > target:
                continue
            else:
                memory.add((i, s))
            # 2 варианта на пробу
            # Взять текущее число
            stack.append((i + 1, s + nums[i]))
            # или не брать
            stack.append((i + 1, s))
        # Всё перебрали
        return False

# dfs с рекурсией, всё ещё много памяти
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)
        if target % 2 != 0:
            return False
        target = target // 2
        memory = set()

        def dfs(i: int, s: int):
            # Уже был этот вариант
            if (i, s) in memory:
                return False
            # Дошли до цели
            if s == target:
                return True
            # Перебрали все числа или перескочили цель
            if i >= len(nums) or s > target:
                return False
            else:
                memory.add((i, s))
            # 2 варианта на пробу: взять текущее число или не брать
            return dfs(i + 1, s + nums[i]) or dfs(i + 1, s)
        return dfs(0, 0)

# DP, никаких лишних затрат памяти
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)
        if target % 2 != 0:
            return False
        target = target // 2

        # Индекс - число (сумма), которые мы получали ранее
        dp = [False] * (target + 1)
        dp[0] = True
        for num in nums:
            if num > target:
                continue
            # Проходим по всем возможным суммам.
            # Идём обязательно с конца, так как будем модифицировать dp.
            # И идя из начала мы бы пересекались с True,
            # которые выставили на предыдущей итерации.
            for i in range(len(dp) - 1, -1, -1):
                # Если такая была, то комбинируем число с ней
                if dp[i]:
                    s = i + num
                    if s <= target:
                        dp[s] = True
        return dp[target]

cases = [
    ([1,5,11,5],True),
    ([1,2,3,5],False),
    ([1,2,5],False),
    ([3,7],False),
    ([3,7,6],False),
    ([1,2,3,4,5,6,7,8,9,10,11],True),
]
sol = Solution()
for nums, ans in cases:
    res = sol.canPartition(nums)
    print(nums, res, ans)
