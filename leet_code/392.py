class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        if len(s) < len(t):
            return False
        j = 0  # Для прохода по второй строке
        for i in range(len(s)):
            if s[i] == t[j]:  # Если совпали символы, то двигаем вторую строку
                j += 1
                # Если прошли всю искомую строку, то всё
                if j == len(t):
                    return True
        # Если прошли всю исходную строку, но не искомую, то не нашли
        else:
            return False
        



if __name__ == '__main__':
    sol = Solution()
    tests = [
        ['abcde', 'ace', True],
        ['abcde', 'acx', False],
        ['a', 'aaa', False],
        ['aaa', 'a', True],
        ['']
    ]

    for s, t, ans in tests:
        print(sol.isSubsequence(s, t), ans)