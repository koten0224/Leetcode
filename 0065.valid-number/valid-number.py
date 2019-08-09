import re
class Solution:
    def isNumber(self, s: str) -> bool:
        s=s.strip()
        ans = re.compile(r'^[+-]?([0-9]+\.?[0-9]*|\.?[0-9]+)(e-?\+?[0-9]+)?').search(s)
        if not ans : return False
        ans = ans.group(0)
        if not ans : return False 
        return ans==s