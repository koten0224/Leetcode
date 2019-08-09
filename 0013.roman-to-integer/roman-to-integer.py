class Solution:
    def romanToInt(self, s: str) -> int:
        symbol={
            'M':1000,
            'CM':900,
            'D':500,
            'CD':400,
            'C':100,
            'XC':90,
            'L':50,
            'XL':40,
            'X':10,
            'IX':9,
            'V':5,
            'IV':4,
            'I':1}
        ans = 0
        while s:
            check = s[:2]
            if check in symbol:
                plus = symbol[check]
                s = s[2:]
            else:
                plus = symbol[s[0]]
                s = s[1:]
            ans += plus
        return ans