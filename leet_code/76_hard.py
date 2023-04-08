'''
Minimum Window Substring.
'''


from collections import defaultdict, Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target_dict = Counter(t)
        current_dict = defaultdict(int)
        to_collect = len(target_dict)
        right, left = 0, 0
        answer = None
        best_score = None
        while right < len(s):
            if s[right] in target_dict:
                current_dict[s[right]] += 1
                if current_dict[s[right]] == target_dict[s[right]]:
                    to_collect -= 1
                    while to_collect == 0 and left <= right:
                        if s[left] in target_dict:
                            current_dict[s[left]] -= 1
                            if current_dict[s[left]] < target_dict[s[left]]:
                                to_collect += 1
                                score = right + 1 - left
                                if answer is None or score < best_score:
                                    answer = (left, right + 1)
                                    best_score = score
                                    if best_score == len(target_dict):
                                        return s[slice(*answer)]
                        left += 1
            right += 1
        return s[slice(*answer)] if answer else ''


sol = Solution()
s = 'bdab'
t = 'ab'
result = sol.minWindow(s, t)
print(result)
