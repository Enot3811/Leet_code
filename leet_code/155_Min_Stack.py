"""155. Min Stack

https://leetcode.com/problems/min-stack/

Design a stack that supports push, pop, top, and retrieving the minimum element
in constant time.

Implement the MinStack class:
- MinStack() initializes the stack object.
- void push(int val) pushes the element val onto the stack.
- void pop() removes the element on the top of the stack.
- int top() gets the top element of the stack.
- int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.

Example 1:
Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]
Output
[null,null,null,null,-3,null,0,-2]
Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2

Constraints:
-2^31 <= val <= 2^31 - 1
Methods pop, top and getMin operations will always be called on non-empty stacks.
At most 3 * 10^4 calls will be made to push, pop, top, and getMin.
"""

# Теги
# Стек (stack)

# Размышления
# Здесь следует обратить внимание, что класть и вынимать числа мы можем только сверху.
# Если мы положили в стек какое-то очень маленькое число, и затем накидали поверх него
# других чисел, то минимум никуда не денется, пока мы снова его не раскопаем.
# То есть нам просто нужно помнить текущий минимум, которые лежит где-то глубже в стеке.
# Если найдём число ещё меньше, то запомним его тоже.
# Получится история минимумов.
# Если мы pop-м докапываемся до текущего минимума, то удаляем его из истории тоже.
# Вся фишка в том, что мы не удаляем случайные элементы из стека.
# Минимум может стать не любой элемент.

class MinStack:

    def __init__(self):
        self.min_history = []
        self.stack = []
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.min_history) == 0 or self.min_history[-1] >= val:
            self.min_history.append(val)

    def pop(self) -> None:
        val = self.stack.pop()
        if val == self.min_history[-1]:
            self.min_history.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_history[-1]

minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.getMin())  # return -3
minStack.pop()
print(minStack.top())  # return 0
print(minStack.getMin())  # return -2
