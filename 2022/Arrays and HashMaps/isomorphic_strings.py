class Solution:
    def isomorphic(self, s: str, t: str) -> bool:
        sMap, tMap = {}, {}

        for s1, t1 in zip(s, t):
            if((s1 in sMap and sMap[s1] != t1) or (t1 in tMap and tMap[t1] != s1)):
                return False
            sMap[s1] = t1
            tMap[t1] = s1
        
        return True
sol = Solution()
print(sol.isomorphic("egg", "ado"))