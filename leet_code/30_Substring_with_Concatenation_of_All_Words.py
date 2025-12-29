"""30. Substring with Concatenation of All Words

https://leetcode.com/problems/substring-with-concatenation-of-all-words/

You are given a string s and an array of strings words.
All the strings of words are of the same length.

A concatenated substring in s is a substring
that contains all the strings of any permutation of words concatenated.

For example, if words = ["ab","cd","ef"],
then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab"
are all concatenated strings.
"acdbef" is not a concatenated substring
because it is not the concatenation of any permutation of words.
Return the starting indices of all the concatenated substrings in s.
You can return the answer in any order.

Example 1:
Input: s = "barfoothefoobarman", words = ["foo","bar"]
Output: [0,9]
Explanation: Since words.length == 2 and words[i].length == 3,
the concatenated substring has to be of length 6.
The substring starting at 0 is "barfoo".
It is the concatenation of ["bar","foo"] which is a permutation of words.
The substring starting at 9 is "foobar".
It is the concatenation of ["foo","bar"] which is a permutation of words.
The output order does not matter. Returning [9,0] is fine too.

Example 2:
Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
Output: []
Explanation: Since words.length == 4 and words[i].length == 4,
the concatenated substring has to be of length 16.
There is no substring of length 16 in s that is equal to the concatenation 
of any permutation of words. We return an empty array.

Example 3:
Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
Output: [6,9,12]
Explanation: Since words.length == 3 and words[i].length == 3,
the concatenated substring has to be of length 9.
The substring starting at 6 is "foobarthe".
It is the concatenation of ["foo","bar","the"] which is a permutation of words.
The substring starting at 9 is "barthefoo".
It is the concatenation of ["bar","the","foo"] which is a permutation of words.
The substring starting at 12 is "thefoobar".
It is the concatenation of ["the","foo","bar"] which is a permutation of words.
 
Constraints:
1 <= s.length <= 10**4
1 <= words.length <= 5000
1 <= words[i].length <= 30
s and words[i] consist of lowercase English letters.
"""

# Теги
# Плавающее окно (left-right pointers), Словарь счётчиков (dict counter),
# Очередь (queue)

# Размышления
# Первое, за что можно зацепиться - длина слов, она одинакова.
# То есть можно проходить по строке с шагом в длину слова.
# Но при этом здесь важно заметить, что нам не давали гарантии, что нужные слова будут
# начинаться с нулевого символа. Нужны сдвиги старта от 0 до word_len - 1.
# Второе, нам нужно собрать определённое количество определённых слов в подстроке.
# Значит нужно их считать - dict counter.
# Прибавляем нужный счётчик при прохождении текущего слова.
# Если слово вообще не в словаре, то сброс счётчиков.
# Третье, допустим, мы соберём нашу комбинацию. Как идти дальше?
# Нужно помнить порядок слов, которые мы клали. Нужен stack или скорее queue.
# Вынимаем слева самое старое слово, отнимаем соответствующий счётчик.
# К тому же у нас может быть переизбыток нужных слов, на что нам укажет счётчик.
# И здесь как в задачах с left-right окном, нужно выкидывать старые слова,
# пока счётчик не успокоится, тоже queue.
# Плюс к этому эта очередь поможет легко определять, что последовательность собрана
# без прохода по всему дикту счётчиков.
# Ведь счётчики гарантируют отсутствие лишних слов,
# а значит если len(queue) == len(words), то все слова собраны.

from typing import List
from collections import deque

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        # Делаем словарь счётчиков слов, чтобы отслеживать сбор всех слов в подстроке.
        words_dict = {}
        for word in words:
            if word in words_dict:
                words_dict[word] += 1
            else:
                words_dict[word] = 1
        word_len = len(words[0])

        ans = []

        # Удобнее всего будет проходить строку с шагом word_len,
        # но тогда нужно перебрать все сдвиги от 0 до word_len-1
        for i in range(word_len):

            # Счётчики, которые отслеживают перебор
            curr_words = words_dict.copy()
            # Последовательность, которая позволяет быстро находить нужный счётчик,
            # и вдобавок по её длине можно сразу понять, что мы закончили,
            # так как ненужных дублей не будет благодаря счётчику
            curr_seq = deque()
            for j in range(i, len(s), word_len):
                word = s[j:j + word_len]

                if word in curr_words:
                    curr_words[word] -= 1
                    curr_seq.append(word)

                    # Если перебор, то двигаем левую границу
                    while curr_words[word] < 0 and len(curr_seq) > 0:
                        deleted_word = curr_seq.popleft()
                        curr_words[deleted_word] += 1

                    # Собрали все слова
                    if len(curr_seq) == len(words):
                        # Сейчас индекс стоит на начале последнего слова в подстроке
                        ans.append(j - (len(words) - 1) * word_len)
                        deleted_word = curr_seq.popleft()
                        curr_words[deleted_word] += 1

                # Слово не подходит, сбрасываем всё, что собрали
                else:
                    curr_words = words_dict.copy()
                    curr_seq.clear()
        return ans

cases = [
    (("barfoothefoobarman", ["foo","bar"]), [0,9]),
    (("wordgoodgoodgoodbestword", ["word","good","best","word"]), []),
    (("barfoofoobarthefoobarman", ["bar","foo","the"]), [6,9,12]),
    (("lingmindraboofooowingdingbarrwingmonkeypoundcake", ['fooo','barr','wing','ding','wing']), [13])
]
sol = Solution()
for inp, ans in cases:
    res = sol.findSubstring(*inp)
    print(inp, res, ans)
