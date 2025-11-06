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
# Просто перемножаем числа, накапливаем число.
# Оно в какой-то момент может стать отрицательным, но возможно не навсегда, так что
# продолжаем просто перемножать, но запомним этот момент, когда оно стало отрицательным.
# Если дойдя до конца окажется, что знак всё ещё отрицательный, то мы можем поменять его
# разделив на то запомненное произведение. Как будто отрезали часть отрезка, и в наше
# произведение попали только числа от i и до конца, а i-1 итд мы отрезали,
# чтобы поменять знак.
# Единственное, стоит обратить внимание на нули. Нули обнуляют наше произведение,
# поэтому после них приходится начинать сначала. По итогу они как бы делят массив на
# отрезки, на каждом из которых мы делаем описанное выше

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = nums[0]  # берём первое число, если оно единственное
        curr_prod = 1  # накапливаем произведение
        first_neg_prod = 1  # нужно будет запомнить момент, когда мы впервые встретили
        # отрицательное число, на случай, если мы захотим поменять знак

        for num in nums:
            curr_prod = curr_prod * num

            ans = max(
                ans,
                # Либо просто накопительное произведение, либо меняем знак и отрезаем
                # часть отрезка, ограниченного первым отрицательным числом
                max(curr_prod, curr_prod // first_neg_prod)
            )

            # Запоминаем момент, когда наше произведение впервые стало отрицательным
            if curr_prod < 0 and first_neg_prod == 1:
                first_neg_prod = curr_prod

            # Нули делят массив на отрезки, начинаем как будто сначала
            if num == 0:
                curr_prod = 1
                first_neg_prod = 1
        return ans


sol = Solution()

examples = [
    ([2,3,-2,4], 6),
    ([-2, 0, -2], 0),
    ([2, 5, 0, 5, 3, 0, 5, 1, 1, 0, 1], 15),
    ([2, 5, 0, 5, -3, 0, 5, 1, 1, 0, 1], 10),
    ([2, 5, 0, 5, 5, -3, 0, 5, 1, 1, 0, 1], 25),
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
