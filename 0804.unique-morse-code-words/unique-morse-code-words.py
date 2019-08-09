class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        dic={"A":".-",
             "B":"-...",
             "C":"-.-.",
             "D":"-..",
             "E":".",
             "F":"..-.",
             "G":"--.",
             "H":"....",
             "I":"..",
             "J":".---",
             "K":"-.-",
             "L":".-..",
             "M":"--",
             "N":"-.",
             "O":"---",
             "P":".--.",
             "Q":"--.-",
             "R":".-.",
             "S":"...",
             "T":"-",
             "U":"..-",
             "V":"...-",
             "W":".--",
             "X":"-..-",
             "Y":"-.--",
             "Z":"--.."}
        words=[''.join([dic[i] for i in word.upper()]) for word in words]
        countdic={}
        for i in words:countdic[i]=1
        return len(countdic)