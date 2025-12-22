"""269. Alien Dictionary

Premium lock
https://www.lintcode.com/problem/alien-dictionary/

There is a new alien language which uses the latin alphabet.
However, the order among letters are unknown to you.
You receive a list of non-empty words from the dictionary,
where words are sorted lexicographically by the rules of this new language.
Derive the order of letters in this language.

- You may assume all letters are in lowercase
- At first different letter, if the letter in s precedes the letter in t
in the given list order, then the dictionary order of s is less than t
- The dictionary is invalid, if string a is prefix of string b and b is appear before a
- If the order is invalid, return an empty string
- There may be multiple valid order of letters,
return the smallest in normal lexicographical order
- The letters in one string are of the same rank by default
and are sorted in Human dictionary order

Example 1:
Input: ["wrt","wrf","er","ett","rftt"]
Output: "wertf"
Explanation:
from "wrt"and"wrf" ,we can get 't'<'f'
from "wrt"and"er" ,we can get 'w'<'e'
from "er"and"ett" ,we can get 'r'<'t'
from "ett"and"rftt" ,we can get 'e'<'r'
So return "wertf"

Example 2:
Input: ["z","x"]
Output: "zx"
Explanation:
from "z" and "x", we can get 'z' < 'x'
So return "zx"
"""

# Размышления
# Для решения нам потребуется знать топологическую сортировку (например 210),
# и min heap структуру (например, 347).
# Первое: необходимо атомарно взглянуть на лексикографическую сортировку слов.
# Как мы сравниваем 2 слова? У них первые буквы одинаковые, но в какой-то момент
# будет одна несовпадающая буква. И именно она и важна.
# Например, "abcd" и "abea" -> "ce". Остальные буквы выбрасываем.
# Так от списка слов мы можем перейти к парам букв, что уже неплохо.
# Второе: в этой задаче спрятан направленный граф,
# который поддаётся топологической сортировке.
# Чем раньше буква в алфавите, тем раньше она будет в графе.
# То есть, например: "aa", "ab", "ac", "c" -> a>b, b>c, a>c
# У 'a' нет "требований", она идёт первая, затем из 'a' выходит 'b' итд.
# Если же во входных данных ошибка, то это приведёт к циклу,
# например: "ab", "bc", "cc", "ca" -> a>b>c>a. 
# Топологическая сортировка нам это покажет.
# Третье: требуется лексикографический порядок между буквами, которые неизвестно
# как стоят друг относительно друга.
# Например: "ab", "az", "b", "c" -> a>b>c и a>z
# Мы не знаем, как относятся друг к другу z и b,c, потому порядок должен быть "abcz".
# И в классической топологической сортировке в очередь сначала попала бы 'z',
# и получилось бы "azbc". Поэтому вместо очереди используем min heap.
# При добавлении 'z' и 'b' она отсортирует их как "bz", а потом и "cz".
# Извлечение верхнего элемента из кучи займёт log(n) времени, так как сдвинуть придётся
# лишь одну ветку длиной log(n), остальное останется на своих местах.

from typing import List
import heapq

class Solution:
    def alien_order(self, words: List[str]) -> str:
        # Узнаём, что за буквы встречаются в словах
        letters = set()
        for word in words:
            letters.update(set(word))

        # Проходим по словам. Ищем первую букву, по которой они расходятся.
        # Буква из первого слова будет идти до буквы из второго.
        # Добавим такое ребро
        edges = []
        for i in range(1, len(words)):
            for char1, char2 in zip(words[i - 1], words[i]):
                if char1 != char2:
                    edges.append((char1, char2))
                    break
            # Если все буквы были равны, то одно слово является префиксом другого
            # Нужно убедиться в правильности порядка
            else:
                if len(words[i - 1]) > len(words[i]):
                    return ""

        # Теперь делаем топологическую сортировку (пример 210)
        counters = {let: 0 for let in letters}  # Сколько букв до (нуждается в)
        next_lets = {let: [] for let in letters}  # Какие буквы после (кто нуждается)
        for u, v in edges:
            counters[v] += 1
            next_lets[u].append(v)
        
        # Очень интересный момент - используем min heap,
        # чтобы обеспечить лексикографический порядок между буквами,
        # между которыми нет твёрдой связи.
        # Например, b->a и c. Сначала добавляем "bc". Обработав b получим "ca".
        # Между 'a' и 'c' нет зависимостей,
        # но при этом 'a' хотелось бы обработать раньше 'c'.
        # При добавлении 'a' в min heap, она сама отсортирует её, и мы получим "ac".
        # Извлечение же из начала списка займёт всего log(n), так как это дерево.
        heap = []
        for let, val in counters.items():
            if val == 0:
                heapq.heappush(heap, let)
        
        ans = []
        while len(heap) > 0:
            let = heapq.heappop(heap)
            ans.append(let)
            for next_let in next_lets[let]:
                counters[next_let] -= 1
                if counters[next_let] == 0:
                    heapq.heappush(heap, next_let)
        return ''.join(ans) if len(ans) == len(letters) else ""


# Во многих кейсам много вариантов ответа
cases = [
    (["wrt","wrf","er","ett","rftt"], "wertf"),
    (["z","x"], "zx"),
    (["ab", "ac", "bd", "ba", "d"], ""),
    (["ade", "ae", "cf", "gik"], "acdefgik"),
    (["ab", "bc", "cd"], "abcd"),
    (["ab", "ad", "ba", "bc", "bd"], "abcd"),
    (["abe", "ade", "adf", "ba", "bac", "bce", "e"], "abcdef"),
    (["abe", "ade", "adf", "ba", "bac", "bce", "ed", "ef"], "abcdef"),
    (["abec", "adef", "adff", "baac", "baca", "bced", "bcf", "eda", "efb"], "abcdef"),
    (["abc", "abd", "add", "ade", "cda", "cdb", "ced", "cee", "eca", "ecc", "ede", "eee"], "abcde")
]
sol = Solution()
for words, ans in cases:
    res = sol.alien_order(words)
    print(words, res, ans)
