class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        def check(li):
            for i in range(len(li)-1):
                if li[i]>li[i+1]:return False
            return True
        leng=len(nums)
        if leng<2:return True
        for i in range(leng-1):
            if nums[i]>nums[i+1]:
                return check(nums[:i]+nums[i+1:]) or check(nums[:i+1]+nums[i+2:])
        return True
                
                    
        