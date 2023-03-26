from typing import List


class Solution:
    def reversePolishNotation(self, s: List[str])-> int:
        stack =[]

        for c in s:
            if c =="+":
                stack.append(stack.pop() + stack.pop())
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif c == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))
            else:
                stack.append(int(c))
        return stack[0]
sol = Solution()
print(sol.reversePolishNotation(["2","1","+","3","*"]))
print(sol.reversePolishNotation(["4","13","5","/","+"]))
print(sol.reversePolishNotation(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))