from typing import List


class Solution:

    def canPlantFlowers(self, flowerbed: List[int], n: int) -> bool:
        f = [0] + flowerbed + [0]

        for i in range(1, len(flowerbed) - 1):
            if f[i - 1] == 0 and f[i] == 0 and f[i + 1] == 0:
                f[i] = 1
                n -= 1

        return n <= 0


sol = Solution()
print(sol.canPlantFlowers([0, 0, 0, 0], 2))
