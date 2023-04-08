from math import ceil
# b, c = [int(i) for i in input().split()]
# r, d = [int(i) for i in input().split()]
# b, c = (10, 700000)
# r, d = (350000, 200000)
# b, c = (21, 1000000)
# r, d = (1100000, 0)
# b, c = (1000000, 999999)
# r, d = (1, 1)
# b, c = (100, 456789)
# r, d = (4500000, 543211)
# b, c = (1000000, 999900)
# r, d = (100, 0)
b, c = (100000, 930000)
r, d = (70000, 0)
mill = 1000000

# Не доделал. Вылетает по времени
# Необходимо найти закономерность, при которой можно бесконечно тратить
# банкноты.

# Код для перебора
# from math import ceil


# def NOD(a, b):
#     if a < b:
#         a, b = b, a
#     while a % b != 0:
#         a = a % b
#         a, b = b, a
#     return b


# def NOK(a, b):
#     return (a * b) / NOD(a, b)


# price = 30
# bank = 100
# coins = 90
# auto = 0
# change = bank - price

# n = ceil((bank - price) / price)
# print(f'{n=}')
# print('n * price', n * price)
# print('n * price - change', n * price - change)
# nok = NOK(price, change)
# print('NOD', NOD(price, change), 'NOK', NOK(price, change))
# n_pereliv = nok // change
# print(f'{n_pereliv=}')
# st_coins = ceil(change / price) * price
# print(f'{st_coins=}')
# diff = st_coins - change
# print(f'{diff=}')
# ans = change + diff * (n_pereliv - 1)
# print(f'{ans=}')



# i = 0
# while i < 100 and auto >= 0:
#     if coins >= price:
#         coins -= price
#         auto += price
#     else:
#         auto -= change
#         coins += change
#     i += 1
#     print(auto, coins)

answer = 0

# Can we pay with only banknotes
if r % mill == 0:
    cost_in_banknotes = r // mill
    num_purchs = b // cost_in_banknotes
    b -= num_purchs * cost_in_banknotes
    answer += num_purchs
# Can we use all our banknotes with million coins?
if c + r >= mill:
    answer2 = (b * mill + c) // r + answer
    print(answer2)
while True:
    coin_diff = r - c
    # Can we pay with only coins?
    if coin_diff <= 0:
        num_purchases = c // r
        c -= r * num_purchases
        d += r * num_purchases
        answer += num_purchases
    # Try to use our banknotes
    else:
        paid_banknotes = ceil(coin_diff / mill)
        paid_coins = r - paid_banknotes * mill
        if paid_banknotes > b or d < -paid_coins:
            break
        b -= paid_banknotes
        d += paid_coins
        c -= paid_coins
        answer += 1

print(answer)
