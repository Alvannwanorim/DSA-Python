from typing import List


class Solution:

    def duplicates(self, num: List[int]) -> bool:
        hasMap = set()
        for n in num:
            if n in hasMap:
                return True
            hasMap.add(n)
        return False


class Solution2:

    def duplicates(self, num: List[int]) -> bool:
        hashMap = {}
        for n in num:
            if n in hashMap:
                return True
            hashMap[n] = 1

        return False


sol = Solution2()
print(sol.duplicates([1, 1, 2, 3, 4]))
