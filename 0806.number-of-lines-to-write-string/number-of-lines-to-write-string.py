class Solution:
    def numberOfLines(self, widths: List[int], S: str) -> List[int]:
        english="abcdefghijklmnopqrstuvwxyz"
        letter=[]
        for s in S:
            width=widths[english.index(s)]
            if letter:
                if letter[-1]+width>100:letter.append(width)
                else:letter[-1]=letter[-1]+width
            else:letter.append(width)
        return len(letter),letter[-1]