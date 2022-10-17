from typing import List


class Solution:
    def courseSchedule(self, numCourses: int, prerequisites: List[List[int]])-> bool:
        prereq = {i:[] for i in range(numCourses)}

        visiting = set()

        for crs, pre in prerequisites:
            prereq[crs].append(pre)

        def dfs(crs):
            if crs in visiting:
                return False
            if prereq[crs] == []:
                return True
            visiting.add(crs)
            for pre in prereq[crs]:
                if not dfs(pre):
                    return False
                
            visiting.remove(crs)
            prereq[crs] = []
            return True
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
