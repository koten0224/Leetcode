class Solution:
    def jump(self, nums: List[int]) -> int:

        leng = i = len(nums)-1
        
        for v in nums[::-1]:
            
            if i==leng:
                nums[i]=0
                
            elif v==0 :
                nums[i]=2**16-1
                
            elif leng-i<=v:
                nums[i]=1
                
            elif v-lastV == 1:
                nums[i]=nums[i+1]
                
            else:
                nums[i] = min(set(nums[i+1:i+v+1]))+1
                
            i-=1
            lastV = v
            
        return nums[0]