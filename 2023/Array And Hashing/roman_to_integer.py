class solution:

    def romanToInteger(self, s: str) -> int:
        res = 0
        haspMap = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        for c in s:
            res += haspMap[c]

        if 'IV' in s:
            res -= 2
        if 'IX' in s:
            res -= 2
        if 'XL' in s:
            res -= 20
        if 'XC' in s:
            res -= 20
        if 'CM' in s:
            res -= 200
        if 'CD' in s:
            res -= 200
        return res


sol = solution()
print(sol.romanToInteger('CMXCIV'))  #994
print(sol.romanToInteger('CDXLIV'))  #444
print(sol.romanToInteger('MMMCDXXIV'))  #3,424
