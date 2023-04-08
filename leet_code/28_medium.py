'''Find the Index of the First Occurrence in a String.'''


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        answer = -1
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i] == needle[0]:
                answer = i
                for s_let, f_let in zip(haystack[i + 1:], needle[1:]):
                    if s_let != f_let:
                        answer = -1
                        break
                else:
                    return answer
        return answer


sol = Solution()
print(sol.strStr('mississippi', 'issip'))
