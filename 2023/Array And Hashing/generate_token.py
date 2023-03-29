class Solution:

    def generateToken(self, s: str, token: str) -> int:
        lastIndex = 0
        tokenCount = 0

        for c in token:
            currentIndex = s.index(c)
            tokenCount += abs(currentIndex - lastIndex)
            lastIndex = currentIndex

        return tokenCount


sol = Solution()
print(sol.generateToken('102030', '201'))
