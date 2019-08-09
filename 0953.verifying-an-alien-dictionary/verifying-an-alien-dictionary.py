class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dic={}
        for index,letter in enumerate(order):
            dic[letter]=str(index+1).zfill(2)
        lastword=''
        for word in words:
            value=''
            for letter in word:
                value+=dic[letter]
            if lastword>value:return False
            lastword=value
        return True
            