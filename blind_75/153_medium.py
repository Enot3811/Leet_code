"""153. Find Minimum in Rotated Sorted Array

https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

Suppose an array of length n sorted in ascending order is rotated between 1 and n times.
For example, the array nums = [0,1,2,4,5,6,7] might become:
[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.

Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results
in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements,
return the minimum element of this array.

You must write an algorithm that runs in O(log n) time. 

Example 1:
Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.

Example 2:
Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.

Example 3:
Input: nums = [11,13,15,17]
Output: 11
Explanation: The original array was [11,13,15,17] and it was rotated 4 times. 

Constraints:
n == nums.length
1 <= n <= 5000
-5000 <= nums[i] <= 5000
All the integers of nums are unique.
nums is sorted and rotated between 1 and n times.
"""

# Размышления
# Указание сложности в log(n) сразу наталкивает на бинарный поиск, или на саму идею
# разделения массива на 2 части.
# А далее необходимо определиться, что мы вообще ищем, и на что хотели бы смотреть
# в поисках.
# Полученная половина может быть отсортированной (смотрим на начало и конец), или нет.
# Если нет, то разрез должен быть где-то внутри, и тогда надо делить её ещё раз
# и повторить для её половинок.
# Если же массив отсортирован, то его копать нет смысла.
# Стоит только заметить, что мы можем попасть при разделении так, что обе половины
# будут отсортированы. В таком случае имеет смысл вообще каждый раз сравнивать первый
# элемент и текущий минимум.
# Когда половинка выродится в один элемент, считаем, что это отсортированная часть,
# то есть просто сравниваем с минимумом.


from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        stack = [(0, len(nums) - 1)]
        min_num = nums[0]
        while len(stack) != 0:
            st, end = stack.pop()
            if nums[st] <= nums[end]:
                min_num = min(min_num, nums[st])
            else:
                mid = (st + end) // 2
                stack.append((st, mid))
                stack.append((mid + 1, end))
        return min_num


sol = Solution()

examples = [
    ([3,4,5,1,2], 1),
    ([4,5,6,7,0,1,2], 0),
    ([11,13,15,17], 11),
    ([1], 1),
    ([4,5,6,7,8,9,1,2,3], 1),
    ([7, 4, 5, 6], 4),
    ([6,7,8,9,10,11,12,13,14,15,1,2,3,4,5], 1)
]
for nums, ans in examples:
    res = sol.findMin(nums)
    print(nums, res, ans)
