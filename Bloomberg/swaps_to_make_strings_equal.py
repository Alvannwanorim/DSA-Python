class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        
        if sorted(s1) != sorted(s2):
            False
        count = 0
        
        for i in range(len(s2)):
            if s1[i] != s2[i]:
                count += 1
        
        if (count ==2 or count == 0) and sorted(s1) == sorted(s2):
            return True
        
        return False
sol = Solution()
print(sol.areAlmostEqual("bank", "kano"))
