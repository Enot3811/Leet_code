"""152. Maximum Product Subarray

https://leetcode.com/problems/maximum-product-subarray/

Given an integer array nums, find a subarray that has the largest product,
and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

Note that the product of an array with a single element is the value of that element.

 

Example 1:
Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Example 2:
Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

Constraints:
1 <= nums.length <= 2 * 10**4
-10 <= nums[i] <= 10
The product of any subarray of nums is guaranteed to fit in a 32-bit integer.
"""

from typing import List

# Размышления
# Вспомнился финт с кумулятивной суммой, только здесь произведения
# Произведения вносят пару моментов:
# 1) Нули делят массив на отрезки. Считаем кумулятивную сумму на отрезках
# 2) Отрицательные числа меняют знак
# Чтобы справиться с отрицательными числами, необходимо запоминать первую встретившуюся
# на отрезке отрицательное кумулятивное произведение.
# Тогда если число большое, но отрицательное, мы сможем "отрезать" кусок отрезка, 
# представленный этой запомненным кумулятивным произведением


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Считаем кумулятивные произведения, разделённые нулями
        cum_prods = [1] * len(nums)
        curr_prod = 1
        for i, num in enumerate(nums):
            cum_prods[i] = curr_prod * num

            # Нули делят массив на отрезки
            if num == 0:
                curr_prod = 1

            else:
                curr_prod = cum_prods[i]
        # print(cum_prods)
        
        # Пройдёмся по кумулятивным суммам, ищем максимальное число
        # или максимальное делённое на первое встретившееся отрицательное произведение
        first_neg_prod = 1  # 1 так как при делении не повлияет
        ans = nums[0]  # берём первое число, если оно единственное
        for cum_prod in cum_prods:
            ans = max(
                ans,
                # Либо просто накопительное произведение, либо меняем знак и отрезаем
                # часть отрезка, ограниченного первым отрицательным числом
                max(cum_prod, cum_prod // first_neg_prod)
            )
            # Запоминаем кумулятивное произведение для первого отрицательного числа
            if cum_prod < 0 and first_neg_prod == 1:
                first_neg_prod = cum_prod
            # Нули делят массив на отрезки
            elif cum_prod == 0:
                first_neg_prod = 1
        return ans


sol = Solution()

examples = [
    ([2,3,-2,4], 6),
    ([-2, 0, -2], 0),
    ([2, 5, 0, 5, 3, 0, 5, 1, 1, 0, 1], 15),
    ([2, 5, 0, 5, -3, 0, 5, 1, 1, 0, 1], 10),
    ([4,5,-1,30], 30),
    ([-2, -4, -5, -1], 40),
    ([5, 2, -1, 0, -2000], 10),
    ([1], 1),
    ([-1], -1),
    ([0], 0),
    ([-5,0, -3, -1, 0], 3),
    ([-1, 0], 0),
    ([0, -1], 0),
    ([2,-5,-2,-4,3], 24),
    ([2, 4, -1, -3, -10, 0, 2, -3, -2, -10], 30),
    ([2, 4, -1, -3, -10, 0, 2, -3, -4, -10], 40)
]
for nums, ans in examples:
    res = sol.maxProduct(nums)
    print(nums, res, ans)
