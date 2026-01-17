"""146. LRU Cache

Design a data structure that follows the constraints of
a Least Recently Used (LRU) cache.

Implement the LRUCache class:
- LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
- int get(int key) Return the value of the key if the key exists, otherwise return -1.
- void put(int key, int value) Update the value of the key if the key exists. Otherwise,
add the key-value pair to the cache. If the number of keys exceeds
the capacity from this operation, evict the least recently used key.

The functions get and put must each run in O(1) average time complexity. 

Example 1:
Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]
Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4

Constraints:
1 <= capacity <= 3000
0 <= key <= 10^4
0 <= value <= 10^5
At most 2 * 10^5 calls will be made to get and put.
"""

# Теги
# Связанный список (Linked list)

# Размышления
# Сначала в голову приходит очередь и, возможно, ленивое удаление элементов.
# Но так или иначе это вырождается в линейную сложность.
# Интереснее идея со связными списками.
# Может показаться, что их будет неудобно использовать,
# ведь поиск элемента это линейное время.
# Но если мы будем в дикте хранить не просто ключ,значение и искать ноду в списке,
# а ключ и саму ноду.
# Тогда искать уже не надо, её сразу можно дёрнуть, вырезать из списка
# и вставить в конец за O(1).
# Из интересного ещё, возможность применить паттерн с dummy head и tail.
# Обычно приходится писать много условий на случай, когда у нас 0 элементов и больше.
# Также нужно менять текущие значения головы и хвоста.
# Вместо этого сразу создадим 2 пустые ноды head и tail, которые никогда не будут удалены.
# Тогда мы оперируем не head и tail, а head.next и tail.prev.
# Этот подход позволяет унифицировать операции и чуть облегчить логику.

from typing import Dict

class Node:
    def __init__(self, key: int, val: int) -> None:
        self.val = val
        self.key = key
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.elems: Dict[int, Node] = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.elems:
            node = self.elems[key]
            # Вырезаем элемент
            node.prev.next = node.next
            node.next.prev = node.prev
            # Двигаем его в конец перед фиктивным хвостом
            prev = self.tail.prev
            prev.next = node
            node.prev = prev
            node.next = self.tail
            self.tail.prev = node
            return node.val
        return -1
        
    def put(self, key: int, value: int) -> None:
        # Обновление
        if key in self.elems:
            node = self.elems[key]
            node.val = value
            # Вырезаем элемент
            node.prev.next = node.next
            node.next.prev = node.prev
            # Двигаем его в конец перед фиктивным хвостом
            prev = self.tail.prev
            prev.next = node
            node.prev = prev
            node.next = self.tail
            self.tail.prev = node
        
        # Добавление
        else:
            # Нужно вытеснить
            if self.capacity == 0:
                node = self.head.next  # Следующий после фиктивной головы
                node.prev.next = node.next
                node.next.prev = node.prev
                self.elems.pop(node.key)
            else:
                self.capacity -= 1

            # Добавление
            node = Node(key, value)
            self.elems[key] = node
            # в конец перед фиктивным хвостом
            prev = self.tail.prev
            prev.next = node
            node.prev = prev
            node.next = self.tail
            self.tail.prev = node

cache = LRUCache(1)
cache.put(1,1)
print(cache.get(2))
print(cache.get(1))
cache.put(1,2)
print(cache.get(1))
cache.put(2,2)
print(cache.get(1))
print(cache.get(2))
