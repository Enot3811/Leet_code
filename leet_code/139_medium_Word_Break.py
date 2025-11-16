"""139. Word Break

https://leetcode.com/problems/word-break/

Given a string s and a dictionary of strings wordDict,
return true if s can be segmented into a space-separated sequence of one
or more dictionary words.

Note that the same word in the dictionary may be reused multiple times
in the segmentation. 

Example 1:
Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Example 2:
Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.

Example 3:
Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false

Constraints:
1 <= s.length <= 300
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 20
s and wordDict[i] consist of only lowercase English letters.
All the strings of wordDict are unique.
"""


# Размышления
# Не нашлось никаких эффективных способов решить данную задачу.
# По сути нам всё равно придётся перебирать все варианты на каждом шагу.
# Можно строить отрезки и проверять, находится ли он в словаре,
# но более удобно будет перебирать сами слова на текущей букве.
# В итоге на i-м индексе у нас может быть несколько вариантов, какое слово взять.
# Делаем поиск в глубину, пытаемся найти способ добраться до конца строки.
# Или иными словами DP с разбиением строки на подстрои и подзадачи.
# Единственная оптимизация, которая здесь нужна, это кэш для уже просчитанных ранее i.
# Если мы каким-то образом уже попадали на индекс i, и при этом задачу не решили,
# значит он был тупиковым, и это следует запоминать в кэш


from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.cache = set()
        self.word_dict = wordDict
        self.s = s
        return self.solve_step(0)

    def solve_step(self, i: int) -> bool:
        # Наша цель прийти в конец слова
        if i == len(self.s):
            return True
        # Проверяем, не решали ли мы эту подзадачу ранее
        if i in self.cache:
            return False
        # На каждом i смотрим, можем ли мы взять какое-то из слов в словаре
        for word in self.word_dict:
            # Если да, то ныряем вглубь
            if self.s[i:i + len(word)] == word:
                # пытаемся решить подзадачу на оставшемся суффиксе
                if self.solve_step(i + len(word)):
                    return True
        # Если никакое из слов не подошло для текущей подстроки, то это тупик
        else:
            # Запоминаем, если вдруг придём к этому индексу другим путём
            self.cache.add(i)
            return False


sol = Solution()

examples = [
    (("leetcode", ["leet", "code"]), True),
    (("applepenapple", ["apple", "pen"]), True),
    (("catsandog", ["cats","dog","sand","and","cat"]), False),
    (("a", ["a"]), True),
    (("a", ["b", "c"]), False),
    (("abcaabc", ["ab", "caa", "c", "aa", "b"]), True),
    (("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab", ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]), False)
]
for inp, ans in examples:
    res = sol.wordBreak(*inp)
    print(inp, res, ans)
