class Solution:
    def minRemove(self, s: str):
        split_str = list(s)
        stack =[]

        for idx in range(len(s)):
            if s[idx] == '(':
                stack.append(s[idx])
            elif s[idx] == ")":
                if stack: stack.pop()

                else:
                    split_str[idx] = ""
        
        for i in stack:
            split_str[i] = ""
        
        return "".join(split_str)
        