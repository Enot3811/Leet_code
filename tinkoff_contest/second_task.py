def trans(account):
    if tuple(account) not in answer:
        answer.add(tuple(account))
        for i in range(3):
            if account[i] - currencies[i] >= 0:
                sub_account = account.copy()
                sub_account[i] -= currencies[i]
                for j in range(3):
                    if j != i:
                        next_account = sub_account.copy()
                        next_account[j] += currencies[j]
                        trans(next_account)


currencies = input()
account = input()
currencies = [int(i) for i in currencies.split()]
account = [int(i) for i in account.split()]
answer = set()
trans(account)
print(len(answer))
