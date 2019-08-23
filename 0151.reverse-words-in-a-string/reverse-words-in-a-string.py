class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(re.split(' +',s.strip())[::-1])