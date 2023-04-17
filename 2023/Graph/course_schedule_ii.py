from typing import List

class Solution:
    def courseSchedule(self, numCourses: int, prerequisites: List[List[int]])->bool:
        preMap = {i: [] for i in range(numCourses)}

        for crs,pre in prerequisites:
            preMap[crs].append(pre)

        output = []
        visiting, cycle = set(), set()

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visiting:
                return True
          
            cycle.add(crs)

            for pre in preMap[crs]:
                if dfs(pre) == False:
                    return False
            cycle.remove(crs)
            output.append(crs)
            visiting.add(crs)
            return True
        
        for c in range(numCourses):
            if dfs(c) == False:
                return []
        
        return output

sol = Solution()
print(sol.courseSchedule(2, [[1,0]]))
print(sol.courseSchedule(2, [[1,0],[0,1]]))