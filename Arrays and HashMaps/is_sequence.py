class Solution:
    def isSequence(self, s: str, t: str) -> bool:
        i, j = 0, 0

        while i <= len(s) and j <= len(t):
            if s[i] == t[j]:
                i +=1
            j += 1
        return j == len(t)

        

