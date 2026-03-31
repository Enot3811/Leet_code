"""2. Add Two Numbers

Check the images!
https://leetcode.com/problems/add-two-numbers/

You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero,
except the number 0 itself.

Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

Constraints:
The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
"""

# Теги
# Связанный список (Linked list)

# Размышления
# Описание задачи и имеющиеся примеры могут сбить с толку.
# Может показаться, что исходные списки идут от старшего разряда к младшему,
# однако они уже в нужном нам виде.
# Проходим по спискам одновременно, складываем разряды от младшего к старшему,
# откладываем переполнение через 10 в отдельную переменную на следующую итерацию.
# Для удобства создания нового списка можем воспользоваться dummy_head,
# чтобы не делать уникальную итерацию для первого сложения.
# В конце просто вернём dummy_head.next

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        additional_add = 0
        dummy_head = ListNode()
        curr_node = dummy_head
        while l1 is not None and l2 is not None or additional_add != 0:
            if l1:
                num1 = l1.val
                l1 = l1.next
            else:
                num1 = 0
            if l2:
                num2 = l2.val
                l2 = l2.next
            else:
                num2 = 0
            curr_sum = num1 + num2 + additional_add
            additional_add = curr_sum // 10
            curr_sum %= 10
            
            # Без dummy_head здесь бы пришлось делать условие для head==None
            curr_node.next = ListNode(curr_sum)
            curr_node = curr_node.next

        # Остаток списка просто присоединяем
        if l1 is not None:
            curr_node.next = l1
        elif l2 is not None:
            curr_node.next = l2

        return dummy_head.next
