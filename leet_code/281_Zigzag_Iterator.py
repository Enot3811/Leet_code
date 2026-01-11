"""281. Zigzag Iterator

Premium lock.
https://leetcode.doocs.org/en/lc/281/

Given two vectors of integers v1 and v2,
implement an iterator to return their elements alternately.

Implement the ZigzagIterator class:
- ZigzagIterator(List<int> v1, List<int> v2) initializes the object
with the two vectors v1 and v2.
- boolean hasNext() returns true if the iterator still has elements,
and false otherwise.
- int next() returns the current element of the iterator
and moves the iterator to the next element.

Example 1:
Input: v1 = [1,2], v2 = [3,4,5,6]
Output: [1,3,2,4,5,6]
Explanation: By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,3,2,4,5,6].

Example 2:
Input: v1 = [1], v2 = []
Output: [1]

Example 3:
Input: v1 = [], v2 = [1]
Output: [1]

Constraints:
0 <= v1.length, v2.length <= 1000
1 <= v1.length + v2.length <= 2000
-2^31 <= v1[i], v2[i] <= 2^31 - 1

Follow up: What if you are given k vectors?
How well can your code be extended to such cases?

Clarification for the follow-up question:
The "Zigzag" order is not clearly defined and is ambiguous for k > 2 cases.
If "Zigzag" does not look right to you, replace "Zigzag" with "Cyclic".

Follow-up Example:
Input: v1 = [1,2,3], v2 = [4,5,6,7], v3 = [8,9]
Output: [1,4,8,2,5,9,3,6,7]
"""

# Теги
# Очередь (queue)

# Размышления
# Может прийти мысль с сортировкой по длине, и отсекать векторы, которые закончились,
# но это нарушит исходный порядок векторов.
# Намного интереснее подход с очередью.
# Мы сохраним порядок векторов, а отсекать ли вектор будем решать в сам момент,
# когда его достаём из очереди.
# Если в векторе не закончились элементы, то просто снова пихаем его в очередь.
# Если же всё, то больше не добавляем.
# Далее уже детали реализации.
# Самый простой подход - пушить вектор с его текущим индексом.
# Так легко отслеживать, что вектор закончился.
# Но можно и заморочиться, чтобы не пушить индексы, ведь у всех векторов на одном
# обороте они всё равно будут одинаковые.

from typing import List
from collections import deque

class ZigzagIterator:
    def __init__(self, vectors: List[List[int]]):
        # Добавляем только непустые веторы
        self.queue = deque()
        for vec in vectors:
            if len(vec) > 0:
                self.queue.append(vec)
        self.vec_idx = 0  # Индекс текущего вектора, чтобы отследить полный оборот
        self.curr_idx = 0  # Индекс элементов, что достаём из вектора
        self.num_vecs = len(vectors)  # Сколько векторов ещё итерируются

    def __iter__(self):
        return self

    def __next__(self) -> int:
        if self.queue:
            # Если сделали оборот
            if self.vec_idx == self.num_vecs:
                self.vec_idx = 0
                self.curr_idx += 1  # берём следующий индекс

            vec = self.queue.popleft()
            # Если это не последний элемент, то закидываем его снова
            if self.curr_idx < len(vec) - 1:
                self.queue.append(vec)
                self.vec_idx += 1
            else:
                self.num_vecs -= 1
            return vec[self.curr_idx]
        else:
            raise StopIteration()


cases = [
    ([[1,1,1], [2,2,2], [3,3,3,3], [4,4,4,4,4]], [1,2,3,4,1,2,3,4,1,2,3,4,3,4,4]),
    ([[1,1], [2,2]], [1,2,1,2]),
    ([[1],[2],[3],[4],[5]], [1,2,3,4,5]),
    ([[1,1],[2],[3],[4],[5]], [1,2,3,4,5,1]),
]
for vectors, ans in cases:
    iterator = ZigzagIterator(vectors)
    res = [num for num in iterator]
    print(vectors, res, ans)
        