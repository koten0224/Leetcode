class Solution:
    def countPrimeSetBits(self, L: int, R: int) -> int:
        count=0
        for val in range(L,R+1):

            num=bin(val).count('1')

            if num<=1:continue
            if num==2 or num==3 or (num%2 and num%3):
                count+=1

        return count