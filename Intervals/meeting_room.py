from typing import List


class Solution:
    def meetingRoom(self, intervals: List[List[int]]):
        intervals.sort(key = lambda i: i[0])

        for i in range(1, len(intervals)):
            i1 = intervals[i - 1]
            i2 = intervals[i]

            if i1[1] > i2[0]:
                return False
        return True
sol = Solution()
print(sol.meetingRoom([[0,30],[5,10],[15,20]]))