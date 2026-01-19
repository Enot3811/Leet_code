"""79. Word search

Check the image!
https://leetcode.com/problems/word-search/

Given an m x n grid of characters board and a string word,
return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells,
where adjacent cells are horizontally or vertically neighboring.
The same letter cell may not be used more than once. 

Example 1:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],
word = "ABCCED"
Output: true

Example 2:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],
word = "SEE"
Output: true

Example 3:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],
word = "ABCB"
Output: false

Constraints:
m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board and word consists of only lowercase and uppercase English letters.

Follow up: Could you use search pruning to make your solution faster
with a larger board?
"""

# Теги
# Поиск в глубину (dfs), мемоизация словарём (dict memoization)

# Размышления
# Сразу мысли о dfs. Проходим по доске и на каждой ячейке пытаемся построить слово.
# Отслеживаем пройденный путь, чтобы не зациклиться,
# и просто пытаемся рекурсивно найти слово.
# Сложность n^2 * 4^(n^2) и её в данной задаче невозможно принципиально улучшить.

from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        h = len(board)
        w = len(board[0])
        def dfs(i: int, j: int, let_idx: int):
            if let_idx == len(word):
                return True
            if ((i, j) in visited or
                i < 0 or i >= h or
                j < 0 or j >= w or
                word[let_idx] != board[i][j]
            ):
                return False
            if board[i][j] == word[let_idx]:
                visited.add((i, j))
                res = (
                    dfs(i, j + 1, let_idx + 1) or
                    dfs(i + 1, j, let_idx + 1) or 
                    dfs(i, j - 1, let_idx + 1) or
                    dfs(i - 1, j, let_idx + 1)
                )
                visited.remove((i, j))
                return res

        for i in range(h):
            for j in range(w):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True
        return False


# Оптимизации, которые чуть могут ускорить:
# 1) Вместо привычного set для visited использовать саму доску и список backtrack.
# Запоминаем текущую букву, а на доске закашиваем его спецсимволом.
# 2) Предварительно можем посмотреть, хватает ли на доске нужных букв в принципе.
# Это может позволить отсеять дорогой поиск в некоторых случаях
# 3) Можно искать слово задом наперёд, если последняя буква встречается реже, чем первая.
# Тогда мы уменьшим количество изначальных ветвлений
from collections import Counter

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        backtrack = []
        h = len(board)
        w = len(board[0])
        def dfs(i: int, j: int, let_idx: int):
            if let_idx == len(word):
                return True
            if (i < 0 or i >= h or
                j < 0 or j >= w or
                word[let_idx] != board[i][j]
            ):
                return False
            if board[i][j] == word[let_idx]:
                backtrack.append(board[i][j])
                board[i][j] = '#'
                res = (
                    dfs(i, j + 1, let_idx + 1) or
                    dfs(i + 1, j, let_idx + 1) or 
                    dfs(i, j - 1, let_idx + 1) or
                    dfs(i - 1, j, let_idx + 1)
                )
                board[i][j] = backtrack.pop()
                return res

        counter = Counter(word)
        # Начнём поиск с конца, если последняя буква встречается реже
        if counter[word[-1]] < counter[word[0]]:
            word = word[::-1]
        # Проверим доску на наличие всех необходимых букв
        for i in range(h):
            for j in range(w):
                if board[i][j] in counter:
                    counter[board[i][j]] -= 1
        for let in counter:
            if counter[let] > 0:
                return False

        for i in range(h):
            for j in range(w):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True
        return False

cases = [
    (
        ([
            ["A","B","C","E"],
            ["S","F","C","S"],
            ["A","D","E","E"],
        ], "ABCCED"), True
    ),
    (
        ([
            ["A","B","C","E"],
            ["S","F","C","S"],
            ["A","D","E","E"]
        ], "SEE"), True
    ),
    (
        ([
            ["A","B","C","E"],
            ["S","F","C","S"],
            ["A","D","E","E"]
        ], "ABCB"), False
    ),
    (
        ([
            ['a','a','a'],
            ['A','A','A'],
            ['a','a','a']
        ], "aAaaaAaaA"), True
    ),
    (
        ([
            ['a','a','a'],
            ['A','A','A'],
            ['a','a','a']
        ], "aaAaaAa"), True
    ),
    (
        ([
            ['a','a','a'],
            ['A','A','A'],
            ['a','a','a']
        ], "aaAAA"), True
    )
]
sol = Solution()
for inp, ans in cases:
    res = sol.exist(*inp)
    print(res, ans)
