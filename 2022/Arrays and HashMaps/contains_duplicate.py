from typing import List


class Solution: 
    def duplicates(self, nums: List[int]) -> bool:
        hashMap =set()

        for num in nums:
            if num in hashMap:
                return True
            else:
                hashMap.add(num)
        return False
sol = Solution()
print(sol.duplicates([2,3,4,5,6,7]))