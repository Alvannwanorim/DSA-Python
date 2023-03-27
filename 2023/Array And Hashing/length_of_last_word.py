class Solution:

    def lastWord(self, s: str) -> int:
        return len(s.split()[-1])


sol = Solution()
print(sol.lastWord('Hello Word  '))