"""House Rubber II."""


from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        # Calculate ratings for each house
        ratings = []
        for i in range(n):
            ratings.append(nums[i] - nums[i - 1] - nums[(i + 1) % n])

        # Do while there are houses that can be robbed
        robbed = 0
        available_houses = [1 for _ in range(n)]
        while sum(available_houses) != 0:
            print(*nums, sep='\t')
            print(*ratings, sep='\t')
            print()
            # Find the best
            max_rating = ratings[0]
            max_idx = 0
            for i, rating in enumerate(ratings):
                if rating > max_rating:
                    max_idx = i
                    max_rating = rating
            
            # Rob the best
            robbed += nums[max_idx]
            available_houses[max_idx] = 0
            ratings[max_idx] = -9999
            # And discard neighbors
            available_houses[max_idx - 1] = 0
            ratings[max_idx - 1] = -9999
            available_houses[(max_idx + 1) % n] = 0
            ratings[(max_idx + 1) % n] = -9999
            # When discarding neighbors we should change the ratings of
            # their neighbors
            if available_houses[max_idx - 2] == 1:
                ratings[max_idx - 2] += nums[max_idx - 1]
            if available_houses[(max_idx + 2) % n] == 1:
                ratings[(max_idx + 2) % n] += nums[(max_idx + 1) % n]
        return robbed



sol = Solution()
tests = [
    # ([2, 3, 2], 3),
    # ([1, 2, 3, 1], 4),
    # ([1, 2, 3], 3),
    # ([5, 1, 6, 4, 2, 6, 1, 2, 8, 9], 25),
    # ([3, 6, 6, 4, 9, 1], 18),
    # ([943, 231, 331, 981, 398, 3, 463, 547, 276, 713, 129, 414, 642, 147, 827,
    #   852, 950, 887, 399, 629, 403, 12, 505, 644, 685, 633, 777, 357, 70, 543,
    #   115, 882, 912, 85, 237, 876, 556, 502, 426, 699, 885, 372, 668, 99, 897,
    #   209, 388, 186, 101, 738, 990, 577, 583, 108, 736, 313, 820, 14, 740, 49,
    #   801, 892, 941, 263, 597, 734, 517, 223, 939, 325, 269, 256, 611, 401,
    #   493, 968, 396, 861, 398, 993, 730, 655, 504, 309, 601, 360, 775, 320,
    #   487, 223, 973, 356, 383, 45, 247, 32, 153, 491, 351, 586], 30193),
    # ([907, 486, 75, 602, 431, 822, 656, 108, 822, 624, 661, 869, 122, 76, 624,
    #   705, 187, 873, 445, 54], 5676),
    # ([943, 231, 331, 981, 398, 3, 463, 547, 276, 713, 129, 414, 642, 147, 827,
    #   852, 950, 887, 399, 629, 403, 12, 505, 644, 685, 633, 777, 357, 70, 543,
    #   115, 882, 912, 85, 237, 876, 556, 502, 426, 699, 885, 372, 668, 99, 897,
    #   209, 388, 186, 101, 738, 990, 577, 583, 108, 736, 313, 820, 14, 740, 49],
    #   18071),
    # ([94, 23, 33, 98, 39, 3, 46, 54, 27, 71, 12, 41, 64, 14, 82], 395),
    ([82, 94, 23, 1], 105),
]
for inp, ans in tests:
    out = sol.rob(inp)
    print('Out:', out, 'Exp:', ans)
