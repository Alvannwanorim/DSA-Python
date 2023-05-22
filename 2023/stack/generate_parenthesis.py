class Solution:
    def generateParenthesis(self, n: int):
        res = []
        stack = []
        def backtrack(openN, closeN):
            if closeN == openN == n:
                res.append("".join(stack))
                return 

            if openN < n:
                stack.append('(')
                backtrack(openN + 1, closeN)
                stack.pop()
            if closeN < openN:
                stack.append(')')
                backtrack(openN, closeN + 1)
                stack.pop()
        backtrack(0,0)

        return res
    
sol = Solution()
print(sol.generateParenthesis(4))
print(sol.generateParenthesis(2))
print(sol.generateParenthesis(1))
print(sol.generateParenthesis(5))