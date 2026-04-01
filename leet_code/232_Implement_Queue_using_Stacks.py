"""232. Implement Queue using Stacks

https://leetcode.com/problems/implement-queue-using-stacks/

Implement a first in first out (FIFO) queue using only two stacks.
The implemented queue should support all the functions of a normal queue
(push, peek, pop, and empty).

Implement the MyQueue class:
- void push(int x) Pushes element x to the back of the queue.
- int pop() Removes the element from the front of the queue and returns it.
- int peek() Returns the element at the front of the queue.
- boolean empty() Returns true if the queue is empty, false otherwise.

Notes:
You must use only standard operations of a stack, which means only push to top,
peek/pop from top, size, and is empty operations are valid.
Depending on your language, the stack may not be supported natively.
You may simulate a stack using a list or deque (double-ended queue) as long
as you use only a stack's standard operations.

Example 1:
Input
["MyQueue", "push", "push", "peek", "pop", "empty"]
[[], [1], [2], [], [], []]
Output
[null, null, null, 1, 1, false]
Explanation
MyQueue myQueue = new MyQueue();
myQueue.push(1); // queue is: [1]
myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
myQueue.peek(); // return 1
myQueue.pop(); // return 1, queue is [2]
myQueue.empty(); // return false

Constraints:
1 <= x <= 9
At most 100 calls will be made to push, pop, peek, and empty.
All the calls to pop and peek are valid.

Follow-up: Can you implement the queue such that each operation
is amortized O(1) time complexity?
In other words, performing n operations will take overall O(n) time
even if one of those operations may take longer.
"""

# Теги
# Очередь (queue), Стек (stack)

# Размышления
# В стеке при добавлении элементов каждый следующий придавливает первый: 123 и т.д.
# Чтобы получить доступ к первому элементу нужно выложить верхние.
# Для этого нам нужен второй стек. Перекладываем: 123 -> 321
# В итоге элементы перевернулись и стали доступны как при очереди.
# При этом мы потратили n операций, но для последующих n элементов всё пройдёт за 1.
# Чтобы новыми элементами не поломать эту логику делаем так: кладём в первый стек,
# а когда нужно взять, пытаемся брать из второго. Если он пустой, то переваливаем
# весь первый стек во второй.

class MyQueue:

    def __init__(self):
        self.on_in = []
        self.on_out = []

    def push(self, x: int) -> None:
        self.on_in.append(x)

    def pop(self) -> int:
        if not self.on_out:
            while self.on_in:
                self.on_out.append(self.on_in.pop())
        return self.on_out.pop()

    def peek(self) -> int:
        if not self.on_out:
            while self.on_in:
                self.on_out.append(self.on_in.pop())
        return self.on_out[-1]

    def empty(self) -> bool:
        return not self.on_out and not self.on_in

queue = MyQueue()
queue.push(1)
queue.push(2)
print(queue.peek())  # 1
print(queue.pop())  # 1
print(queue.empty())  # False
queue.push(3)
print(queue.pop())  # 2
print(queue.pop())  # 3
print(queue.empty())  # True
queue.push(4)
print(queue.peek())  # 4
print(queue.pop())  # 4
print(queue.empty())  # True
