"""11. Container with most water

Check the image!
https://leetcode.com/problems/container-with-most-water/description/

You are given an integer array height of length n.
There are n vertical lines drawn such
that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container,
such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7].
In this case, the max area of water (blue section) the container can contain is 49.

Example 2:
Input: height = [1,1]
Output: 1

Constraints:
n == height.length
2 <= n <= 10^5
0 <= height[i] <= 10^4
"""


# Размышления
# Не интуитивная идея, которую я подсмотрел
# Возьмём 2 указателя по краям массива. Посчитаем значение площади между указателями.
# Двинем ближе к центру тот, который стоит на менее высоком столбике.
# Таким образом ширина будет уменьшаться, но есть шанс, что мы наткнёмся на пару высоких
# столбиков, которые за счёт высоты дадут большую площадь

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0
        while left < right:
            current_area = min(height[left], height[right]) * (right - left)
            max_area = max(current_area, max_area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area


sol = Solution()

examples = [
    ([1,8,6,2,5,4,8,3,7], 49),
    ([1, 1], 1),
]
for height, ans in examples:
    res = sol.maxArea(height)
    print(height, res, ans)
        