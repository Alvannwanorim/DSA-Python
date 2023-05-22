class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        map = {")": "(", "]": "[", "}": "{"}

        for c in s:
            if not c in map:
                stack.append(c)
                continue
            if not stack or stack[-1] != map[c]:
                return False
            stack.pop()

        return True if not stack else False


sol = Solution()
print(sol.isValid("()[]{}"))
print(sol.isValid("()[]{})"))