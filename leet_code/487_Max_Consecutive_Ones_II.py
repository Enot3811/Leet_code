"""Max Consecutive Ones II

Premium lock
https://leetcode.doocs.org/en/lc/487/

Given a binary array nums, return the maximum number of consecutive 1's in the array
if you can flip at most one 0.

Example 1:
Input: nums = [1,0,1,1,0]
Output: 4
Explanation: 
- If we flip the first zero, nums becomes [1,1,1,1,0] and we have 4 consecutive ones.
- If we flip the second zero, nums becomes [1,0,1,1,1] and we have 3 consecutive ones.
The max number of consecutive ones is 4.

Example 2:
Input: nums = [1,0,1,1,0,1]
Output: 4
Explanation: 
- If we flip the first zero, nums becomes [1,1,1,1,0,1] and we have 4 consecutive ones.
- If we flip the second zero, nums becomes [1,0,1,1,1,1] and we have 4 consecutive ones.
The max number of consecutive ones is 4.

Constraints:
1 <= nums.length <= 10^5
nums[i] is either 0 or 1.

Follow up: What if the input numbers come in one by one as an infinite stream?
In other words, you can't store all numbers coming from the stream
as it's too large to hold in memory. Could you solve it efficiently?
"""

# Теги
# Плавающее окно (left-right pointers)

# Размышления
# Ещё одна задача из семейства Max Consecutive Ones (1004 3-я задача).
# Легко решается с помощью sliding window с двумя указателями (2-е решение),
# но здесь предлагается оптимизировать решение под поток.
# То есть left уже не сможет идти по числам, сужая окно.
# Тогда просто будем считать текущий сегмент единиц и запоминать предыдущий.
# Ведь flip всего 1, то есть сегментов будет всего 2.
# Получается, когда находим 0, то perv + curr, prev = curr, curr = 0

from typing import List

# Оптимизированное решение. Сложность n
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        prev_seg = 0
        cur_seg = 0
        max_len = 0
        used_flip = False
        for num in nums:
            if num == 0:
                used_flip = True
                max_len = max(max_len, cur_seg + prev_seg + (1 if used_flip else 0))
                prev_seg = cur_seg
                cur_seg = 0
            else:
                cur_seg += 1
        max_len = max(max_len, cur_seg + prev_seg + (1 if used_flip else 0))
        return max_len

# Классический sliding window подход. Сложность 2n
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        left = 0
        used_flip = False
        max_len = 0
        for right, num in enumerate(nums):
            if num == 0:
                if not used_flip:
                    used_flip = True
                else:
                    max_len = max(max_len, right - left)
                    # Двигаем левую границ до первого нуля и перешагиваем его
                    while left <= right:
                        if nums[left] == 0:
                            left += 1
                            break
                        left += 1
                        
        max_len = max(max_len, right - left + 1)
        return max_len


cases = [
    ([1,0,1,1,0], 4),
    ([0,1,1,1,0,0], 4),
    ([1,0,1,0,0,1,1,1], 4),
    ([1], 1),
    ([0], 1),
    ([0,0], 1),
    ([1,0], 2),
]
sol = Solution()
for nums, ans in cases:
    res = sol.findMaxConsecutiveOnes(nums)
    print(nums, res, ans)
                