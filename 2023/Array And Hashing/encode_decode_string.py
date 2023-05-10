class Codec:
    def encode (self, strs: str):
        res ="" 

        for s in strs:
            res += str(len(s)) + '#' + s
        return res
    
    def decode(self, s: str):
        res = []
        i = 0

        while i < len(s):
            j = i 
            while s[j] !='#':
                j += 1
            length = int(s[i:j])
            res.append(s[j+ 1:length + j+ 1])
            i = j + 1 + length
        return res

sol = Codec()
print(sol.decode(sol.encode(["leet", "code"])))
print(sol.decode(sol.encode([""])))