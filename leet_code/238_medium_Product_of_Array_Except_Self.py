"""238. Product of Array Except Self

https://leetcode.com/problems/product-of-array-except-self/

Given an integer array nums, return an array answer such that answer[i] is equal
to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time
and without using the division operation.

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

Constraints:
2 <= nums.length <= 10**5
-30 <= nums[i] <= 30
The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.

Follow up: Can you solve the problem in O(1) extra space complexity?
(The output array does not count as extra space for space complexity analysis.)
"""

# Размышления
# В голову сразу приходят префиксные суммы (или произведения здесь).
# Создадим массив такого же размера, как исходный, и каждому i-му элементу посчитаем
# произведение всех элементов вплоть до него.
# А потом сделаем то же самое, но уже справа-налево.
# Таким образом у нас для каждого i будет возможность взять префиксное произведение
# как i - 1 и постфиксное как i + 1, и перемножив их получим произведение всех
# элементов кроме i-го.
# Если нам необходимо обойтись без дополнительный памяти, то придётся всё это уместить
# в один массив.
# Посчитаем префиксную сумму, а суффиксную будем считать по мере вычисления ответа для
# i-го элемента.

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []
        # Считаем префиксное произведение слева направо
        for i, num in enumerate(nums):
            if i == 0:
                answer.append(num)
            else:
                answer.append(answer[-1] * num)
        # А теперь идём справа налево, но не накапливаем суффиксные произведения,
        # а сразу используем их
        curr_prod = 1
        for i in range(len(nums) - 1, -1, -1):
            if i == 0:
                answer[i] = curr_prod
            else:
                answer[i] = answer[i - 1] * curr_prod
            curr_prod *= nums[i]
        return answer


cases = [
    ([1,2,3,4], [24,12,8,6]),
    ([-1,1,0,-3,3], [0,0,9,0,0]),
    ([1,1], [1,1]),
]
sol = Solution()        
for nums, ans in cases:
    res = sol.productExceptSelf(nums)
    print(nums, res, ans)
