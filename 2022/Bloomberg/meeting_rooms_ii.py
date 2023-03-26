from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start = sorted(x[0] for x in intervals)
        end = sorted(x[1] for x in intervals)

        s, e = 0, 0 
        count, res = 0, 0

        while s < len(intervals):
            if start[s] < end[e]:
                s += 1
                count += 1
            else:
                e += 1
                count -= 1
            res = max(res, count)
        return res
sol = Solution()
print(sol.minMeetingRooms([[0,30],[5,25],[15,20]]))
        