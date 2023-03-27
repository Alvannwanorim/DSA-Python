class Solution:

    def lastWord(self, s: str) -> int:
        return len(s.split()[-1])


class Solution2:

    def lastWord(self, s: str) -> int:
        i, length = len(s) - 1, 0

        while s[i] == " ":
            i -= 1
        while i > 0 and s[i] != " ":
            length += 1
            i -= 1
        return length


sol = Solution()
sol2 = Solution2()
print(sol.lastWord('Hello'))
print(sol2.lastWord('Hello Word  '))