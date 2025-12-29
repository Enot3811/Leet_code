"""Video Stitching.

You are given a series of video clips from a sporting event
that lasted time seconds. These video clips can be overlapping with each other
and have varying lengths.

Each video clip is described by an array clips
where clips[i] = [start[i], end[i]] indicates that the ith clip started
at start[i] and ended at end[i].

We can cut these clips into segments freely.
For example, a clip [0, 7] can be cut into segments [0, 1] + [1, 3] + [3, 7].

Return the minimum number of clips needed so that we can cut the clips
into segments that cover the entire sporting event [0, time].
If the task is impossible, return -1.

Example 1:
Input: clips = [[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]], time = 10
Output: 3
Explanation: We take the clips [0,2], [8,10], [1,9]; a total of 3 clips.
Then, we can reconstruct the sporting event as follows:
We cut [1,9] into segments [1,2] + [2,8] + [8,9].
Now we have segments [0,2] + [2,8] + [8,10]
which cover the sporting event [0, 10].

Example 2:
Input: clips = [[0,1],[1,2]], time = 5
Output: -1
Explanation: We cannot cover [0,5] with only [0,1] and [1,2].

Example 3:
Input: clips = [[0,1],[6,8],[0,2],[5,6],[0,4],[0,3],[6,7],[1,3],[4,7],[1,4],
                [2,5],[2,6],[3,4],[4,5],[5,7],[6,9]], time = 9
Output: 3
Explanation: We can take clips [0,4], [4,7], and [6,9].
 
Constraints:

1 <= clips.length <= 100
0 <= start[i] <= end[i] <= 100
1 <= time <= 100
"""

from typing import List


class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        clips.sort()
        self.clips = [
            clips[i]
            for i in range(len(clips))
            if i == len(clips) - 1 or clips[i][0] != clips[i + 1][0]
        ]
        print(self.clips)
        self.time = time
        self.memory = {}
        return self.make_step(0, 0)

    def make_step(
        self, i: int, current_time: int
    ) -> int:
        # Если набрали нужный таймлайн
        if current_time >= self.time:
            return 0
        # Если клипы закончились, а таймлайн не набран
        elif i == len(self.clips) and current_time < self.time:
            return -1
        # Если образовался промежуток между current time и текущим клипом
        elif self.clips[i][0] > current_time:
            return -1
        # Если уже решали задачу для текущего элемента
        if (i, current_time) in self.memory:
            return self.memory[(i, current_time)]

        # Если нет смысла брать текущий клип
        if self.clips[i][1] <= current_time:
            return self.make_step(i + 1, current_time)
        else:
            # Когда нашли подходящий, необходимо решить, брать ли его
            result1 = self.make_step(i + 1, self.clips[i][1])  # Если взяли
            if result1 == -1:  # и не получилось собрать
                result = result1
            else:  # Если же получилось, то надо проверить, не будет ли лучше,
                result1 += 1
                result2 = self.make_step(i + 1, current_time)  # если не брать
                
                if result2 == -1:
                    result = result1
                else:
                    result = min(result1, result2)
            self.memory[(i, current_time)] = result
            return result
    
    # Someone else's solution
    # def videoStitching(self, clips: List[List[int]], time: int) -> int:
    #     clips.sort()
    #     current_end = 0
    #     count = 0

    #     i = 0
    #     while i < len(clips) and current_end < time:
    #         max_end = current_end
    #         while i < len(clips) and clips[i][0] <= current_end:
    #             max_end = max(max_end, clips[i][1])
    #             i += 1

    #         if max_end == current_end:
    #             # Unable to extend the current range
    #             return -1

    #         current_end = max_end
    #         count += 1

    #     return count if current_end >= time else -1


if __name__ == '__main__':
    sol = Solution()
    cases= [
        (([[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]], 10), 3),
        (([[0,1],[1,2]], 5), -1),
        (([[0,1],[6,8],[0,2],[5,6],[0,4],[0,3],[6,7],[1,3],[4,7],[1,4],[2,5],
           [2,6],[3,4],[4,5],[5,7],[6,9]], 9), 3),
        (([[1, 2]], 1), -1),
        (([[1, 2], [1, 2], [1, 3]], 1), -1),
        (([[0, 2], [0, 2], [0, 2]], 2), 1),
        (([[0, 6], [1, 2], [1, 7], [3, 5], [3, 7], [3, 8], [5, 7], [5, 10],
           [6, 10]], 10), 2),
        (([[0, 6], [1, 2], [1, 7], [3, 5], [3, 7], [3, 8], [5, 7], [5, 10],
           [8, 10]], 10), 2),
        (([[0, 6], [1, 2], [1, 7], [3, 5], [3, 7], [3, 8], [5, 7],
           [8, 10]], 10), 3),
        (([[0, 1], [0, 5], [3, 7], [4, 6], [5, 6], [5, 8], [6, 7], [7, 8]], 8),
         2),
        (([[0, 5], [1, 6], [2, 7], [3, 7], [4, 8], [5, 7], [8, 10]], 10), 3)
    ]
    for inp, ans in cases:
        res = sol.videoStitching(*inp)
        print('Got:', res, 'Exp:', ans)
