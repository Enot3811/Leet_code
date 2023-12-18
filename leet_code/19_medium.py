"""Remove Nth Node From End of List.

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


from typing import Optional
from linked_list import LinkedList, ListNode


class Solution:
    def removeNthFromEnd(
        self, head: Optional[ListNode], n: int
    ) -> Optional[ListNode]:
        if head.next == None:
            return None
        right = head
        left = head
        for i in range(n):
            right = right.next
        if right is None:
            head = head.next
        else:
            while not right.next is None:
                right = right.next
                left = left.next
            left.next = left.next.next
        return head
