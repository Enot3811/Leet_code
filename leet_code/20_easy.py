'''Valid Parentheses.'''


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
