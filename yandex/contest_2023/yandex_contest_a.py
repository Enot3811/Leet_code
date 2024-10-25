"""
Сколько пациентов может принять врач при времени t и списки a
с временами осмотра
"""

with open('input.txt') as f:
    lines = f.readlines()
n, t = list(map(int, lines[0].split()))
a = list(map(int, lines[1].split()))

a.sort()

got = 0
for i in range(n):
    got += a[i]
    if got > t:
        print(i)
        break
else:
    print(n)
