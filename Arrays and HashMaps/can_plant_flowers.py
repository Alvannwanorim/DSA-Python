from typing import List


class Solution:
    def canPlantFlowers(self, flowerbed: List[int], n: int) -> bool:
        f = [0] + flowerbed + [0]

        for i in range(1, len(flowerbed) -1):
            if flowerbed[i - 1] == 0 and flowerbed[i] == 0 and flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                n -= 1
        print(flowerbed)
        return n <= 0

sol = Solution()
print(sol.canPlantFlowers([0,0,0],2))
