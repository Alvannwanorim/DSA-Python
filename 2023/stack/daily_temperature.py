from typing import List


class Solution:
    def dailyTemperature(self,temperatures: List[int]):
        stack = []
        res = [0] * len(temperatures)
        
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackIn = stack.pop()
                res[stackIn] = i - stackIn
            stack.append((t, i))
        
        return res
sol = Solution()
print(sol.dailyTemperature([73,72, 74,76,70]))
             
