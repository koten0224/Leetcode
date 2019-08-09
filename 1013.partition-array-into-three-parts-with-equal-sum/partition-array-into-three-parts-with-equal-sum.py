class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        sum_=sum(A)/3
        if int(sum_)!=sum_:return False
        count = 0
        presum = 0
        for num in A:
            presum += num
            if presum == sum_:
                presum = 0
                count += 1
        return count==3