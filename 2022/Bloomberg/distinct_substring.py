class Solution:
    def distinctSubstring(self, s: str):
        trie, res = dict(), 0
        for i in range(len(s)):
            cur = trie
            for j in range(i, len(s)):
                if s[j] not in cur:
                    cur[s[j]] = dict()
                    res += 1
                cur = cur[s[j]]
        return res
sol = Solution()
print(sol.distinctSubstring("aabbaba"))