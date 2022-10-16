from collections import defaultdict
from typing import Counter, List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) ->List[str]:
        if set(Counter(s).keys()) > set(Counter("".join(wordDict)).keys()):
            return []
        wordSet = set(wordDict)
        dp = [[]] * (len(s)+ 1)
        dp[0] =[""]

        for endIndex in range(1,len(s) + 1):
            sublist = []
            for startIndex in range(0, endIndex):
                word = s[startIndex:endIndex]
                if word in wordSet:
                    for subsentence in dp[startIndex]:
                        sublist.append((subsentence + ' ' + word).strip())
            dp[endIndex] = sublist

        return dp[len(s)]
sol = Solution()
print(sol.wordBreak('abcdef', [ 'ab', 'abc', 'cd', 'def', 'abcd', 'ef', 'c' ]))