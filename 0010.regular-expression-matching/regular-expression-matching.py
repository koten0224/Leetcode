class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        result=re.search(p,s)
        if not result:
            return False
        return result.group()==s