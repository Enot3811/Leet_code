"""51. N-Queens

https://leetcode.com/problems/n-queens/

The n-queens puzzle is the problem of placing n queens on an n x n chessboard
such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle.
You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement,
where 'Q' and '.' both indicate a queen and an empty space, respectively. 

Example 1:
Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above

Example 2:
Input: n = 1
Output: [["Q"]]

Constraints:
1 <= n <= 9
"""

# Теги
# Поиск в глубину (dfs)

# Размышления
# Задача упрощена тем, что количество строк равно количеству королев.
# Нужно на каждую строку поставить фигуру, и затем попробовать решить задачу дальше,
# то есть dfs подход.
# Чтобы определять, куда мы можем поставить, а куда нет, будем собирать все блокируемые
# вертикали, горизонтали и диагонали в сеты.
# Получается решение со сложностью n^n.
# По памяти n, не считая собираемых решений (досок со строками).

from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # Множества для сохранения блокированных линий
        # Горизонтали хранить не будем. Вместо этого будем по ним двигаться.
        # То есть одна фигура на одну горизонталь.
        verticals = set()
        diags1 = set()
        diags2 = set()
        ans = []
        curr_board = []
        
        def dfs(i: int):
            # Прошли всю доску, поставили все фигуры
            if i == n:
                ans.append([])
                for j in curr_board:
                    ans[-1].append('.' * j + 'Q' + (n - j - 1) * '.')
                return
                
            # Проходим по текущей строке
            for j in range(n):
                # Все координаты главной диагонали имеют один и тот же i - j
                diag1 = i - j
                # Все координаты главной диагонали имеют один и тот же i + j
                diag2 = i + j

                # Проверяем клетки на возможность поставить фигуру
                if (j not in verticals and
                    diag1 not in diags1 and
                    diag2 not in diags2
                ):
                    # Добавляем текущую клетку в текущее решение
                    verticals.add(j)
                    diags1.add(diag1)
                    diags2.add(diag2)
                    curr_board.append(j)
                    dfs(i + 1)
                    # Как отработали её, убираем
                    verticals.remove(j)
                    diags1.remove(diag1)
                    diags2.remove(diag2)
                    curr_board.pop()
        dfs(0)
        return ans

cases = [
    (4, [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]),
    (1, [['Q']]),
]
sol = Solution()
for n, ans in cases:
    res = sol.solveNQueens(n)
    print("res")
    for r in res:
        print(*r, sep='\n', end="\n\n")
    print("ans")
    for a in ans:
        print(*a, sep='\n', end="\n\n")
