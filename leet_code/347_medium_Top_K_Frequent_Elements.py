"""347. Top K Frequent Elements

https://leetcode.com/problems/top-k-frequent-elements/

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order. 

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]

Example 3:
Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2
Output: [1,2]

Constraints:
1 <= nums.length <= 10**5
-10**4 <= nums[i] <= 10**4
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""

# Размышления
# Данную задачу сразу можно решить с помощью сортировки и проходу по массиву.
# Получится nlog(n) сложность. Однако предлагается ускорить решение.
# 1) Подход, который пришёл в голову, это counter + min_heap
# Посчитаем все элементы, а затем, чтобы отобрать k самых частых, будем поддерживать
# дерево на k элементов, где каждый элемент (частота, число).
# Таким образом у нас всегда будет в лёгком доступе наименее частый из самых частых,
# а дерево позволит актуализировать коллекцию за log(k).
# Итого сложность n + mlog(k), где m - количество уникальных элементов.
# По памяти: m + log(k)

from typing import List
from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        min_heap = []
        for key, val in counter.items():
            if len(min_heap) < k:
                heapq.heappush(min_heap, (val, key))
            elif min_heap[0][0] < val:
                heapq.heappushpop(min_heap, (val, key))
        return list(map(lambda x: x[1], min_heap))


# 2) Более оптимальное решение использует алгоритм bucket sort.
# Мы создаём массив длиной n, где индекс - это частота элемента,
# а сам элемент - список чисел с такой частотой.
# Таким образом получим и вовсе линейную сложность.
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        
        freq = [[] for _ in range(len(nums) + 1)]
        
        for num, count in count.items():
            freq[count].append(num)
            
        res = []
        # Идем с конца массива (от максимальной возможной частоты) к 0
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

sol = Solution()
cases = [
    (([1,1,1,2,2,3], 2), [1,2]),
    (([1,2,1,2,1,2,3,1,3,2], 2), [1,2]),
    (([1], 1), [1])
]
for inp, ans in cases:
    res = sol.topKFrequent(*inp)
    print(inp, res, ans)
