class Solution:

    def validAnagram(self, s: str, k: str) -> bool:
        if len(s) != len(k):
            return False

        countS, countK = {}, {}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countK[k[i]] = 1 + countK.get(k[i], 0)

        return countK == countS


sol = Solution()
print(sol.validAnagram('alvan', 'vanil'))
