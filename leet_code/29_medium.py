'''Divide Two Integers.'''


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = (divisor < 0) ^ (dividend < 0)
        divisor = abs(divisor)
        dividend = abs(dividend)
        
        multipliers = []
        answer = 0
        cumuli = 0
        while cumuli < dividend:
            i = len(multipliers) - 1
            if i >= 0:
                while cumuli + multipliers[i][0] > dividend and i > 0:
                    i -= 1
                cumuli += multipliers[i][0]
                answer += multipliers[i][1]
            else:
                cumuli += divisor
                answer += 1
            multipliers.append((cumuli, answer))
        if cumuli > dividend:
            answer -= 1
        if sign:
            answer = -answer
        if answer > 2147483647:
            answer = 2147483647
        elif answer < -2147483648:
            answer = -2147483648
        return answer
