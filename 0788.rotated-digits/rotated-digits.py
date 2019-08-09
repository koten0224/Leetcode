class Solution:
    def rotatedDigits(self, N: int) -> int:
        count = 0
        valid = '2569'
        invalid = '347'
        num = 0
        while num < N+1:
            check = False
            snum = str(num)
            index = len(snum)
            for s in snum:
                index-=1
                if s in valid:
                    check = True
                elif s in invalid:
                    check = False
                    break
            num += 10**index
            if check:count+=1
        return count