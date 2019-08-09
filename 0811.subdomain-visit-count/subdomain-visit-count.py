class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        dic={}
        for s in cpdomains:
            visit,domain=s.split(' ')
            visit=int(visit)
            domain=domain.split('.')
            for i in range(len(domain)):
                mainname='.'.join(domain[i:])
                if mainname in dic:dic[mainname]+=visit
                else:dic[mainname]=visit
        return [str(y)+' '+x for x,y in dic.items()]