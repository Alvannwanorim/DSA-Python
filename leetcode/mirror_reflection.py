from math import gcd, lcm


class Solution:
    def mirrorReflection(self, p: int, q: int):
        l = lcm(p,q)

        if(l//q)%2 == 0:
            return 2
        
        return (l//p)%2



class Solution2:
    def mirrorReflection(self, p: int, q: int):
        GCD = gcd(p,q)

        b, a = p // GCD , q // GCD
        print(GCD, a, b)
        if b % 2 == 0:
            return 2
        return 0 if a % 2 == 0 else 1

sol = Solution2()
print(sol.mirrorReflection(3,2))