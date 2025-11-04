"""143. Reorder List

Check the images!
https://leetcode.com/problems/reorder-list/

You are given the head of a singly linked-list. The list can be represented as:
L0 → L1 → … → Ln - 1 → Ln

Reorder the list to be on the following form:
L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …

You may not modify the values in the list's nodes. Only nodes themselves may be changed.

Example 1:
Input: head = [1,2,3,4]
Output: [1,4,2,3]

Example 2:
Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]

Constraints:
The number of nodes in the list is in the range [1, 5 * 10**4].
1 <= Node.val <= 1000
"""

# Размышления
# Проблема задачи в том, что мы берём последний элемент,
# и уже не можем взять предпоследний из-за прямой связи.
# Что если просто взять и сделать реверс во второй части списка?
# А дальше в задаче есть несколько финтов, который полезно наловчится реализовывать.
# Например, как найти середину списка без лишних прогонов?
# Использовать быстрый и медленные указатели.
# Как потом делать реверс через 3 указателя и как потом смешивать две половины
# с помощью пинг-понг реализации



from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def print_list(self, head: ListNode):
        while head is not None:
            print(head.val, end=' ')
            head = head.next
        print()

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Ищем середину списка с помощью быстрого и медленного указателя
        # Ставим медленный указатель на нулевую позицию, а быстрый на первую
        # Когда быстрый достигнет конца, медленный будет на середине
        slow = head
        fast = head.next
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        self.print_list(slow)

        # Переворачиваем вторую часть списка
        curr = slow.next
        prev = None
        slow.next = None
        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        # Смешиваем две части
        curr1 = head
        curr2 = prev
        while curr2 is not None:
            next = curr1.next
            curr1.next = curr2
            curr1 = curr2
            curr2 = next
