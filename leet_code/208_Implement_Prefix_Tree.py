"""208. Implement Trie (Prefix Tree)

https://leetcode.com/problems/implement-trie-prefix-tree

A trie (pronounced as "try") or prefix tree is a tree data structure
used to efficiently store and retrieve keys in a dataset of strings.
There are various applications of this data structure,
such as autocomplete and spellchecker.

Implement the Trie class:

Trie() Initializes the trie object.
void insert(String word) Inserts the string word into the trie.
boolean search(String word) Returns true if the string word is in the trie
(i.e., was inserted before), and false otherwise.
boolean startsWith(String prefix) Returns true if there is a previously inserted
string word that has the prefix prefix, and false otherwise.

Example 1:
Input
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
Output
[null, null, true, false, true, null, true]

Explanation
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // return True
trie.search("app");     // return False
trie.startsWith("app"); // return True
trie.insert("app");
trie.search("app");     // return True

Constraints:
1 <= word.length, prefix.length <= 2000
word and prefix consist only of lowercase English letters.
At most 3 * 10**4 calls in total will be made to insert, search, and startsWith.
"""

# Размышления
# Задача на воспроизведение структуры.
# Если что-то не понятно, то идём читать, что она из себя представляет.
# Для удобства в реализации дерева можно сделать класс ноды.
# Суть такого дерева в том, что каждая стрелка обозначает букву, и при прохождении
# через ноды у нас составляется слово.
# Каждая нода хранит флаг, что эта последовательность букв реально была добавлена
# и существует.
# В противном же случае означает, что это префикс к какому-то ранее добавленному слову.

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

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
