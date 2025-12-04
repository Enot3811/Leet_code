"""211. Design Add and Search Words Data Structure

https://leetcode.com/problems/design-add-and-search-words-data-structure/

Design a data structure that supports adding new words
and finding if a string matches any previously added string.

Implement the WordDictionary class:

WordDictionary() Initializes the object.
void addWord(word) Adds word to the data structure, it can be matched later.
bool search(word) Returns true if there is any string in the data structure
that matches word or false otherwise.
word may contain dots '.' where dots can be matched with any letter.

Example:
Input
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output
[null,null,null,null,false,true,true,true]
Explanation
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True

Constraints:
1 <= word.length <= 25
word in addWord consists of lowercase English letters.
word in search consist of '.' or lowercase English letters.
There will be at most 2 dots in word for search queries.
At most 104 calls will be made to addWord and search.
"""

# Размышления
# Задача сразу наталкивает на мысли о prefix tree (208).
# Единственное отличие здесь - наличие точек.
# Для них приходится перебирать все ветви

class TreeNode:
    def __init__(self, is_real: bool = False) -> None:
        self.is_real = is_real
        self.children = {}

class WordDictionary:

    def __init__(self):
        self.root = TreeNode()

    def addWord(self, word: str) -> None:
        curr_node = self.root
        for char in word:
            if char not in curr_node.children:
                curr_node.children[char] = TreeNode()
            curr_node = curr_node.children[char]
        curr_node.is_real = True

    def search(self, word: str) -> bool:
        
        def process_letter(node: TreeNode, idx: int) -> bool:
            # Сделали последний переход
            if idx == len(word):
                return node.is_real

            # Для точки вызываем все ветви
            if word[idx] == '.':
                for child_node in node.children.values():
                    if process_letter(child_node, idx + 1):
                        return True
                else:
                    return False

            # Для буквы одну конкретную ветвь
            if word[idx] in node.children:
                return process_letter(node.children[word[idx]], idx + 1)
            else:
                return False

        return process_letter(self.root, 0)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)