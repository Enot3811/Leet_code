"""212. Word Search II

https://leetcode.com/problems/word-search-ii/

Given an m x n board of characters and a list of strings words,
return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells,
where adjacent cells are horizontally or vertically neighboring.
The same letter cell may not be used more than once in a word.

Example 1:
Input: board = [["o","a","a","n"],
                ["e","t","a","e"],
                ["i","h","k","r"],
                ["i","f","l","v"]],
words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]

Example 2:
Input: board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []

Constraints:
m == board.length
n == board[i].length
1 <= m, n <= 12
board[i][j] is a lowercase English letter.
1 <= words.length <= 3 * 10**4
1 <= words[i].length <= 10
words[i] consists of lowercase English letters.
All the strings of words are unique.
"""

from typing import List
from collections import Counter

# Размышления
# Задача является продолжением задачи Word Search (79), где был поиск одного слова.
# Задача целиком посвящена оптимизации решения.
# Просто взять решение (79) и прогнать его для n слов мы не можем, так как само по себе
# это решение уже было недопустимо медленное.
# Нужно производить поиск для всех слов одновременно, и здесь помогает prefix tree (208)
# Когда мы идём по dfs, у нас получается некая последовательность.
# Она может быть префиксом какого-либо из слов или нет.
# Потому если мы закинем все слова в prefix tree, то сможем на каждом шаге проверять
# все слова одновременно

# Изначальное решение, которое упирается в time limit
# Берём готовое дерево и пользуемся им, реализую описанную задумку.
# Плюс не забываем о некоторых старых оптимизациях из (79), которые всё так же могут
# обрезать лишние вызовы тяжёлого решения

# Дерево из 208-й задачи
class TrieNode:
    def __init__(self, is_real: bool = False) -> None:
        self.is_real = is_real
        self.children = {}

    def __getitem__(self, key: str):  
        return self.children[key]

    def __setitem__(self, key: str, value: 'TrieNode'):
        self.children[key] = value

    def __contains__(self, key: str):
        return key in self.children

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr_node = self.root
        for let in word:
            if let not in curr_node:
                curr_node[let] = TrieNode()
            curr_node = curr_node[let]
        curr_node.is_real = True

    def search(self, word: str) -> bool:
        curr_node = self.root
        for let in word:
            if let not in curr_node:
                return False
            curr_node = curr_node[let]
        return curr_node.is_real

    def startsWith(self, prefix: str) -> bool:
        # Ищем префикс. Если он есть, то в любом случае ниже будут слова
        curr_node = self.root
        for let in prefix:
            if let not in curr_node:
                return False
            curr_node = curr_node[let]
        return True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Перед поиском следует проверить наличие букв для хотя бы одного слова
        h = len(board)
        w = len(board[0])
        board_counter = {}
        for i in range(h):
            for j in range(w):
                let = board[i][j]
                board_counter[let] = board_counter.get(let, 0) + 1
        # Удалим из поиска все слова, для которых не хватает нужных букв
        words_to_find = []
        for word in words:
            counter = Counter(word)
            for let in counter:
                if let not in board_counter or counter[let] > board_counter[let]:
                    break
            else:
                words_to_find.append(word)
        # Если доска не смогла покрыть ни одного слова по буквам
        if not words_to_find:
            return []

        # Наполняем префиксное дерево словами, чтобы потом сверять собранные
        # последовательности букв с ним
        trie = Trie()
        for word in words_to_find:
            trie.insert(word)
        
        ans = set()
        def dfs(i: int, j: int, curr_prefix: str):
            # Небольшая оптимизация, закончить раньше, если все слова найдены
            if len(words_to_find) == len(ans):
                return

            if not trie.startsWith(curr_prefix):
                return
            if trie.search(curr_prefix):
                ans.add(curr_prefix)
            if (i < 0 or i >= h or
                j < 0 or j >= w or
                board[i][j] == '#'
            ):
                return

            curr_let = board[i][j]
            board[i][j] = '#'
            dfs(i, j + 1, curr_prefix + curr_let)
            dfs(i + 1, j, curr_prefix + curr_let)
            dfs(i, j - 1, curr_prefix + curr_let)
            dfs(i - 1, j, curr_prefix + curr_let)
            board[i][j] = curr_let

        # Всё так же проходим по доске и собираем слова с dfs
        for i in range(h):
            for j in range(w):
                dfs(i, j, "")
        return list(ans)


# Две основные причины time limit
# 1) Методы поиска дерева вызываются линейно от корня при каждой итерации dfs
# 2) Хоть мы и добавляем в ответ найденное слово, оно всё ещё остаётся в дереве,
# а потому провоцирует поиск на лишние ветвления после того, как его уже нашли.
# Нужна возможность удалять ноды и ветви дерева.

# Изменённое дерево
class TrieNode:
    def __init__(self) -> None:
        self.children: dict[str, TrieNode] = {}
        # Для удобства будем хранить слова вместо is_real
        # Теперь по его наличию будем проверять, дошли ли мы до слова
        self.word: str | None = None

# Методы поиска удалили, теперь будем итерироваться по нодам руками,
# что даёт возможность их потом удалять
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr_node = self.root
        for let in word:
            if let not in curr_node.children:
                curr_node.children[let] = TrieNode()
            curr_node = curr_node.children[let]
        curr_node.word = word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Перед поиском следует проверить наличие букв для хотя бы одного слова
        h = len(board)
        w = len(board[0])
        board_counter = {}
        for i in range(h):
            for j in range(w):
                let = board[i][j]
                board_counter[let] = board_counter.get(let, 0) + 1
        # Удалим из поиска все слова, для которых не хватает нужных букв
        words_to_find = []
        for word in words:
            counter = Counter(word)
            for let in counter:
                if let not in board_counter or counter[let] > board_counter[let]:
                    break
            else:
                words_to_find.append(word)
        # Если доска не смогла покрыть ни одного слова по буквам
        if not words_to_find:
            return []

        # Наполняем префиксное дерево словами, чтобы потом сверять собранные
        # последовательности букв с ним
        trie = Trie()
        for word in words_to_find:
            trie.insert(word)
        
        ans = []
        def dfs(i: int, j: int, node: TrieNode):
            let = board[i][j]
            # Если собираемый префикс не нашёл продолжения в дереве (или #)
            if let not in node.children:
                return

            # Отдельно запомним родителя и ребёнка для возможного удаления
            curr_node = node.children[let]

            # Слова хранят только "реальные" узлы, то есть мы нашли слово
            if curr_node.word:
                ans.append(curr_node.word)
                curr_node.word = None  # Больше не ищем слово (нужно для удаления ветки)

            board[i][j] = '#'
            for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_i, new_j = i + di, j + dj
                if 0 <= new_i < h and 0 <= new_j < w and board[new_i][new_j] != '#':
                    dfs(new_i, new_j, curr_node)
            board[i][j] = let

            # Удаление ноды, если у неё нет детей
            # Потом при возврате из рекурсии будет удаляться вся пустая ветка
            if not curr_node.children:
                del node.children[let]

        # Всё так же проходим по доске и собираем слова с dfs
        for i in range(h):
            for j in range(w):
                dfs(i, j, trie.root)
        return ans


cases = [
    (
        ([
            ["o","a","a","n"],
            ["e","t","a","e"],
            ["i","h","k","r"],
            ["i","f","l","v"]
        ], ["oath","eat","et","eta","ihk","hkr"]),
        ["oath","eat","et","eta","ihk","hkr"]
    ),
    (
        ([
            ["o","a","a","n"],
            ["e","t","a","e"],
            ["i","h","k","r"],
            ["i","f","l","v"]
        ], ["oath","pea","eat","rain"]),
        ["oath","eat"]
    ),
    (
        ([
            ["o","a","a","n"],
            ["e","t","a","e"],
            ["i","h","k","r"],
            ["i","f","l","v"]
        ], ["oath","pea","eat","rain","hklf","hf"]),
        ["oath","eat","hklf","hf"]
    ),
]
sol = Solution()
for inp, ans in cases:
    res = sol.findWords(*inp)
    print(res, ans)
        