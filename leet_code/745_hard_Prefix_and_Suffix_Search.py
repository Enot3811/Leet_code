"""745. Prefix and Suffix Search

https://leetcode.com/problems/prefix-and-suffix-search/

Design a special dictionary that searches the words in it by a prefix and a suffix.

Implement the WordFilter class:
WordFilter(string[] words) Initializes the object with the words in the dictionary.
f(string pref, string suff) Returns the index of the word in the dictionary,
which has the prefix pref and the suffix suff.
If there is more than one valid index, return the largest of them.
If there is no such word in the dictionary, return -1. 

Example 1:
Input
["WordFilter", "f"]
[[["apple"]], ["a", "e"]]
Output
[null, 0]
Explanation
WordFilter wordFilter = new WordFilter(["apple"]);
wordFilter.f("a", "e");
// return 0, because the word at index 0 has prefix = "a" and suffix = "e".

Constraints:
1 <= words.length <= 10**4
1 <= words[i].length <= 7
1 <= pref.length, suff.length <= 7
words[i], pref and suff consist of lowercase English letters only.
At most 10**4 calls will be made to the function f.
"""

# Размышления
# Решение в лоб, которое сразу приходит на ум.
# Для поиска по префиксу и суффиксу можно использовать префиксное дерево.
# Оба дереве приведут нас к какому-то уменьшенному множеству слов.
# И если есть слово с таким префиксом и суффиксом, то оно будет одновременно и в
# prefix множестве и suffix.
# Соберём оба эти множества полными проходами по отобранной ветви деревьев,
# отберём id, которые встретились и там, и там.
# Однако хоть алгоритмическая сложность линейная, но слов очень много,
# и сбор сетов, а затем intersection займёт много времени.

from typing import List, Dict, Optional

class TreeNode:
    def __init__(self, word_id: Optional[int] = None) -> None:
        self.word_id = word_id
        self.children: Dict[str, TreeNode] = {}

class WordFilter:

    def __init__(self, words: List[str]):
        self.prefix_tree = TreeNode()
        self.suffix_tree = TreeNode()
        for i, word in enumerate(words):
            
            curr_node = self.prefix_tree
            for char in word:
                if char not in curr_node.children:
                    curr_node.children[char] = TreeNode()
                curr_node = curr_node.children[char]
            curr_node.word_id = i

            curr_node = self.suffix_tree
            for char in word[::-1]:
                if char not in curr_node.children:
                    curr_node.children[char] = TreeNode()
                curr_node = curr_node.children[char]
            curr_node.word_id = i    

    def f(self, pref: str, suff: str) -> int:
        # Выходим на нужную ноду на префиксе и суффиксе.
        # Если есть слова с таким префиксом и суффиксом, то при поиске в обоих деревьях
        # у них будут одинаковые id, так как это одно и то же слово
        prefix_node = self.prefix_tree
        for char in pref:
            if char not in prefix_node.children:
                return -1
            prefix_node = prefix_node.children[char]

        suffix_node = self.suffix_tree
        for char in suff[::-1]:
            if char not in suffix_node.children:
                return -1
            suffix_node = suffix_node.children[char]

        # Теперь продолжаем поиск из нужных нод, запоминаем все слова
        prefix_words = set()
        stack = [prefix_node]
        while len(stack) != 0:
            curr_node = stack.pop()
            if curr_node.word_id is not None:
                prefix_words.add(curr_node.word_id)
            if len(curr_node.children) > 0:
                stack += curr_node.children.values()

        suffix_words = set()
        stack = [suffix_node]
        while len(stack) != 0:
            curr_node = stack.pop()
            if curr_node.word_id is not None:
                suffix_words.add(curr_node.word_id)
            if len(curr_node.children) > 0:
                stack += curr_node.children.values()

        # Одно слова в обоих деревьях - один и тот же id
        words_idxs = prefix_words.intersection(suffix_words)
        return max(words_idxs) if len(words_idxs) > 0 else -1


# Иной вариант решения, безумный по памяти, но O(1) по производительности.
# Привяжемся к тому, что слова у нас короткие, и просто сгенерируем все-все
# пары префикс суффикс к каждому слову.
# Получится 49n по памяти
class WordFilter:
    def __init__(self, words: List[str]):
        self.store = {}
        for idx, word in enumerate(words):
            n = len(word)
            # Генерируем все префиксы и суффиксы
            for i in range(1, n + 1):
                prefix = word[:i]
                for j in range(1, n + 1):
                    suffix = word[n - j:]
                    self.store[(prefix, suffix)] = idx

    def f(self, pref: str, suff: str) -> int:
        return self.store.get((pref, suff), -1)

# Your WordFilter object will be instantiated and called as such:
obj = WordFilter(['apple'])
param_1 = obj.f('a','e')