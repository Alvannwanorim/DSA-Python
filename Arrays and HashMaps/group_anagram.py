from collections import defaultdict
from typing import List


class Solution:
    def groupAnagram(self, strs = List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26 

            for c in s:
                count[ord(c) - ord("a")] +=1
            
            res[tuple(count)].append(s)
        return list(res.values())
sol = Solution()
print(sol.groupAnagram(['ant', 'tan', 'ate', 'eat']))