class Solution:
    def isHappy(self, n: int) -> bool:
        viewed = [n]
        while n != 1:
            digits = []
            while n != 0:
                digits.append((n % 10) ** 2)
                n //= 10
            n = sum(digits)
            if n in viewed:
                return False
            else:
                viewed.append(n)
        return True
        

sol = Solution()
tests = [
    (19, True),
    (2, False),
    (1, True),
    (123, False),
    (1111111, True)
]

for inp, ans in tests:
    out = sol.isHappy(inp)
    print('Out:', out, 'Exp:', ans)
