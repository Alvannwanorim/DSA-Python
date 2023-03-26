from typing import List


class Solution:
    def courseSchedule(self, numCourses: int, prerequisites: List[List[int]]) ->List[int]:
        preq = {i: [] for i in range(numCourses)}

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
            return True
        res = []
        for c in range(numCourses):
            if dfs(c):
                res.append(c)
        
        return res



sol = Solution()
print(sol.courseSchedule(2, [[1,0]]))
print(sol.courseSchedule(4,[[1,0],[2,0],[3,1],[3,2]]))
            
