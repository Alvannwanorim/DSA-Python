class Solution:
    def stringSwap(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        if len(s1) != len(s2):
            return False
        
        if sorted(s1) != sorted(s2):
            return False
        
        count = 0

        for x,y in zip(s1,s2):
            if x != y:
                count += 1
        
        return count == 2
sol = Solution()
print(sol.stringSwap("bank", "kanb"))
print(sol.stringSwap("bank", "lanb"))