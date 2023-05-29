from typing import List
class Solution:
    def minValue(self, num: List[int])->int:
        res = float("inf")
        l, r = 0, len(num) - 1 

        while l < r:
            if num[l] < num[r]:
                res = min(res, num[l])
                break
            m = (l + r) // 2 
            print(num[m])
            res = min(res, num[m])
            if num[m] >= num[l]:
                l = m + 1
            else:
                r = m - 1
        return  res

sol = Solution()
print(sol.minValue([4, 5, 1, 2, 3]))
print(sol.minValue([9, 10, 11, 7,]))
print(sol.minValue([4,5,6,7,0,1,2]))
