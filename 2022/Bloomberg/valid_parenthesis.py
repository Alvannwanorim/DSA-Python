class Solution:
    def isValid(self, s: str) -> bool:
        lookup = {"]": "[", ")": "(", "}": "{"}
        stack = []
        for c in s:
            if c not in lookup:
                stack.append(c)
                continue
            if not stack or stack[-1] != lookup[c]:
                return False
            stack.pop()
        print(stack)
        return not stack
sol = Solution()
print(sol.isValid("{()[]}"))
print(sol.isValid("()[]{}"))

class Solution2:
    def isValid(self, s: str) -> bool:
        lookup = {"[": "]", "(": ")", "{": "}"}
        stack = []
        for c in s:
            if c in lookup:
                stack.append(c)
            elif not stack or lookup[stack.pop()] != c:
                return False

        return not stack
sol2 = Solution2()
print(sol2.isValid("()[]{}"))
