class Solution(object):
    def twoSum(self, nums, target):
        check = {}
        index = 0
        for n in nums:
            p = target-n
            if p not in check:
                check[n] = index
            else: return [check[p],index]
            index += 1
        

                