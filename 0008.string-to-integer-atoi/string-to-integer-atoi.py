class Solution:
    def myAtoi(self, str: str) -> int:
        s=re.match('[\-\+]?\d+',str.strip())
        if not s:return 0
        ans=int(s.group())
        if ans < -2**31:ans=-2**31
        elif ans > 2**31-1:ans=2**31-1
        return ans