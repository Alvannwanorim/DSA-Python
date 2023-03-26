from typing import List


class Solution:

    def duplicates(self, num: List[int]) -> bool:
        hasMap = set()
        for n in num:
            if n in hasMap:
                return True
            hasMap.add(n)
        return False


sol = Solution()
print(sol.duplicates([1, 5, 2, 3, 4]))
