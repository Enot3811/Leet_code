"""Word search.

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


from typing import List
from collections import defaultdict, Counter


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        positions = (0, 1, 0, -1, 0)
        num_letters = Counter(word)
        letters_coords = defaultdict(set)

        def search(i: int, j: int, idx: int = 1):
            if idx == len(word):
                return True
            for k in range(4):
                coord = (i + positions[k], j + positions[k + 1])
                if coord in letters_coords[word[idx]]:
                    letters_coords[word[idx]].remove(coord)
                    if search(*coord, idx + 1):
                        return True
                    letters_coords[word[idx]].add(coord)

        for i in range(len(board)):
            for j in range(len(board[i])):
                let = board[i][j]
                if let in num_letters:
                    letters_coords[let].add((i, j))

        if len(letters_coords) != len(num_letters):
            return False
        for letter in letters_coords:
            if len(letters_coords[letter]) < num_letters[letter]:
                return False
        if len(letters_coords[word[-1]]) < len(letters_coords[word[0]]):
            word = word[::-1]

        for i, j in letters_coords[word[0]]:
            letters_coords[word[0]].remove((i, j))
            if search(i, j):
                return True
            letters_coords[word[0]].add((i, j))
        return False


sol = Solution()
print(sol.exist([['a', 'a', 'a'], ['A', 'A', 'A'], ['a', 'a', 'a']],
                'aAaaaAaaA'))
