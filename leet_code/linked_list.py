'''
A module that contains LinkedList class.
'''


class LinkedList:
    """Linked list."""

    class ListNode:
        """Node of LinkedList."""

        def __init__(self, val: int):
            self.val = val
            self.next: LinkedList.ListNode = None
    
    def __init__(self):
        self.head: LinkedList.ListNode = None
        self.tail: LinkedList.ListNode = None
        self.length = 0

    def __len__(self):
        return self.length

    def append(self, val: int):
        """
        Append a new value to tail of list.

        Parameters
        ----------
        val : int
            Value to add.
        """
        if len(self) == 0:
            self.head = self.ListNode(val)
            self.tail = self.head
        else:
            self.tail.next = self.ListNode(val)
            self.tail = self.tail.next
        self.length += 1

    def pop(self, idx: int) -> int:
        """
        Pop the element at the given index from the list.

        Parameters
        ----------
        idx : int
            Index of element to pop.

        Returns
        -------
        int
            Value of popped element.
        """
        if idx == 0:
            popped_val = self.head.val
            self.head = self.head.next
            if len(self) == 1:
                self.tail = self.head
        else:
            current = self.head
            for _ in range(idx - 1):
                current = current.next
            if idx == len(self) - 1:
                current.next = None
                popped_val = self.tail.val
                self.tail = current
            else:
                popped_val = current.next.val
                current.next = current.next.next
        self.length -= 1
        return popped_val
