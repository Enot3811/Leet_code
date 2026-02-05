"""307. Range Sum Query - Mutable

https://leetcode.com/problems/range-sum-query-mutable/

Given an integer array nums, handle multiple queries of the following types:
- Update the value of an element in nums.
- Calculate the sum of the elements of nums between indices left and right inclusive
where left <= right.

Implement the NumArray class:
- NumArray(int[] nums) Initializes the object with the integer array nums.
- void update(int index, int val) Updates the value of nums[index] to be val.
- int sumRange(int left, int right) Returns the sum of the elements of nums between
indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).

Example 1:
Input
["NumArray", "sumRange", "update", "sumRange"]
[[[1, 3, 5]], [0, 2], [1, 2], [0, 2]]
Output
[null, 9, null, 8]
Explanation
NumArray numArray = new NumArray([1, 3, 5]);
numArray.sumRange(0, 2); // return 1 + 3 + 5 = 9
numArray.update(1, 2);   // nums = [1, 2, 5]
numArray.sumRange(0, 2); // return 1 + 2 + 5 = 8

Constraints:
1 <= nums.length <= 3 * 10^4
-100 <= nums[i] <= 100
0 <= index < nums.length
-100 <= val <= 100
0 <= left <= right < nums.length
At most 3 * 10^4 calls will be made to update and sumRange.
"""

# Теги
# Дерево отрезков (segment tree)

# Размышления
# В этой задаче нам потребуется структура под названием дерево отрезков.
# Префиксные суммы здесь не сработают, так как любой update,
# и нам снова всё пересчитывать.
# А дерево отрезков гарантирует, что мы можем обновиться и получить сумму за log(n).
# Пояснение к дереву:
# Изначально строим такой массив, где справа n исходных чисел,
# а слева планируются суммы
# [0,0,0,0,0,0,0,1,2,3,4,5,6,7]
# Суммы считаем как arr[i] = arr[i * 2] + arr[i * 2 + 1]
# Сначала они будут покрывать пары исходных чисел, а потом начнут пары сумм.
# [0,28,14,14,5,9,13,1,2,3,4,5,6,7]
# Нулевой элемент фиктивный, нужен просто чтобы индексы не ломались.
# Взятие же суммы более замысловатый процесс
# Например, хотим от индекса 1 до 5
# [1,|2,3,4,5,6|,7]
# Мы планируем суммировать родителей слева, но чтобы это делать надо убедиться,
# что родители не покрывают лишних чисел.
# Считаем индексы и смотрим на их чётность:
# l = n + 1 = 8; r = n + 5 = 12
# В дереве на массиве чётный элемент это всегда левый ребёнок.
# Выходит, что у 2 брат 3, они оба в диапазоне.
# А у 6 брат 7, который выходит за границы.
# Значит мы не можем прибавить их родителя, а вместо этого просто прибавим саму 6
# res += 6 = 6
# r -= 1 = 11
# После этого идём на уровень выше
# l //= 2 = 4
# r //= 2 = 5
# [0,28,14,14,|5,9|,13,1,2,3,4,5,6,7]
# 5 и 9 являются левым и правым детьми. Всё ок, можем идти на следующий уровень.
# l //= 2 = 2
# r //= 2 = 2
# [0,28,|14|,14,5,9,13,1,2,3,4,5,6,7]
# Здесь r указывает на левого ребёнка, а у него есть брат 14, который выходит за границу
# Прибавляем как на первом шаге:
# res += 14 = 20
# r -= 1 = 1
# Идём на следующий шаг
# l //= 2 = 1
# r //= 2 = 0
# И вот у нас получилось, что r левее l.
# Обобщение:
# На каждом шаге l должен быть левым ребёнком, а r правым.
# Если это не так, то прибавляем arr[l] или arr[r] и сдвигаем l или r на 1.
# Переход на следующий уровень через //2.
# Крутим это пока l <= r.

from typing import List

class NumArray:

    def __init__(self, nums: List[int]):
        self.tree = [0] * (2 * len(nums))
        self.n = len(nums)
        self.tree[self.n:] = nums
        # Заполняем суммы
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]

    def update(self, index: int, val: int) -> None:
        # Меняем элемент в листе, а затем прокидываем изменение наверх
        index = index + self.n
        diff = val - self.tree[index]
        self.tree[index] = val
        while index != 0:
            index //= 2
            self.tree[index] += diff

    def sumRange(self, left: int, right: int) -> int:
        res = 0
        left += self.n
        right += self.n
        while left <= right:
            # Должен быть чётным (левым)
            if left % 2 == 1:
                res += self.tree[left]
                left += 1
            # Должен быть нечётным (правым)
            if right % 2 == 0:
                res += self.tree[right]
                right -= 1
            
            left //= 2
            right //= 2
        return res
        
obj = NumArray([1,2,3,4,5,6,7])
print(obj.sumRange(0, 6))  # 28
print(obj.sumRange(1, 5))  # 20
print(obj.sumRange(5, 6))  # 13
print(obj.sumRange(5, 5))  # 6
obj.update(2, 10)  # 3 -> 10
print(obj.sumRange(0, 6))  # 35
obj.update(6, 0)  # 7 -> 0
print(obj.sumRange(1, 5))  # 27
print(obj.sumRange(1, 6))  # 27
