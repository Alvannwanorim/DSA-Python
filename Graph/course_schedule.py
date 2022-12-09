
from typing import List


class Solution:
    def courseSchedule(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preq = {i:[] for i in range(numCourses)}

        for crs, pre in prerequisites:
            preq[crs].append(pre)
        
        visited = set()

        def dfs(crs):
            if crs in visited:
                return False
            if preq[crs] == []:
                return True
            visited.add(crs)
            for pre in preq[crs]:
                if not dfs(pre):
                    return False
            visited.remove(crs)
            preq[crs] =[]
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
            
        return True
            
            


sol = Solution()
print(sol.courseSchedule(2, [[1,0],[0,1]]))
print(sol.courseSchedule(2, [[1,0]]))
