from typing import List


class Solution:
    def frequency(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for _ in range(len(nums) + 1)]

        for num in nums:
            count[num] = 1 + count.get(num,0)
        
        for n, c in count.items():
            freq[c].append(n)
        res = []
        print(count)
        print(freq)
        for i in range(len(freq) -  1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
sol = Solution()
print(sol.frequency([1,2,2,3,4,4], 2))