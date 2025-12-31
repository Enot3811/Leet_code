"""46. Permutations

https://leetcode.com/problems/permutations/

Given an array nums of distinct integers,
return all the possible permutations. You can return the answer in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:
Input: nums = [0,1]
Output: [[0,1],[1,0]]

Example 3:
Input: nums = [1]
Output: [[1]]

Constraints:
1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.
"""

# Теги
# Поиск в глубину (dfs)

# Размышления
# Сразу хочется применить dfs.
# У нас есть текущая позиция и пул чисел. Берём какое-то из чисел для текущей позиции и
# решаем задачу для следующей позиции из оставшихся чисел.
# Интересен момент, как не плодить кучу списков во время решения.
# Эту задачу можно решать in-place методом.
# То есть будем ставить одно из чисел на текущую позицию прямо в исходном массиве.
# А затем, когда прорешали dfs для этого варианта, возвращаем обратно, как было.

from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def dfs(locked: int):
            # Слева от locked числа, которые мы уже зафиксировали,
            # они пойдут в текущий ответ.
            # Сам locked указывает на позицию,
            # на место которой мы будем перебирать числа

            if locked == len(nums):
                ans.append(nums[:])

            for i in range(locked, len(nums)):
                # Перебираем все оставшиеся числа, ставим их на locked и продолжаем
                nums[locked], nums[i] = nums[i], nums[locked]
                dfs(locked + 1)
                nums[locked], nums[i] = nums[i], nums[locked]
        dfs(0)
        return ans


if __name__ == '__main__':
    nums = [1, 2, 3]
    sol = Solution()
    print(sol.permute(nums))
