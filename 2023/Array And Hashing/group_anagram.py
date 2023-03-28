from typing import List
from collections import defaultdict


class Solution:

    def groupAnagram(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for i in range(len(s)):
                count[ord(s[i]) - ord('a')] += 1

            res[tuple(count)].append(s)

        return res.values()


sol = Solution()
print(sol.groupAnagram(['ant', 'tan', 'eat', 'ate', 'lite', 'tile']))
