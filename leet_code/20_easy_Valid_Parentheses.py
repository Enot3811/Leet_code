"""20. Valid Parentheses

https://leetcode.com/problems/valid-parentheses/

Given a string s containing just the characters '(', ')', '{', '}',
'[' and ']', determine if the input string is valid.

An input string is valid if:
1) Open brackets must be closed by the same type of brackets.
2) Open brackets must be closed in the correct order.
3) Every close bracket has a corresponding open bracket of the same type.
 
Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Constraints:
1 <= s.length <= 10**4
s consists of parentheses only '()[]{}'.
"""

# Размышления
# Базовая задача на стек
# Запоминаем всё открытые скобки в стек. Когда встречаем закрывающую, то она должна
# соответствовать последней отрытой.
# Когда дойдём до конца строки без ошибок - стек должен опустеть

class Solution:
    def isValid(self, s: str) -> bool:
        sp = []
        d = {')': '(', ']': '[', '}': '{'}
        for n in s:
            if n in {'(', '[', '{'}:
                sp.append(n)
            else:
                if len(sp) != 0 and d[n] == sp[-1]:
                    sp.pop(-1)
                else:
                    return False
        if len(sp) == 0:
            return True
        else:
            return False
