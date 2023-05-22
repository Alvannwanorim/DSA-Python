from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            
            elif c == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b/a))
            elif c == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            else:
                stack.append(int(c))
        
        return stack[0]
sol = Solution()
print(sol.evalRPN(["4","13","5","/","+"]))
print(sol.evalRPN(["2","1","+","3","*"]))
print(sol.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))

                