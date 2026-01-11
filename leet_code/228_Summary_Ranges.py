"""228. Summary Ranges

https://leetcode.com/problems/summary-ranges/

You are given a sorted unique integer array nums.
A range [a,b] is the set of all integers from a to b (inclusive).

Return the smallest sorted list of ranges that cover all the numbers
in the array exactly. That is, each element of nums is covered by exactly
one of the ranges, and there is no integer x such that x is in one
of the ranges but not in nums.

Each range [a,b] in the list should be output as:
"a->b" if a != b
"a" if a == b
 
Example 1:
Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"

Example 2:
Input: nums = [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: The ranges are:
[0,0] --> "0"
[2,4] --> "2->4"
[6,6] --> "6"
[8,9] --> "8->9"

Constraints:
0 <= nums.length <= 20
-2^31 <= nums[i] <= 2^31 - 1
All the values of nums are unique.
nums is sorted in ascending order.
"""

# Теги
# Просто лёгкая задача (Easy task)

# Размышления
# Проходим по массиву, смотрим, что текущее число на 1 больше предыдущего.
# Следим, что начало интервала и его конец не равны, ведь тогда обозначение другое.

class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        if len(nums) == 0:
            return []
        st_num = nums[0]
        end_num = nums[0]
        answer = []
        for i in range(1, len(nums)):
            # Если текущее число продолжает диапазон
            if nums[i] - end_num == 1:
                end_num = nums[i]
            # Если диапазон закончился
            else:
                if st_num == end_num:
                    answer.append(str(st_num))
                else:
                    answer.append(f'{st_num}->{end_num}')
                st_num = end_num = nums[i]
        else:
            if st_num == end_num:
                answer.append(str(st_num))
            else:
                answer.append(f'{st_num}->{end_num}')
        return answer


examples = [
    ([0,1,2,4,5,7], ["0->2","4->5","7"]),
    ([0,2,3,4,6,8,9], ["0","2->4","6","8->9"]),
    ([0,1,2,3,4,5,6,7,8,9,10], ['0->10']),
    ([0,2,4,6,8,10], ['0','2','4','6','8','10']),
    ([0,1,2,4,5,7,8,10,12,15,17,18,19,20],
     ['0->2','4->5','7->8','10','12','15','17->20']),
    ([], [])
]

sol = Solution()

for inp, ans in examples:
    out = sol.summaryRanges(inp)
    print(inp, out, ans)
