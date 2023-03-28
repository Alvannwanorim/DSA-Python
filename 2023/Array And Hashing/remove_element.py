from typing import List


class Solution:

    def removeElement(self, num: List[int], val: int) -> int:
        k = 0

        for i in range(len(num)):
            if num[i] != val:
                num[i] = num[k]
                k += 1

        return k


sol = Solution()
print(sol.removeElement([1, 2, 2, 3, 4, 2, 2], 2))
