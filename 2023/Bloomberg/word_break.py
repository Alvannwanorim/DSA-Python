from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str])->bool:
        dp =[False] * (len(s) + 1 )
        dp[0] = True
        for i in range(len(s)):
            if dp[i] == True:
                for word in wordDict:
                    if s[i:i + len(word)] == word and ( i + len(word)) <= len(s):
                        dp[i + len(word)] = True
        
        return dp[len(s)]
                       