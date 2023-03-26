from typing import List


class Solution:

    def concatenate(self, num: List[int]) -> List[int]:
        target = len(num)

        for i in range(target):
            num.append(num[i])

        return num


sol = Solution()
print(sol.concatenate([1, 2, 3, 4]))
