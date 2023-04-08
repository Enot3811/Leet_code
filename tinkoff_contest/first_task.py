n = int(input())
s_inp = input()
color_inp = input()
words = s_inp.split()
color_spl = []
i = 0
for word in words:
    color_spl.append(color_inp[i:i + len(word)])
    i += len(word)
answer = 0
for color_word in color_spl:
    for i in range(1, len(color_word)):
        if color_word[i - 1] == color_word[i]:
            answer += 1
            break
print(answer)
