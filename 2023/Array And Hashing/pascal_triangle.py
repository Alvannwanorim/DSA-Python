from typing import List


class Solution:

    def pascalTriangle(self, numRow) -> List[List[int]]:
        res = [[1]]

        for i in range(numRow - 1):
            temp = [0] + res[-1] + [0]
            row = []

            for j in range(len(res[-1]) + 1):
                row.append(temp[j] + temp[j + 1])

            res.append(row)
        return res


sol = Solution()
print(sol.pascalTriangle(5))
print(sol.pascalTriangle(6))