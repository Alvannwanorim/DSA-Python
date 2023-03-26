from typing import List


class solution:
    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        m = len(A)
        n = len(A[0])

        nB = len(B[0])
        res = [[0] * nB for _ in range(m)]

        for i in range(m):
            for j in range(nB):
                res[i][j] = sum(A[i][k] * B[k][j] for k in range(n))
        return res

sol = solution()
print(sol.multiply([[1,0,0],[-1,0,3]],[[7,0,0],[0,0,0],[0,0,1]]))