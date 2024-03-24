"""Minimum Number of Pushes to Type Word I."""


class Solution:
    def minimumPushes(self, word: str) -> int:
        cnt1 = len(word) // 8
        cnt2 = len(word) % 8
        res = 0
        for i in range(1, cnt1 + 1):
            res += i * 8
        mult = 1 if cnt1 == 0 else i + 1
        res += mult * cnt2
        return res


if __name__ == '__main__':
    sol = Solution()
    cases= [
        ('abcde', 5),
        ('a', 1),
        ('ab', 2),
        ('qwertyuio', 10),
        ('qwertyuiasdfghjkzxc', 33)
    ]
    for word, ans in cases:
        res = sol.minimumPushes(word)
        print('Got:', res, 'Exp:', ans)
