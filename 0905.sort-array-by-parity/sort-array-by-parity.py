class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        return[num for num in A if not num%2]+[num for num in A if num%2]
        