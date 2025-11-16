"""21. Merge Two Sorted Lists

https://leetcode.com/problems/merge-two-sorted-lists/

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list.
The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]

Constraints:
The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
"""

# Размышления
# Так как 2 списка отсортированы, head хранят наименьшие значения
# Будем сравнивать head друг с другом на каждом шагу. Меньшую пихаем в новый список и
# делаем next для неё. В итоге одна из голов рано или поздно дойдёт до None.
# Оставшиеся значения можно просто приклеить к новому списку сзади

from typing import Optional
from linked_list import LinkedList, ListNode


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
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
    

if __name__ == '__main__':
    l1 = LinkedList([1, 3, 6, 9, 10])
    l2 = LinkedList([0, 0, 1, 4, 5, 6, 8, 11])
    sol = Solution()
    res_node = sol.mergeTwoLists(l1.head, l2.head)
    print(res_node, res_node.val)
    res_list = LinkedList.from_list_nodes(res_node)
    for node in res_list:
        print(node.val)
