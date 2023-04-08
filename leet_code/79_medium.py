'''Word search.'''


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
