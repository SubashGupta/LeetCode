class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        d1={}
        d2={}
        op=[]
        for i in words[0]:
            d1[i]=d1.get(i,0)+1
        for i in range(1,len(words)):
            for j in words[i]:
                d2[j] = d2.get(j,0)+1
            for j in d1.keys():
                d1[j] = min(d1[j],d2.get(j,0))
            d2={}
        for k,v in d1.items():
            for r in range(v):
                op.append(k)
        return op