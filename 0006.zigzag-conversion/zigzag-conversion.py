class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1:return s
        ans_li=['' for _ in range(numRows)]
        index=0
        reverse=False
        for letter in s:
            ans_li[index]+=letter
            if not reverse:
                index+=1
                if index==numRows-1:
                    reverse=True
            else:
                index-=1
                if index==0:
                    reverse=False
        return ''.join(ans_li)
                
                