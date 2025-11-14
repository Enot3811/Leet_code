"""Merge k Sorted Lists.

https://leetcode.com/problems/merge-k-sorted-lists/

You are given an array of k linked-lists lists,
each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.


Example 1:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

Example 2:
Input: lists = []
Output: []

Example 3:
Input: lists = [[]]
Output: []

Constraints:
k == lists.length
0 <= k <= 10**4
0 <= lists[i].length <= 500
-10**4 <= lists[i][j] <= 10**4
lists[i] is sorted in ascending order.
The sum of lists[i].length will not exceed 10**4.
"""

# Размышления
# Так или иначе эта задача сводится к слитию двух списков (task 21),
# что даст сложность n * k. Однако то, как мы будем сливать списки, может дать буст.
# Допустим у нас 8 списков с размером n. Мы начинаем сливать их подряд и получаем
# 1 + 2: размер и работа 2n
# 1 + 3: размер и работа 3n
# 1 + 4: размер и работа 4n
# ...
# (2 + 3 + 4 + 5 + 6 + 7 + 8) = 35n
# Но если сливать их как при merge sort, попарно, то получится
# 2 + 2 + 2 + 2 + 4 + 4 + 8 = 24n
# И при увеличении количества списков разница будет расти.
# Если более конкретно, то в первом случае наблюдается арифметическая прогрессия.
# Можем вспомнить формулу суммы членов арифметической прогрессии: k * (k + 1) / 2
# раскрыв скобки получаем: (k^2 + k) / 2
# И при оценке сложности мы убираем всю мишуру и получаем k^2
# То есть грубо говоря разница между k^2 * n и log(k) * n

from typing import Optional, List
from linked_list import ListNode

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        for i in range(len(lists) - 1, -1, -1):
            if not type(lists[i]) is ListNode:
                lists.pop(i)
        if len(lists) == 0:
            return None
        while len(lists) > 1:
            l1 = lists.pop(0)
            l2 = lists.pop(0)
            merged = self.mergeTwoLists(l1, l2)
            lists.append(merged)
        return lists[0]

    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        
        if list1.val < list2.val:
            head = list1
            list1 = list1.next
        else:
            head = list2
            list2 = list2.next
        tail = head

        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        if list1 is not None:
            tail.next = list1
        else:
            tail.next = list2
        return head
        