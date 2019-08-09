class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        A=[x**2 for x in A]
        A.sort()
        return A
        