from typing import List


class Solution:
    def pascalTriangle(self, k: int)->List[List[int]]:
        res =[[1]]

        while k > 1:
            temp = [0] + res[-1] + [0]
            row = []
            for i in range(len(temp) -1):
                row.append(temp[i] + temp[i + 1])
            res.append(row)
            k -= 1
        return res

sol = Solution()
print(sol.pascalTriangle(5))