class Solution(object):
    def findComplement(self, num):
        
        """
        :type num: int
        :rtype: int
        """
        return int(bin(num).replace('0b','n').replace('1','2').replace('0','1').replace('2','0').replace('n','0b'),2)