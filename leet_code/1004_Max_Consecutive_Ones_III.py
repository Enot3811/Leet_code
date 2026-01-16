"""1004. Max Consecutive Ones III

Given a binary array nums and an integer k,
return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

Example 1:
Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

Example 2:
Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

Constraints:
1 <= nums.length <= 10^5
nums[i] is either 0 or 1.
0 <= k <= nums.length
"""

# Теги
# Плавающее окно (left-right pointers)

# Размышления
# Типичная задача на плавающее окно.
# Пытаемся расширить текущую последовательность за счёт k.
# Когда k < 0, мы израсходовали все заряды, нужно сужать окно, чтобы вернуть 1 заряд.

from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        ans = 0
        for right, num in enumerate(nums):
            if num == 0:
                k -= 1
                # Ловим < 0, так как k и по умолчанию может быть 0
                if k < 0:
                    # 1 не прибавляем, так как текущий right уже лишний
                    ans = max(ans, right - left)
                while k < 0:
                    if nums[left] == 0:
                        k += 1
                    left += 1
        ans = max(ans, right - left + 1)
        return ans

cases = [
    (([1,1,1,0,0,1,1], 2), 7),
    (([1,1,1,0,0,1,1,1,0], 1), 4),
    (([1,1,1,0,0,1,1,1,1], 1), 5),
    (([1,1,1,0,0,1,1], 1), 4),
    (([1,1,1,0,0,1,1], 0), 3),
    (([1,1,1,1,1], 0), 5),
    (([1,1,1,1,1], 1), 5),
    (([0,1,1,1,1,1], 1), 6),
    (([0,1,1,1,0,0,1,1], 0), 3),
    (([0,0,0], 1), 1),
    (([0,0,0], 5), 3),
]
sol = Solution()
for inp, ans in cases:
    res = sol.longestOnes(*inp)
    print(inp, res, ans)
