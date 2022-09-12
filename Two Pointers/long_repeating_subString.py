class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        """
        s="abcadef"
        count=0
        charSet =set()
        
        l =0
        res=3
        s="p -> w -> w -> k -> e -> w"
                          l         i
        count=i-l+1
        charSet= set(k,e,w)
        res =max(res, count)
        TC: o(n) n=length 
        SC: o(n) n= length of our string
        """
        
        """
        res=3
        charSet={c,a,}
        """
        l = 0
        res = 0
        charSet = set()
        for i in range(len(s)):
            while s[i] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[i])
            res = max(res, i - l + 1)
        return res