class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        coun = collections.Counter
        return coun(t) == coun(s)