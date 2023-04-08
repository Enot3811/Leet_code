n = int(input())
if n % 2 == 0:
    a = n // 2
    b = a
else:
    a = n // 2
    b = a + 1
while a != 0:
    if b % a == 0:
        break
    b += 1
    a -= 1
print(a, b)