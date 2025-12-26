"""4. Median of two sorted arrays

https://leetcode.com/problems/median-of-two-sorted-arrays/

Given two sorted arrays nums1 and nums2 of size m and n respectively,
return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

Constraints:
nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-10**6 <= nums1[i], nums2[i] <= 10**6
"""

# Теги
# Бинарный поиск (binary search)

# Размышления
# Очень сложный алгоритм, который можно разве что запомнить.
# Общая интуиция в том, что мы можем резать два массива разными способами,
# но сумма длин левых частей и правых должны быть равны, раз это медиана.
# nums1: [ ... L1 ... ] | [ ... R1 ... ] (разрез после индекса i)
# nums2: [ ... L2 ... ] | [ ... R2 ... ] (разрез после индекса j)
# количество_элементов_из_1 + количество_элементов_из_2 = half
# j = half - i
# Как мы проверяем, что разрез проведён верно?
# Нужно проверить, что самый большой элемент левой части меньше самого малого правой,
# То есть, если L1 <= R2 и L2 <= r1, то разбиение правильное.
# Если же L1 > R2, то нужно уменьшить левую часть L1,
# так как она уже содержит большие числа.
# А если L2 > R1, то наоборот, нужно увеличить левую часть L1,
# так как там всё ещё слишком малые числа.
# И данный процесс можно ускорить с помощью бинарного поиска.

from typing import List

class Solution():
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
            
        m, n = len(nums1), len(nums2)
        total_len = m + n
        # half_len - сколько элементов должно быть в левой части
        # (total_len + 1) // 2 работает и для четных, и для нечетных корректно
        half_len = (total_len + 1) // 2
        
        l, r = 0, m
        
        while l <= r:
            # i - это РАЗРЕЗ (сколько элементов берем из nums1)
            # i может быть от 0 до m
            i = (l + r) // 2
            # j - сколько элементов берем из nums2, чтобы в сумме было half_len
            j = half_len - i
            
            # Элементы вокруг разреза
            # Если i == 0, значит слева от разреза в nums1 ничего нет -> -inf
            nums1_left = nums1[i - 1] if i > 0 else float('-inf')
            # Если i == m, значит справа от разреза в nums1 ничего нет -> inf
            nums1_right = nums1[i] if i < m else float('inf')
            
            nums2_left = nums2[j - 1] if j > 0 else float('-inf')
            nums2_right = nums2[j] if j < n else float('inf')
            
            # Проверяем условие правильного разреза:
            # Все слева должны быть <= всем справа
            if nums1_left <= nums2_right and nums2_left <= nums1_right:
                # Нашли!
                if total_len % 2 == 1:
                    # Если нечетное, медиана - это максимум из левой части
                    return max(nums1_left, nums2_left)
                else:
                    # Если четное, среднее между макс. слева и мин. справа
                    return (max(nums1_left, nums2_left) + min(nums1_right, nums2_right)) / 2
            
            elif nums1_left > nums2_right:
                # Мы взяли слишком много из nums1 (его левый элемент слишком большой)
                # Сдвигаем разрез влево
                r = i - 1
            else:
                # Мы взяли слишком мало из nums1 (его правый элемент слишком маленький, 
                # либо nums2_left слишком большой)
                l = i + 1


cases = [
    (([1,2,3,4,5,6,7,8],[1,2,3,4,5]), 4),
    (([1,4,5,7,9],[3,5,8]), 5),
    (([1,2,3,4,5,6],[10,11,12]), 5),
    (([1,3,6,8,9],[2,4,5]), 4.5),
    (([1,2,4,6,7,9,10,11,14],[9,12,13]), 9),
    (([1,2,3,4,5,6,7],[7,8,9,10,11,12]), 7)
]
sol = Solution()
for inp, ans in cases:
    res = sol.findMedianSortedArrays(*inp)
    print(inp, res, ans)
