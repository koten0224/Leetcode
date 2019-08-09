class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        li=[]
        for i in range(left,right+1):
            s=str(i)
            if '0' in s:continue
            check=1
            for j in s:
                if i%int(j): check=0
            if check:li.append(i)
        return li