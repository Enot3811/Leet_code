n = int(input())
numbers = [int(input()) for i in range(n)]
cur_set = set()
for i, num in enumerate(numbers):
    if i == 0:
        answer = 0
        cur_set.add(num)
    elif num not in cur_set:
        for old_num in cur_set:
            answer = max(answer, num ^ old_num)
        cur_set.add(num)
    print(answer)
