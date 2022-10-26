from math import lcm


class Solution:
    def mirrorReflection(self, p: int, q: int):
        l = lcm(p,q)

        if(l//q)%2 == 0:
            return 2
        
        return (l//p)%2

sol = Solution()
print(sol.mirrorReflection(3,1))