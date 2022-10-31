from typing import List


class Solution:
    def eraseOverlappingntervals(self, intervals: List[List[int]]) -> List[List[int]]:
        res = 0

        intervals.sort()
        prevEnd = intervals[0][1]

        for start, end in intervals[1:]:
            if start >= prevEnd:
                prevEnd = end
            else:
                res += 1
                prevEnd = min(end, prevEnd)
        return res
sol = Solution()
print(sol.eraseOverlappingntervals([[1,2],[2,5],[4,7],[8,10],[12,16]]))