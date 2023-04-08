"""Sort List."""


from typing import Optional, List, Union


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self, iterable: Optional[List[int]] = None) -> None:
        self.head = None
        self.tail = None
        if iterable:
            for i in iterable:
                self.append(i)

    def append(self, elem: Union[int, ListNode]):
        if isinstance(elem, int):
            node = ListNode(elem)
        else:
            node = elem
        if self.head is None:
            self.head = node
            self.tail = self.head
        else:
            self.tail.next = node
            self.tail = self.tail.next

    def to_list(self) -> List[int]:
        normal_list = []
        cur = self.head
        while cur is not None:
            normal_list.append(cur.val)
            cur = cur.next
        return normal_list


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sub_len = 1
        cur_head = head
        first_part = LinkedList()
        second_part = LinkedList()
        first_full = False
        second_full = False

        current_node = head
        counter = 0
        while current_node:
            # Смотрим в какой кидать
            if not first_full:
                first_part.append(current_node)
            elif not second_full:
                second_part.append(current_node)
            else:
                raise
            counter += 1
            # Смотрим не переполнился ли
            if counter == sub_len:
                if not first_full:
                    first_full = True
                elif not second_full:
                    second_full = True
                else:
                    raise
            # Сливаем, если оба переполнились
            if first_full and second_full:
                # Слияние здесь
                pass
            current_node = current_node.next
            
                


sol = Solution()
l = LinkedList([4, 5, 1, 2, 7])
print(l.to_list())
