class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashMap = {}
        if len(s) == len(t):
            return False
        for c in s:
            if c in hashMap:
                hashMap[c] += 1
            else:
                hashMap[c] = 1
        
        for c in t:
            if not hashMap[c]:
                return False
            hashMap[c]  -= 1
        return True

sol = Solution()
print(sol.isAnagram("anagram","nagaran"))