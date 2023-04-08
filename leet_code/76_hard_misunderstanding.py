'''
Minimum Window Substring.
Неправильно понял условие.
Находит минимальную подстроку со всеми заданными символами в заданном порядке
'''


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        table = []
        best = None
        best_score = None
        for i, s_let in enumerate(s):
            table.append([])
            for j, t_let in enumerate(t):
                if s_let == t_let:
                    added = False
                    if j == 0:
                        table[i].append((j, i, i))
                        added = True
                    elif i > 0 and table[i - 1][j - 1] is not None:
                        table[i].append((j, i, table[i - 1][j - 1][-1]))
                        added = True
                    else:
                        table[i].append(None)
                    if added:
                        if j == len(t) - 1:
                            cur_score = table[i][j][1] - table[i][j][-1]
                            if best_score is None or cur_score < best_score:
                                best_score = cur_score
                                best = (table[i][j][-1], table[i][j][1] + 1)
                else:
                    if i == 0:
                        table[i].append(None)
                    else:
                        table[i].append(table[i - 1][j])
        return best


sol = Solution()
s = 'baecbeeacbac'
t = 'abc'
result = sol.minWindow(s, t)
print(result)
print(s[slice(*result)])
