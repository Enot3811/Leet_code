"""D. Постфиксная запись

Дано выражение в постфиксном виде. Необходимо его посчитать
"""

# Размышления
# Здесь просто надо посмотреть, как считается постфиксная запись

from collections import deque

def reverse_notation(notation: str) -> int:
    stack = deque()
    for i in range(0, len(notation), 2):
        let = notation[i]
        if let.isdigit():
            stack.append(int(let))
        else:
            num2 = stack.pop()
            num1 = stack.pop()
            if let == '+':
                stack.append(num1 + num2)
            elif let == '-':
                stack.append(num1 - num2)
            else:
                stack.append(num1 * num2)
    return stack.pop()


notation = input()
print(reverse_notation(notation))
