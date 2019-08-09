class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxLen = 0
        Len = 0
        for num in nums:
            if not num:
                Len = 0
                continue
            else:
                Len += 1
                if Len > maxLen:
                    maxLen = Len
        return maxLen