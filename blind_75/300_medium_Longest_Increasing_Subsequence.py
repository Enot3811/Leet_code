"""300. Longest Increasing Subsequence

https://leetcode.com/problems/longest-increasing-subsequence/

Given an integer array nums, return the length of the longest strictly
increasing subsequence. 

Example 1:
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101],
therefore the length is 4.

Example 2:
Input: nums = [0,1,0,3,2,3]
Output: 4

Example 3:
Input: nums = [7,7,7,7,7,7,7]
Output: 1

Constraints:
1 <= nums.length <= 2500
-10**4 <= nums[i] <= 10**4

Follow up: Can you come up with an algorithm that runs in O(n log(n)) time complexity?
"""


from typing import List, Optional

# Решение с моим подходом: бинарный выбор на каждом из шагов, ветвление
# Проблема в том, что предыдущий элемент (prev) влияет на вычисление текущего,
# потому кешировать придётся не только по i, но по (prev, i).
# Это даст кеш размером n^2
# Алгоритмическая сложность: мы будем вызывать step для каждого i (n)
# со всеми prev числами, что были до него (n).
# Итого n^2
# Вылет по памяти
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memory = {}

        def step(i: int, prev: Optional[int]):
            if i == len(nums):
                return 0
            elif (i, prev) in memory:
                return memory[(i, prev)]

            curr = nums[i]
            if prev is None or curr > prev:
                val1 = step(i + 1, nums[i]) + 1
            else:
                val1 = 0
            val2 = step(i + 1, prev)
            memory[(i, prev)] = max(val1, val2)
            return memory[(i, prev)]

        return step(0, None)


# Вариант neetcode с dfs
# Переиначим логику каждого шага
# Вместо решения брать i-th или не брать, будем перебирать кандидатов для продления.
# То есть цикл по n для каждого из n.
# В итоге для i-го элемента мы посчитаем n цепочек, начинающихся с него.
# Кешируем максимальную.
# Логика как при улучшении brute force. В нём бы мы проходились по каждому элементу и
# пытались бы построить от него максимальную цепочку (ветвление на n). Но кеш это сильно
# оптимизирует. При этом здесь кеш размером n, так как мы теперь просто для каждого i
# сохраняем максимальную цепочку
# Вылет по глубине рекурсии
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memory = {}

        def step(i: int, prev: Optional[int]):
            if i in memory:
                return memory[i]

            max_len = 0
            for j in range(i, len(nums)):
                if prev is None or nums[j] > prev:
                    max_len = max(
                        max_len,
                        step(j + 1, nums[j]) + 1
                    )
            memory[i] = max_len
            return memory[i]
        return step(0, None)


# Подход neetcode с dp
# Идём с конца в начало
# На каждом i-м мы можем взять либо просто его, либо его + самая длинная
# последовательность, которая была после него, если он меньше
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memory = [1] * len(nums)  # По умолчанию 1, то есть само число
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                # Если размер чисел позволяет,
                # то пытаемся присоединить j-ю последовательность
                if nums[i] < nums[j]:
                    memory[i] = max(memory[i], memory[j] + 1)
        return max(memory)


# Оптимальный алгоритм за nlog(n)
# Весьма смутная логика
# Вводим массив tails, который будет показывать на что оптимально может заканчиваться
# последовательность длинной i.
# Если текущий num > tails[-1], то добавляем его в tails.
# Максимальная последовательность увеличилась.
# Если же нет, то идём по tails и ищем первое число, которое будет меньше,
# и заменяем его.
# Например
# [5, 6, 1, 2, 3] -> tails: [5] -> [5,6] -> [1,6] -> [1,2] -> [1,2,3]
# Когда больше - append, когда меньше - ищем замену.
# Таким образом для LIS длины 1 лучшим вариантом будет 1.
# И потом уже на его основе может получиться ещё лучший LIS(2), LIS(3) итд.
# Ещё пример
# [10, 12, 4, 15, 5, 6]
# tails -> [10] -> [10,12] -> [4,12] -> [4,12,15] -> [4,5,12] -> [4,5,6]
# Сами числа не отражают текущий LIS, но зато сохраняют оптимальный "фундамент"
# для продолжения LIS(i). А также длину максимальной LIS
# По сложности log получается из-за того, что tails отсортирован, используем бинарный
# поиск для замен
import bisect

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] > tails[-1]:
                tails.append(nums[i])
            else:
                tails[bisect.bisect_left(tails, nums[i])] = nums[i]
        return len(tails)


sol = Solution()

examples = [
    ([2,5,7,3,1], 3),
    ([3, 2, 5, 1, 4], 2),
    ([10,9,2,5,3,7,101,18], 4),
    ([1], 1),
    ([1,10,5,11,7,12,9], 4),
    ([7,7,7,7], 1),
    ([4,10,4,3,8,9], 3),
    (list(range(1000)), 1000)
]
for nums, ans in examples:
    res = sol.lengthOfLIS(nums)
    print(nums, res, ans)
