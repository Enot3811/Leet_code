"""Substring with Concatenation of All Words.

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


from typing import List
from collections import defaultdict, deque


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_len = len(words[0])
        sequence_len = word_len * len(words)
        word_dict = defaultdict(int)
        for word in words:
            word_dict[word] += 1
        answer = []

        # Обрабатываем последовательность со всеми возможными сдвигами
        # от 0 до word_len
        for i in range(word_len):
            # Копия словаря для коллекционирования слов
            current_words = word_dict.copy()
            # и очередь для сборки последовательности
            sequence = deque()

            # Идём по словам
            for j in range(i, len(s), word_len):
                selected_word = s[j:j + word_len]
                if selected_word in current_words:
                    # Если нужное слово, то в любом случае надо добавить его
                    # в последовательность, но следует решить вопрос с
                    # его необходимым количеством
                    if current_words[selected_word] > 0:
                        current_words[selected_word] -= 1
                    # Если нужное слово, но в чрезмерном колиестве
                    else:
                        # то придётся удалять ранее сохранённые слова
                        # до тех пор, пока не получится уместить текущее,
                        # либо пока очередь не очистится полностью
                        while len(sequence) > 0:
                            deleted_word = sequence.popleft()
                            if selected_word == deleted_word:
                                break
                            else:
                                current_words[deleted_word] += 1
                    sequence.append(selected_word)

                    # Каждый раз проверяем, не собралась ли последовательность
                    if sum(current_words.values()) == 0:
                        answer.append(j - sequence_len + word_len)
                        deleted_word = sequence.popleft()
                        current_words[deleted_word] += 1

                # Если слово, которое не нужно
                else:
                    # то придётся сбросить словарь и очередь
                    if current_words != word_dict:
                        sequence = deque()
                        current_words = word_dict.copy()
        return answer


if __name__ == '__main__':
    sol = Solution()
    s = 'lingmindraboofooowingdingbarrwingmonkeypoundcake'
    words = ['fooo', 'barr', 'wing', 'ding', 'wing']
    print(sol.findSubstring(s, words))
