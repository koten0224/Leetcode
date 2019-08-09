class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub=''
        leng=0
        for letter in s:
            while letter in sub:sub=sub[1:]
            sub=sub+letter
            if len(sub)>leng:leng=len(sub)
        return leng