class Solution:
    def minRemove(self, s: str):
        split_str = list(s)
        print(split_str)
        stack =[]

        for idx in range(len(s)):
            if s[idx] == '(':
                stack.append(s[idx])
            elif s[idx] == ")":
                if stack: stack.pop()

                else:
                    split_str[idx] = ""
        
        for i in stack:
            print(i)
            split_str[i] = ""
        
        return "".join(split_str)
sol = Solution()
print(sol.minRemove("lee(t(c)o)de)"))
print(sol.minRemove("))(("))