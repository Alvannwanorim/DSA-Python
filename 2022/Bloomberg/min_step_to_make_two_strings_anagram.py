from collections import Counter


class Solution:
    def minSteps(self, s: str, t: str):
        map_s = Counter(s)
        map_t = Counter(t)

        res = 0
        for char in map_s:
            diff = map_s[char] - map_t[char]

            if diff >= 0:
                res += 1
        return res

sol = Solution()
print(sol.minSteps("leetcode","practice"))