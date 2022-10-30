from typing import List


class Solution:
    def mergeIntervals(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key = lambda i: i[0])
        output = [intervals[0]]
        for start, end in intervals:
            lastEnd = output[-1][1]

            if start <= lastEnd:
                output[-1][1] = max(end, lastEnd)
            else:
                output.append([start, end])
        return output

sol = Solution()
print(sol.mergeIntervals([[1,2],[2,5],[4,7],[8,10],[12,16]]))