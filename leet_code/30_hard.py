'''Substring with Concatenation of All Words.'''


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


sol = Solution()
s = 'lingmindraboofooowingdingbarrwingmonkeypoundcake'
words = ['fooo', 'barr', 'wing', 'ding', 'wing']
print(sol.findSubstring(s, words))
