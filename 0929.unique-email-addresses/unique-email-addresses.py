class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        dic={}
        for i in range(len(emails)):
            emails[i]=emails[i].split('@')
            emails[i][0]=emails[i][0].split('+')[0].replace('.','')
            emails[i]='@'.join(emails[i])
            dic[emails[i]]=1
        
        return len(dic)