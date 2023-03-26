from typing import List


class Solution:
    def meetingRoom(self, intervals: List[List[int]]):
        start= sorted([x[0] for x in intervals])
        end = sorted([ x[1] for x in intervals])

        res, count = 0,0
        s, e = 0, 0
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
print(sol.meetingRoom([[0,30],[5,10],[15,20]]))