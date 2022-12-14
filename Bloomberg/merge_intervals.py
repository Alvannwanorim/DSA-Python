from typing import List


class Solution:
    def mergeInterval(self, intervals: List[List[int]]) ->List[List[int]]:
        intervals.sort(key= lambda i: i[0])

        output = [intervals[0]]
        for start, end in intervals:
            lastEnd = output[-1][1]

            if start <= lastEnd:
                output[-1][1] = max(end, lastEnd)
            else:
                output.append([start, end])
            
        return output