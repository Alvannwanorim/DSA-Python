from typing import List

class Solution:
    def courseSchedule(self, numCourses: int, prerequisites: List[List[int]])->bool:
        preMap = {i:[] for i in range(numCourses)}

        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        visiting = set()

        def dfs(crs):
            if crs in visiting:
                return False
            if preMap[crs] == []:
                return True
            
            visiting.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
                
            visiting.remove(crs)
            preMap[crs] = []

            return True
        
        for c in range(numCourses):
            if not dfs(crs):
                return False
        return True

sol = Solution()
print(sol.courseSchedule(2, [[1,0]]))
print(sol.courseSchedule(2, [[1,0],[0,1]]))


