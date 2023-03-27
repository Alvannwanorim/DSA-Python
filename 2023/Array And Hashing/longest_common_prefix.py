from typing import List


class Solution:

    def longestCommonPrefix(self, s: List[str]) -> str:
        res = ''
        for i in range(len(s[0])):
            for c in s:
                if i == len(c) or c[i] != s[0][i]:
                    return res

            res += s[0][i]
        return res


sol = Solution()
print(sol.longestCommonPrefix(["flow", "flowing", "flower"]))
