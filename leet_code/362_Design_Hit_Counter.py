"""362. Design Hit Counter

Premium lock.
https://leetcode.doocs.org/en/lc/362/

Design a hit counter which counts the number of hits received in the past 5 minutes
(i.e., the past 300 seconds).

Your system should accept a timestamp parameter (in seconds granularity),
and you may assume that calls are being made to the system in chronological order
(i.e., timestamp is monotonically increasing).
Several hits may arrive roughly at the same time.

Implement the HitCounter class:
- HitCounter() Initializes the object of the hit counter system.
- void hit(int timestamp) Records a hit that happened at timestamp (in seconds).
Several hits may happen at the same timestamp.
- int getHits(int timestamp) Returns the number of hits in the past 5 minutes
from timestamp (i.e., the past 300 seconds).

Example:
Input
["HitCounter", "hit", "hit", "hit", "getHits", "hit", "getHits", "getHits"]
[[], [1], [2], [3], [4], [300], [300], [301]]
Output
[null, null, null, null, 3, null, 4, 3]

Explanation
HitCounter hitCounter = new HitCounter();
hitCounter.hit(1);       // hit at timestamp 1.
hitCounter.hit(2);       // hit at timestamp 2.
hitCounter.hit(3);       // hit at timestamp 3.
hitCounter.getHits(4);   // get hits at timestamp 4, return 3.
hitCounter.hit(300);     // hit at timestamp 300.
hitCounter.getHits(300); // get hits at timestamp 300, return 4.
hitCounter.getHits(301); // get hits at timestamp 301, return 3.
"""

# Теги
# Бинарный поиск (binary search)

# Размышления
# Задача путает своей простотой, но на самом деле имеет некоторые подводные камни.
# Делать преподсчёт для получаемых timestamp с помощью sliding window не получится,
# так как getHits может включать в себя несуществующие timestamp,
# для которых мы не посчитали накопленные хиты за 300 секунд.
# А раз за O(1) не получается, то можем просто воспользоваться бинарным поиском,
# найдя обе границы диапазона.
# И здесь есть ещё одно уточнение, которое скрывается в условиях задачи.
# Аргумент timestamp всегда монотонно возрастающий.
# То есть не может быть такого, что getHits попросит timestamp из прошлого.
# В таком случае мы можем не искать индекс для timestamp, а просто взять len.

import bisect

class HitCounter:
    def __init__(self):
        self.hits = []

    def hit(self, timestamp: int):
        self.hits.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        # return (bisect.bisect_right(self.hits, timestamp) - 
        #         bisect.bisect_right(self.hits, timestamp - 300))
        return len(self.hits) - bisect.bisect_right(self.ts, timestamp - 300)


obj = HitCounter()
obj.hit(1)
obj.hit(1)
obj.hit(2)
obj.hit(3)
print(obj.getHits(3))
obj.hit(300)
print(obj.getHits(300))
print(obj.getHits(301))
print(obj.getHits(302))