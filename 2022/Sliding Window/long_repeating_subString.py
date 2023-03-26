class Solution(object):
    def lengthOfLongestSubstring(self, s):
        i, l = 0, 0
        res = 0
        charSet = set()

        for i, char in enumerate(s):
            while char in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(char)
            res = max(res, i - l + 1)
            i += 1
        return res
sol = Solution()
print(sol.lengthOfLongestSubstring("abcabcbb"))
print(sol.lengthOfLongestSubstring("bbbbb"))
print(sol.lengthOfLongestSubstring("pwwkew"))