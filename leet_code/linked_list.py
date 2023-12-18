"""A module that contains LinkedList class."""

from typing import Iterable, Any, Optional


class ListNode:
    """Node of LinkedList."""

    def __init__(self, val: int):
        self.val = val
        self.next: LinkedList = None


class LinkedList:
    """Linked list."""
    
    def __init__(self, initial_values: Optional[Iterable[Any]] = None):
        self.head: ListNode = None
        self.tail: ListNode = None
        self.length = 0

        if initial_values:
            for i, val in enumerate(initial_values):
                if i == 0:
                    self.head = ListNode(val)
                    self.tail = self.head
                else:
                    self.tail.next = ListNode(val)
                    self.tail = self.tail.next
            self.length += (i + 1)

    def __len__(self):
        return self.length
    
    def __iter__(self):
        self.current_node = self.head
        return self
    
    def __next__(self):
        if self.current_node is not None:
            return_node = self.current_node
            self.current_node = self.current_node.next
            return return_node
        raise StopIteration
    
    def __getitem__(self, idx: int):
        if idx >= len(self):
            raise IndexError
        node = self.head
        for _ in range(idx):
            node = node.next
        return node

    def append(self, val: int):
        """
        Append a new value to tail of list.

        Parameters
        ----------
        val : int
            Value to add.
        """
        if len(self) == 0:
            self.head = ListNode(val)
            self.tail = self.head
        else:
            self.tail.next = ListNode(val)
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
    

if __name__ == '__main__':
    l = LinkedList(range(5))
    for node in l:
        print(node.val)        
