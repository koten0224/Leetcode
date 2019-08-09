class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        
        lastNum = None
        moreThan = None
        for num in A:
            if lastNum==None:
                lastNum = num
                continue
            if lastNum == num:
                continue
            elif moreThan == None:
                moreThan = lastNum > num
            elif (lastNum > num) != moreThan:return False
            lastNum = num
        return True
                
            