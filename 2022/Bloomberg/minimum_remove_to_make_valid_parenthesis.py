class Solution:
    def minRemove(self, s: str):
        indexes_to_remove = set()
        stack =[]

        for i, c  in enumerate(s):
            if c not in "()":
                continue 
            if c == "(":
                stack.append(i)
            
            elif not stack:
                indexes_to_remove.add(i)
            else:
                stack.pop()
        # print(indexes_to_remove)
        indexes_to_remove = indexes_to_remove.union(set(stack))
        # print(indexes_to_remove)
        string_builder = []
        for i, c in enumerate(s):
            if i not in indexes_to_remove:
                string_builder.append(c)
        
        return "".join(string_builder)
sol = Solution()
print(sol.minRemove("lee(t(c)o)de)"))
print(sol.minRemove("))(("))