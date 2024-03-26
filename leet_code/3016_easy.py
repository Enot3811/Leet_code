"""Minimum Number of Pushes to Type Word I."""

from collections import Counter

class Solution:
    def minimumPushes(self, word: str) -> int:
        let_dict = Counter(word)
        sorted_letters = sorted(
            let_dict.items(), key=lambda pair: pair[1], reverse=True)
        res = 0
        for i, pair in enumerate(sorted_letters):
            res += pair[1] * (i // 8 + 1)
        return res


if __name__ == '__main__':
    sol = Solution()
    cases= [
        ('abcde', 5),
        ('a', 1),
        ('ab', 2),
        ('qwertyuio', 10),
        ('qwertyuiasdfghjkzxc', 33),
        ('aabbccddeeffgghhiiiiii', 24)
    ]
    for word, ans in cases:
        res = sol.minimumPushes(word)
        print('Got:', res, 'Exp:', ans)
