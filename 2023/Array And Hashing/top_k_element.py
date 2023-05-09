from typing import List


class Solution:
    def countFreq(self, nums: List[int], k: int):
        count = {}
        freq =  [[] for i in range(len(nums) + 1)]

        print(freq)
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        for n, c in count.items():
            freq[c].append(n)
        
        res = []

        for i in range(len(freq) -1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k: return res

sol = Solution()
print(sol.countFreq([1,1,2,3,4,4,4], 2))
        
