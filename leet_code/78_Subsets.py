"""78. Subsets

https://leetcode.com/problems/subsets/

Given an integer array nums of unique elements, return all possible 
subsets (the power set).

The solution set must not contain duplicate subsets.
Return the solution in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:
Input: nums = [0]
Output: [[],[0]]

Constraints:
1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique.
"""

# Теги
# Поиск в глубину (dfs)

# Размышления
# Задачу можно решить через dfs.
# Вести текущий список и на каждом шаге добавлять по очереди числа от текущего до конца.
# В итоге будет 1, 12, 123, 13, 2, 23, 3 через рекурсию и возвраты.
# Но есть очень интересный способ решить без рекурсии.
# Проходим по числам. Первое число просто добавляем в ответ.
# А начиная со второго добавляем и проходим по всем ранее добавленным элементам и
# присоединяем текущее число к ним.
# Получается 1, 2, 12, 3, 13, 23, 123

from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = []
        for number in nums:
            answer.append([number])
            # Начиная со второго, перебираем прошлые и прибавляем к ним текущее.
            if len(answer) >= 2:
                last = len(answer) - 1
                for i in range(last):
                    answer.append(answer[i] + answer[last])
        answer.append([])
        return answer

if __name__ == '__main__':
    sol = Solution()
    print(sol.subsets([1, 2, 3, 4]))
