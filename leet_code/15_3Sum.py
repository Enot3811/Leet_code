"""15. 3Sum

https://leetcode.com/problems/3sum/

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.

Constraints:
3 <= nums.length <= 3000
-10**5 <= nums[i] <= 10**5
"""

# Теги
# Продолжение задачи, сдвигающиеся указатели (left-right pointers)

# Размышления
# Задача сводится к задачам two sum (1) и two sum II (167).
# Мы берём какое-то число и по сути оно становится target и мы решаем two sum.
# Единственная проблема будет в появлении дубликатов. Если в two sum нам гарантировали
# отсутствие дубликатов, то здесь они будут.
# В таком случае мы можем отсортировать массив и скипать итерации, где одно из чисел
# будет равно предыдущему.

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        for i in range(len(nums) - 2):
            # Защита от дублей у числа A
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1
            # Решаем two sum II
            while left < right:
                sum = nums[left] + nums[right] 
                if sum < -nums[i]:
                    left += 1
                elif sum > -nums[i]:
                    right -= 1
                else:
                    ans.append([nums[i], nums[left], nums[right]])
                    
                    # Нужно двинуть указатели дальше, но при этом снова защититься от
                    # дублей
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                    # Можно двинуть и правый, но по сути условия выше и сами двинут его
        return ans


sol = Solution()

examples = [
    ([-1,0,1,2,-1,-4], [[-1,-1,2],[-1,0,1]]),
    ([0,1,1], []),
    ([0,0,0], [[0,0,0]]),
    ([-3, 3, 4, -3, 1, 2], [[-3, 1, 2]])
]

[-5, -3, -1, 0, 0, 1, 2, 3, 4]
for nums, ans in examples:
    res = sol.threeSum(nums)
    print(nums, res, ans)
