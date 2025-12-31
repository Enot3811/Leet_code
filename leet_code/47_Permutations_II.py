"""47. Permutations II

https://leetcode.com/problems/permutations-ii/

Given a collection of numbers, nums, that might contain duplicates,
return all possible unique permutations in any order. 

Example 1:
Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]

Example 2:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Constraints:
1 <= nums.length <= 8
-10 <= nums[i] <= 10
"""

# Теги
# Поиск в глубину (dfs), Продолжение задачи

# Размышления
# Задача является продолжением задачи (46. Permutations), и по сути имеет точно такое же
# решение.
# Единственное, требуется избежать дубликатов,
# а для этого нам нужно избежать использования повторяющихся чисел.
# Добавим на каждом шаге set, который запомнит, какие числа мы уже использовали.

from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def dfs(locked: int):
            if locked == len(nums):
                ans.append(nums[:])

            # Добавим set чисел, которые уже использовали
            used = set()
            for i in range(locked, len(nums)):
                if nums[i] not in used:
                    # Запоминаем число, которое уже использовали, чтобы избежать дублей
                    used.add(nums[i])
                    nums[locked], nums[i] = nums[i], nums[locked]
                    dfs(locked + 1)
                    nums[locked], nums[i] = nums[i], nums[locked]
        dfs(0)
        return ans
    

if __name__ == '__main__':
    sol = Solution()
    nums = [1, 1, 2, 2, 3]
    print(sol.permuteUnique(nums))
