"""A module that contains LinkedList class."""

from typing import Iterable, Any, Optional


class ListNode:
    """Node of LinkedList."""

    def __init__(self, val: int):
        self.val = val
        self.next: LinkedList = None
        self.prev: LinkedList = None


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
                    new_node = ListNode(val)
                    self.tail.next = new_node
                    new_node.prev = self.tail
                    self.tail = new_node
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
            new_node = ListNode(val)
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
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
        if len(self) == 1:
            popped_val = self.head.val
            self.head = None
            self.tail = None
        elif idx == 0:
            popped_val = self.head.val
            self.head = self.head.next
            self.head.prev = None
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
                current.next.prev = current
        self.length -= 1
        return popped_val
    
    @classmethod
    def from_list_nodes(cls, list_head: ListNode) -> 'LinkedList':
        """Create a `LinkedList` from given list nodes.

        Parameters
        ----------
        list_head : ListNode
            A head of the given list nodes.

        Returns
        -------
        LinkedList
            The created `LinkedList`.
        """
        obj = cls()
        obj.head = list_head
        node = list_head
        length = 1
        while node.next != None:
            node = node.next
            length += 1
        obj.tail = node
        obj.length = length
        return obj

if __name__ == '__main__':
    l = LinkedList(range(5))
    for node in l:
        print(node.val)        
