"""42. Trapping Rain Water

Check the image!
https://leetcode.com/problems/trapping-rain-water/

Given n non-negative integers representing an elevation map where the width of each bar
is 1, compute how much water it can trap after raining.

Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9

Constraints:
n == height.length
1 <= n <= 2 * 10**4
0 <= height[i] <= 10**5
"""

# Теги
# Сдвигающиеся указатели (left-right pointers)

# Размышления
# Задача не очень сложная, но всё равно обманывает своей простотой.
# Линейно проходим, держа в памяти высокий дом позади, пытаясь найти ему пару,
# которая больше, либо равна.
# Но если вдруг мы наткнёмся на дом, который выше всей правой части массива,
# то просто уйдём с нулём.
# Потому на ум приходит идея с двумя проходами: слева-направо и справа-налево,
# и результаты потом совместить.
# И в целом так можно решить, но есть проблема дублей,
# когда прибавим диапазон в обоих проходах, и потому приходится использовать
# окололинейную память.
# Но есть решение менее интуитивное, но как раз без памяти и всего с 1 прогоном.
# Используем сдвигающиеся указатели.
# Двигаем тот указатель, который меньше.
# Так гарантируем, что супер высокий столбик обработается лишь после того,
# как найдётся кто-то повыше него.
# А если нет, то просто посчитаем все диапазоны до него слева и справа.

from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        left_max = 0
        right_max = 0
        left = 0
        right = len(height) - 1
        total_sum = 0
        while left < right:
            if height[left] < height[right]:
                # Если обновляем максимум, то в сумму пойдёт 0.
                left_max = max(left_max, height[left])
                # Если максимум не обновится, то в сумму пойдёт разность.
                # В итоге вместо кумулятивной суммы просто сразу кидаем в ответ.
                total_sum += left_max - height[left]
                left += 1
            else:
                right_max = max(right_max, height[right])
                total_sum += right_max - height[right]
                right -= 1
        return total_sum

cases = [
    ([4,2,0,3,2,5], 9),
    ([0,1,0,2,1,0,1,3,2,1,2,1], 6),
    ([5,1,2,1,4],8),
    ([5,1,2,1,4,1,2],9),
    ([2,0,5,0,2,0,2],6),
    ([2,0,5,0,1,0,2],7),
    ([1,0,1,0,1],2),
    ([5,2,0,2],2),
    ([1,2,3,2,1,1,2,3,4],6),
    ([0,0,0,0],0),
    ([1,2,3],0),
    ([1,0,1,5,0,4,0,3],8)
]
sol = Solution()
for height, ans in cases:
    res = sol.trap(height)
    print(height, res, ans)
