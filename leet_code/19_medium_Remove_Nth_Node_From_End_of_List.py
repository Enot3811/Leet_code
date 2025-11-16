"""19. Remove Nth Node From End of List

https://leetcode.com/problems/remove-nth-node-from-end-of-list/

Given the head of a linked list, remove the n-th node from the end of the list
and return its head.

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]
 

Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
"""


# Размышления
# Можно решить с помощью финта с медленным и быстрым указателем
# Так мы окажемся на середине списка, узнаем его длину и легко дойдём до n-го с конца.
# Но есть и другая интересная мысль:
# Запустим первый указатель на n вперёд
# Затем запустим второй и будем двигать оба указателя вперёд до тех пор, пока первый
# не дойдёт до конца.
# В этот момент второй окажется перед n-м с конца
# |1-^----| n = 5
# |--^--1-|
# |2-^--1-|
# |-2^---1|
# И удаляем его

[1, 2, 3, 4]

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(
        self, head: Optional[ListNode], n: int
    ) -> Optional[ListNode]:
        if head.next == None:
            return None
        right = head
        left = head
        for _ in range(n):
            right = right.next
        if right is None:  # Если требуется удалить голову (n = len(list))
            head = head.next
        else:
            while not right.next is None:
                right = right.next
                left = left.next
            left.next = left.next.next
        return head
