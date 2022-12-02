from typing import List


class Solution:
    def validPalindrome(self, s: str) ->bool:
        l, r = 0, len(s) - 1

        while l< r:
            while l < r and not self.isAphaNum(s[l]):
                l += 1
            while l < r and not self.isAphaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True
 
    def isAphaNum(self, c:str) ->bool:
        return ((ord("A") <= ord(c) <= ord("Z")) or
            (ord("a") <= ord(c) <= ord("z")) or 
            (ord("0") <= ord(c) <= ord("9")))

sol = Solution()
print(sol.validPalindrome("A man, a plan, a canal: Panama"))