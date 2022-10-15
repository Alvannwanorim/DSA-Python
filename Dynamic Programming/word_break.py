from typing import List



def wordBreak(s: str, wordDict: List[str]):
    dp = [False] * (len(s) + 1)
    dp[0] = True

    for i in range(len(s)):
        if(dp[i] == True):
            for word in wordDict:
                if(s[i: i + len(word)] == word and (i + len(word))<=len(s)):
                    dp[i + len(word)] = True
    print(dp)
    return dp[len(s)]

print(wordBreak('abcdef', [ 'ab', 'abc', 'cd', 'def', 'abcd', 'ef', 'c' ]))