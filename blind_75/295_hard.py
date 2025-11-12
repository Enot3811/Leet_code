"""295. Find Median from Data Stream

https://leetcode.com/problems/find-median-from-data-stream/

The median is the middle value in an ordered integer list.
If the size of the list is even, there is no middle value,
and the median is the mean of the two middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far.
Answers within 10-5 of the actual answer will be accepted. 

Example 1:
Input
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
Output
[null, null, null, 1.5, null, 2.0]
Explanation
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0

Constraints:
-10**5 <= num <= 10**5
There will be at least one element in the data structure before calling findMedian.
At most 5 * 10**4 calls will be made to addNum and findMedian.
 

Follow up:
If all integer numbers from the stream are in the range [0, 100],
how would you optimize your solution?
If 99% of all integer numbers from the stream are in the range [0, 100],
how would you optimize your solution?
"""

# Размышления
# Задача на структуру min/max heap
# Max heap это дерево, в котором каждый родитель больше своих детей
# При добавлении элемент пробрасывается в первый доступный лист, а затем просеивается
# вверх, если больше родителя
# В python эта структура реализована через heapq над списком, где элементы списка
# как развёрнутое построчно дерево
# Реализована только min heap, потому для max heap умножаем все элементы на -1
# Сам алгоритм заключается в отслеживании двух центральных элементов через две кучи.
# Левая - max, а правая - min. Эти две кучи должны иметь одинаковый размер или +1.
# Получаем элемент, смотрим куда его, направо или налево. Поддерживаем размеры куч.
# При извлечении медианы просто дёргаем из этих куч max и min.

import heapq

class MedianFinder:

    def __init__(self):
        self.left_heap = []
        self.right_heap = []
        

    def addNum(self, num: int) -> None:
        if len(self.left_heap) == 0 or self.left_heap[0] * -1 >= num:
            heapq.heappush(self.left_heap, num * -1)

            if len(self.left_heap) > len(self.right_heap) + 1:
                heapq.heappush(self.right_heap, heapq.heappop(self.left_heap) * -1)
        else:
            heapq.heappush(self.right_heap, num)

            if len(self.right_heap) > len(self.left_heap) + 1:
                heapq.heappush(self.left_heap, heapq.heappop(self.right_heap) * -1)
        

    def findMedian(self) -> float:
        if len(self.left_heap) == len(self.right_heap):
            return (self.left_heap[0] * -1 + self.right_heap[0]) / 2
        elif len(self.left_heap) > len(self.right_heap):
            return self.left_heap[0] * -1
        else:
            return self.right_heap[0]
        

obj = MedianFinder()
obj.addNum(0)
print(obj.findMedian())  # 0
obj.addNum(2)
print(obj.findMedian())  # 1
obj.addNum(3)
print(obj.findMedian())  # 2
obj.addNum(4)
print(obj.findMedian())  # 2.5
obj.addNum(5)
print(obj.findMedian())  # 3
obj.addNum(5)
print(obj.findMedian())  # 3.5
obj.addNum(5)
print(obj.findMedian())  # 4
obj.addNum(5)
print(obj.findMedian())  # 4.5
obj.addNum(-1)
print(obj.findMedian())  # 4
obj.addNum(-1)
print(obj.findMedian())  # 3.5
