"""161. One Edit Distance

Premium lock.
https://leetcode.doocs.org/en/lc/161/

Given two strings s and t, return true if they are both one edit distance apart,
otherwise return false.

A string s is said to be one distance apart from a string t if you can:
- Insert exactly one character into s to get t.
- Delete exactly one character from s to get t.
- Replace exactly one character of s with a different character to get t.

Example 1:
Input: s = "ab", t = "acb"
Output: true
Explanation: We can insert 'c' into s to get t.

Example 2:
Input: s = "", t = ""
Output: false
Explanation: We cannot get t from s by only one step.

Constraints:
0 <= s.length, t.length <= 10^4
s and t consist of lowercase letters, uppercase letters, and digits.
"""

# Теги
# Просто лёгкая задача (Easy task)

# Размышления
# Задача похожа на (72. Edit Distance), но является обрезанной версией.
# Здесь всего 1 операция редактирования, которую можно поймать просто циклом по строкам.
# Строки не должны различаться по длине более чем 1 символ.
# Если длина равна, то нужна 1 замена.
# Если длина отличается на 1, то нужно 1 удаление.
# Вот и проверяем, что строки этому соответствуют.

class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        # Пусть s всегда будет большей
        if len(s) < len(t):
            s, t = t, s
        
        edit = False
        if len(s) - len(t) > 1:
            return False

        # Нужно удалить один символ в s
        elif len(s) - len(t) == 1:
            i = 0
            j = 0
            while j < len(t):
                if s[i] != t[j]:
                    # Уже было удаление
                    if edit:
                        return False
                    else:
                        # Удаляем букву, двигая длинную строку
                        edit = True
                        i += 1
                else:
                    i += 1
                    j += 1
            # После цикла 0 или 1 удаление.
            # Если 0, то последняя буква s под удаление.
            return True
            
        # Нужно заменить 1 символ
        else:
            for let1, let2 in zip(s, t):
                if let1 != let2:
                    # Больше одной замены
                    if edit:
                        return False
                    # Замены ещё не было
                    else:
                        edit = True
            # Была лишь 1 замена
            if edit:
                return True
            # Если строки оказались равны
            else:
                return False

# Или более лаконичный код со срезами
# Гарантируем, что s всегда длиннее или равна t
class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if len(s) < len(t):
            s, t = t, s
            
        if len(s) - len(t) > 1:
            return False

        # Ищем первое различие
        for i in range((len(t))):
            if s[i] != t[i]:
                if len(s) == len(t):
                    # Остаток строки должен быть равен
                    return s[i:] == t[i:]
                else:
                    # Остаток строки после удаления должен быть равен
                    return s[i + 1:] == t[i:]
        # Если не нашли отличий, то s должна быть длиннее
        return len(s) == len(t) + 1


cases = [
    (("", ""), False),
    (("a", ""), True),
    (("a", "ab"), True),
    (("a", "abb"), False),
    (("a", "aa"), True),
    (("a", "aaa"), False),
    (("a", "z"), True),
    (("az", "z"), True),
    (("ab", "z"), False),
]
sol = Solution()
for inp, ans in cases:
    res = sol.isOneEditDistance(*inp)
    print(inp, res, ans)
        