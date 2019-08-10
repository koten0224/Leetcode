class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        return re.findall('(?<=' + first + ' ' + second + ' ).+?(?!\w)' , text)