class Solution:
    def decodeString(self, s: str):
        stack = []

        for i in range(len(s)):
            if s[i] != "]":
                stack.append(s[i])
            else:
                subStr = ""
                while stack[-1] != "[":
                    subStr = stack.pop() + subStr
                stack.pop()

                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k 
                
                stack.append(int(k) * subStr)
        
        return "".join(stack)

sol = Solution()
print(sol.decodeString("3[a]2[bc]"))
print(sol.decodeString("2[abc]3[cd]ef"))
